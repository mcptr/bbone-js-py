from functools import wraps
from flask import abort, request, g
from app.models.session import Session


def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		user = g.get("user")
		if user and user.get_session_id():
			session_touched = g.get("session_touched", None)
			if not session_touched:
				session = Session()
				session_touched = session.touch(
					user.get_session_id(),
					request.user_agent,
					request.remote_addr
				)
			if session_touched:
				return f(*args, **kwargs)
		abort(401)
	return decorated


def is_same_user(uid):
	user = g.get("user")
	if user:
		user.load()
		return user.get_id() == uid
	return False
