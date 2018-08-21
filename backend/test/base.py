import os
import sys
import time
import json
import hashlib
import logging
import unittest


import sqlalchemy
from app import WebApp
from app import db as app_db
from config.testing import TestingConfig

MY_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(MY_DIR)
DB_UTILS_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "db", "bin")
SCHEMA_DIR = os.path.join(PROJECT_DIR, "db", "schema")


class TestConfig(TestingConfig):
	TESTING = True
	DATABASE = {
		"main": {
			"dsn": None,
			"options": dict(
				pool_size=5,
				max_overflow=0,
				pool_timeout=3,
				#echo=True,
			)
		}
	}

	DB_USER = "tester"
	DB_PASSWORD = "tester"
	DB_HOST = "localhost"

	def __init__(self, config):
		for k in config:
			self.__setattr__(k, config[k])

	def __setattr__(self, name, value):
		self.__dict__[name] = value

	@classmethod
	def set_dsn(cls, db, dbname):
		dsn = cls.get_dsn(dbname)
		cls.DATABASE[db]["dsn"] = dsn
		return dsn

	@classmethod
	def get_dsn(cls, dbname):
		dsn = "postgresql+psycopg2://{}:{}@{}/{}".format(
			cls.DB_USER,
			cls.DB_PASSWORD,
			cls.DB_HOST,
			dbname
		)
		return dsn


class AppTestCase(unittest.TestCase):
	logger = logging.getLogger("AppTestCase")
	logger.addHandler(logging.StreamHandler(sys.stderr))
	logger.setLevel(logging.DEBUG)

	DB_NAME = ""

	@classmethod
	def setUpClass(cls):
		cls._create_test_database()
		dsn = TestConfig.set_dsn("main", cls.DB_NAME)
		cfg = TestConfig((cls.CONFIG or {}))
		cfg.RESTFUL_APPS = (cfg.RESTFUL_APPS or [])
		cfg.RESTFUL_APPS.extend([
			"app.rest.user",
			"app.rest.session",
		])
		instance = WebApp()
		instance.configure_app(cfg)
		cls.app = instance.get_app()
		cls.client = cls.app.test_client()

	@classmethod
	def tearDownClass(cls):
		cls._drop_test_database()

	@classmethod
	def _create_test_database(cls):
		dsn = TestConfig.get_dsn("postgres")
		engine = sqlalchemy.create_engine(dsn)
		conn = engine.connect()
		conn.execute("commit")
		suffix = hashlib.sha1(str(time.time()).encode("utf8")).hexdigest()
		suffix = suffix[:4] + suffix[-4:]
		db_name = "portal_test_" + suffix
		cls.logger.info("Creating database " + db_name)
		conn.execute("create database %s;" % db_name)
		conn.close()
		cls.DB_NAME = db_name
		cls._init_test_database()
		cls.logger.info("#" + "=" * 70 + "\n")

	@classmethod
	def _drop_test_database(cls):
		if cls.DB_NAME:
			cls.logger.info("\n#" + "=" * 70)
			dsn = TestConfig.get_dsn("postgres")
			engine = sqlalchemy.create_engine(dsn)
			conn = engine.connect()
			conn.execute("commit")
			cls.logger.info("Dropping database " + cls.DB_NAME)
			conn.execute(
				"SELECT pg_terminate_backend(pg_stat_activity.pid) "
				"FROM pg_stat_activity "
				"WHERE pg_stat_activity.datname = %s "
				"AND pid <> pg_backend_pid(); ",
				(cls.DB_NAME,)
			)
			conn.execute("drop database %s;" % cls.DB_NAME)
			cls.DB_NAME = None

	@classmethod
	def _init_test_database(cls):
		initdb = os.path.join(DB_UTILS_DIR, "initdb")
		cmd = (
			"{tool} -U{user} -P{password} -D{name} -s " +
			"-w {schema_dir} --sql-schema-in ."
		)
		cmd = cmd.format(
			tool=initdb,
			user=TestConfig.DB_USER,
			password=TestConfig.DB_PASSWORD,
			host=TestConfig.DB_HOST,
			name=cls.DB_NAME,
			schema_dir=SCHEMA_DIR,
		)
		status = os.system(cmd)
		if status:
			msg = "Initializing db failed"
			cls.logger.error(msg)
			raise Exception(msg)

	@classmethod
	def __del__(cls):
		cls._drop_test_database()

	def make_session(self, **kwargs):
		r = self.post_json("/api/session/", follow_redirects=True)
		self.session_id = self.get_response_data(r, "id")
		from app.models.session.tables import sessions
		if kwargs.get("verbose", False):
			with app_db.transaction("main") as tx:
				for s in tx.execute(sessions.select()).fetchall():
					print(s)

	def make_auth(self):
		from app.models.user.tables import users
		from app.models.session.tables import sessions
		self.make_session()
		pid = os.getpid()
		self.username = "testUser-{}".format(pid)
		self.ident = "test-{}@localhost".format(pid)
		self.password = "password-{}".format(pid)
		st = users.insert().returning(users.c.id).values(
			username=self.username,
			ident=self.username,
			password=self.password
		)
		with app_db.transaction("main") as tx:
			r = tx.execute(st)
			self.uid = r.fetchone()[0]
			st = sessions.update().values(user_id=self.uid).where(
				sessions.c.id == self.session_id
			).returning(sessions.c.id)
			result = tx.execute(st).fetchone()[0]
			if not result:
				raise Exception("make_auth failed")

	def collect_headers(self, headers=None):
		d = {
			"User-Agent": "AppTestCase Client"
		}
		if hasattr(self, "session_id"):
			d["X-App-Session"] = self.session_id
		d.update((headers or {}))
		return d

	def get_json(self, url, data=None, **kwargs):
		data = (data or {})
		return self.client.get(
			url,
			data=json.dumps(data),
			content_type="application/json",
			follow_redirects=True,
			headers=self.collect_headers(kwargs.get("headers"))
		)

	def post_json(self, url, data=None, **kwargs):
		data = (data or {})
		return self.client.post(
			url,
			data=json.dumps(data),
			content_type="application/json",
			follow_redirects=True,
			headers=self.collect_headers(kwargs.get("headers"))
		)

	def get_response_data(self, response, path=""):
		data = json.loads(response.data.decode("utf8"))
		if path:
			return self._extract_data(data, path.split("."))
		return data

	def assert_response_ok(self, response):
		self.assertEquals(response.status_code, 200)

	def assert_resource_not_found(self, response):
		self.assertEquals(response.status_code, 404)

	def assert_response_json_equals(self, response, expected, path=""):
		data = json.loads(response.data.decode("utf8"))
		if path:
			data = self._extract_data(data, path.split("."))
			self.assertEquals(data, expected, "Testing value for path: " + path)
		else:
			self.assertEquals(data, expected)

	def _extract_data(self, root, path):
		if len(path) > 1:
			try:
				root = root[path[0]]
			except IndexError as e:
				self.fail("Element '{}' not found for path '{}'".format(
					path[0], ".".join(path)
				))

			return self._extract_data(root[path[0]], path[1:])
		if root and path[0] in root:
			return root[path[0]]
		self.fail("Element '{}' not found for path '{}'".format(
			path[0], ".".join(path)
		))
