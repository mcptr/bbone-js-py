import sys
import os
import logging
import jinja2
import celery
from flask import Flask
from flask_restful import Api as RestAPI
from flask_mail import Mail
from sqlalchemy import create_engine, MetaData, select, text
from celery import Celery

from . import rest
from . import db
from . import request_hooks


class App(object):
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.app = Flask(__name__)

	def get_app(self):
		return self.app

	def configure_app(self, config):
		self.app.config.from_object(config)
		self.init_logging()
		self.init_mail()
		self.init_db()
		self.init_core_config()
		self.init_jinja()
		self.init_celery()
		# with self.app.app_context() as ctx:
		# 	from . import views

	def init_logging(self):
		log_dir = os.path.join(self.app.root_path, "var", "log")
		log_file = os.path.join(log_dir, "application.log")
		debug_format = (
			"%(asctime)s %(process)-5s %(thread)s "
			"%(levelname)s (%(name)s) "
			"%(module)s.%(funcName)s:%(lineno)s - %(message)s"
		)

		std_format = (
			"%(asctime)s %(process)-5s %(thread)s "
			"%(levelname)s (%(name)s) - %(message)s"
		)

		logging.basicConfig(
			# filename=log_file,
			level=logging.DEBUG,
			format=std_format,
		)

		logconfig = self.app.config.get("LOGGING", {})
		for lc in logconfig:
			if "level" in logconfig[lc]:
				logger = logging.getLogger(lc)
				logger.setLevel(logconfig[lc]["level"])
				if "handler" in logconfig[lc]:
					logger.addHandler(logconfig[lc]["handler"])


	def init_db(self):
		self.logger.info("Initializing database pool")
		db.initialize(self.app)


	def init_core_config(self):
		self.logger.info("Initializing db core.config")
		cfg = self.app.config.get("DB_CONFIG")
		with db.transaction("main") as tx:
			st = "SELECT core.set_config_value(%(k)s, %(v)s)s"
			tx.execute(st, [dict(k=k, v=cfg[k]) for k in cfg])


	def init_mail(self):
		self.logger.info("Initializing Mail")
		self.app.mail = Mail(self.app)


	def init_jinja(self):
		self.logger.info("Initializing jinja2")
		self.app.jinja_loader = jinja2.ChoiceLoader([
			self.app.jinja_loader,
			jinja2.FileSystemLoader(self.app.config["TEMPLATE_DIRS"]),
		])

class WebApp(App):
	def __init__(self):
		super().__init__()

	def configure_app(self, config):
		super().configure_app(config)
		self.init_rest_api()
		self.app.before_request(request_hooks.check_session)
		from . modules.email import email

	def init_rest_api(self):
		self.logger.info("Initializing REST API")
		with self.app.app_context():
			for dep in self.app.config.get("RESTFUL_APPS", []):
				self.logger.info("RESTFUL: " + dep)
				try:
					mod = __import__(dep)
				except ImportError as e:
					self.logger.exception(e)
					raise
			rest.api.init_app(self.app)

	def init_celery(self):
		self.logger.info("Initializing Celery")
		self.app.celery = Celery(__name__)
		self.app.celery.conf.update(self.app.config)


class FlaskCeleryApp(App, Celery):
	def __init__(self, *args, **kwargs):
		super().__init__()

	def patch_task(self):
		TaskBase = self.Task
		_celery = self

		class ContextTask(TaskBase):
			abstract = True

			def __call__(self, *args, **kwargs):
				print("CALL")
				if flask.has_app_context():
					return TaskBase.__call__(self, *args, **kwargs)
				else:
					with _celery.app.app_context():
						return TaskBase.__call__(self, *args, **kwargs)

		self.Task = ContextTask

	def configure_app(self, config):
		super().configure_app(config)
		self.init_celery()
		self.patch_task()

	def init_celery(self):
		self.logger.info("Initializing Celery")
		self.app.celery = Celery(__name__)
		self.app.celery.app = self.app
		self.app.celery.conf.update(self.app.config)
