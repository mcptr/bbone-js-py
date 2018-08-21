import json
from app import db
from sqlalchemy.sql import func, select

from . import tables


class UserModel(object):
	def __init__(self, session_id):
		self.session_id = session_id
		self.id = None
		self.ident = None
		self.username = None
		self.city = None
		self.country = None
		self.groups = []
		self.last_failure = None
		self.last_success = None
		self.failures = None
		self.confirmed = None

	def ident_exists(self, ident):
		with db.session("main") as s:
			st = select([func.count(tables.users.c.id)])
			st = st.select_from(tables.users)
			st = st.where(tables.users.c.ident == ident)
			return s.execute(st).fetchone()[0]

	def username_exists(self, username):
		with db.session("main") as s:
			st = select([func.count(tables.users.c.username)])
			st = st.select_from(tables.users)
			st = st.where(tables.users.c.username == username)
			return s.execute(st).fetchone()[0]

	def update(self, data):
		print("####### USER UPDATE", data)

	def create(self, data):
		with db.transaction("main") as tx:
			st = tables.users.insert().returning(
				tables.users.c.id,
				tables.users.c.ident,
				tables.users.c.username,
				tables.users.c.last_success,
				tables.users.c.last_failure,
				tables.users.c.failures,
				tables.users.c.city,
				tables.users.c.country,
				tables.users.c.gender,
			)
			params = dict(
				ident=data.get("ident"),
				username=data.get("username"),
				password=data.get("password"),
			)

			if data.get("social_uid"):
				params["social_uid"] = data.get("social_uid")
				params["social_provider"] = data.get("social_provider")

			st = st.values(**params)
			rs = tx.execute(st)
			return rs.fetchone()

	def load(self):
		if self.session_id:
			params = dict(
				session_id=self.session_id
			)
			q = (
				"select * from views.authenticated_users au " +
				"where session_id = %s"
			)
			with db.session("main") as c:
				rs = c.execute(q, (self.session_id,))
				record = rs.fetchone()
				if record:
					self.id = record.user_id
					self.username = record.username
					self.city = record.city
					self.country = record.country
					self.ident = record.user_ident
					self.groups = record.user_groups
					self.last_failure = record.last_failure
					self.last_success = record.last_success
					self.failures = record.failures
					self.confirmed = record.confirmed
					return True
		return False

	def get(self, ident):
		with db.session("main") as c:
			st = tables.users.select().where(
				tables.users.c.ident == ident
			)
			r = c.execute(st)
			return r.fetchone()

	# def update(self, data):
	# 	return self.call_safe("update", data, verbose=True)

	def get_ident(self):
		return self.ident

	def get_name(self):
		return self.username

	def get_session_id(self):
		return self.session_id

	# def get_id(self):
	# 	return "/".join([self.get_ident(), self.get_session_id()])

	def get_id(self):
		return self.id

	def get_data(self):
		return self.data

	def get_groups(self):
		return self.groups

	def __repr__(self):
		return "<User-%d %s/%s>" % (self.id, self.ident, self.session_id)
