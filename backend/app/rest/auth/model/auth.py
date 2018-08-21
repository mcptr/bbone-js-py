from app import db
from app.models.base import Model


class AuthModel(Model):
	def __init__(self):
		Model.__init__(self, "Auth")

	def authenticate(self, user, password, origin, agent, session_id):
		q = (
			"select * from " +
			"auth.authenticate(%s, %s, %s, %s, %s)"
		)
		result = {}
		with db.transaction("main") as tx:
			rs = tx.execute(q, user, password, origin, agent, session_id)
			session_id = rs.fetchone()[0]
			if session_id:
				result["session_id"] = session_id
		return result
