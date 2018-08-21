import uuid
import json
from app import db
from app.models.base import Model
#from nix.core.request import Request

from . tables import sessions


class BaseSession(Model):
	def __init__(self):
		Model.__init__(self, "Session")

	def create(self, client_origin, client_agent):
		pass

	def auth_create(self, user, password, client_origin, client_agent):
		pass

	def destroy(self, session_id):
		pass

	def touch(self, session_id):
		pass

	def read(self, session_id):
		pass


class Session(BaseSession):
	def __init__(self):
		BaseSession.__init__(self)

	def create(self, client_origin, client_agent):
		with db.transaction("main") as tx:
			session_id = str(uuid.uuid4())
			st = sessions.insert(returning=sessions.c).values(
				id=session_id,
				client_origin=str(client_origin),
				client_agent=str(client_agent),
			)
			rs = tx.execute(st)
			tx.connection.commit()
			return rs.fetchone()

	def destroy(self, session_id):
		with db.transaction("main") as tx:
			st = sessions.delete().where(sessions.c.id == session_id)
			tx.execute(st)
			tx.connection.commit()

	def touch(self, session_id, client_agent, client_origin):
		with db.transaction("main") as tx:
			rs = tx.execute(
				"select * from auth.touch_session(%s, %s, %s) as result",
				(session_id, str(client_agent), str(client_origin))
			)
			return rs.fetchone()[0]

	def read(self, session_id):
		with db.transaction("main") as tx:
			rs = tx.execute(
				"select * from auth.read_session(%s) as " +
				"(id varchar, ctime timestamp, mtime timestamp, user_id int, " +
				"permanent boolean, data json)",
				(session_id, )
			)
			record = rs.fetchone()
			record = dict(record or {})
			if record and record.get("data"):
				record["data"] = json.loads(record.get("data"))
			return record

	def update_data(self, session_id, data):
		data = (data or {})
		session_data = None
		if data:
			r = self.read(session_id)
			session_data = (r.get("data") or {})
			session_data.update(data)

		with db.transaction("main") as tx:
			st = sessions.update(returning=sessions.c)
			st = st.values(
				data=(json.dumps(session_data) if session_data else None),
			)
			st = st.where(sessions.c.id == session_id)
			rs = tx.execute(st)
			return rs.fetchone()

	def update(self, session_id, **kwargs):
		with db.transaction("main") as tx:
			st = sessions.update(returning=sessions.c)
			st = st.values(**kwargs)
			st = st.where(sessions.c.id == session_id)
			rs = tx.execute(st)
			return rs.fetchone()

# class SessionExtern(BaseSession):
# 	def __init__(self):
# 		BaseSession.__init__(self)

# 	def create(self, client_origin, client_agent):
# 		req = Request()
# 		req.data.update(dict(
# 			client_origin=client_origin,
# 			client_agent=client_agent
# 		))
# 		return self.call_safe("create", req, verbose=True)

# 	def auth_create(self, user, password, client_origin, client_agent):
# 		req = Request(schema="api/session/auth_create")
# 		req.data.update(dict(
# 			user=user,
# 			password=password,
# 			client_origin=client_origin,
# 			client_agent=client_agent
# 		))
# 		return self.call_safe("auth_create", req, verbose=True)

# 	def destroy(self, session_id):
# 		req = Request(schema="api/session/session")
# 		req.data["session_id"] = session_id
# 		return self.call_safe("destroy", req, verbose=True)

# 	def touch(self, session_id):
# 		req = Request(schema="api/session/session")
# 		req.data["session_id"] = session_id
# 		return self.call_safe("touch", req, verbose=True)

# 	def read(self, session_id):
# 		req = Request(schema="api/session/session")
# 		req.data["session_id"] = session_id
# 		return self.call_safe("read", req, verbose=True)
