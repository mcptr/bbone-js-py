from flask import current_app, g, request, abort


def check_session(*args, **kwargs):
	from app.models.session import Session
	from app.models.user import UserModel
	g.user = None
	header = current_app.config.get("SESSION_HEADER")
	session_id = request.headers.get(header)
	session = Session()
	session_data = session.read(session_id)
	if session_data:
		g.user = UserModel(session_id)
		g.user.load()
	if request.endpoint in ["session", "status"]:
		pass
	elif request.method == "POST" and request.endpoint == "user":
		if not validate_session(session_id):
			abort(403)
	else:
		if not validate_session(session_id):
			abort(403)
		if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
			if request.endpoint == "auth":
				pass
			elif not g.user or not g.user.get_id():
				print("Request denied (no auth)", request.endpoint)
				abort(403)
	g.session_id = session_id


def validate_session(session_id):
	from app.models.session import Session
	session_model = Session()
	client_origin = (request.remote_addr or "0.0.0.0")
	client_agent = request.user_agent
	session_ok = (
		session_id and
		session_model.touch(session_id, client_agent, client_origin)
	)
	return session_ok


# @current_app.after_request
# def as_json(response):
# 	if isinstance(response, Response):
# 		return response
# 	elif not isinstance(response, str):
# 		return jsonify(dict(results=response))
# 	else:
# 		return response
