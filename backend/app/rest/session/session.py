import json
import time
from flask import abort, request, jsonify, g, make_response
from flask_restful import Resource

from app.models.session import Session as SessionModel


class Session(Resource):
	cache = {}

	def __init__(self):
		self._model = SessionModel()

	def post(self):
		data = self._model.create(
			(request.remote_addr or "0.0.0.0"),
			str(request.user_agent)
		)
		if data:
			data = self._model.read(data.id)
			return jsonify(dict(data))
		abort(400)

	def get(self, session_id=None):
		response = self._model.read(session_id)
		if response:
			return jsonify(response)
		abort(404)

	def delete(self, session_id=None):
		self._model.destroy(session_id)
		return ""

	def put(self, session_id=None):
		data = self._model.update(
			session_id, data=json.dumps(request.json)
		)
		if data:
			data = self._model.read(session_id)
			if data:
				return jsonify(dict(data))
		abort(400)


class SessionExtern(Resource):
	def __init__(self):
		Resource.__init__(self)
		self.model = SessionModel()

	def _validate_session(self, session_id=None):
		if not session_id:
			abort(404)

	def post(self):
		response = self.model.create(
			(request.remote_addr or "0.0.0.0"),
			str(request.user_agent or "")
		)
		if response.is_ok():
			return response.data()
		elif response.is_communication_error():
			abort(503)
		else:
			abort(401)

	def get(self, session_id=None):
		self._validate_session(session_id)
		response = self.model.read(session_id)
		if response.is_ok():
			return jsonify(response.data())
		abort(404)

	def delete(self, session_id=None):
		self._validate_session()
		response = self.model.destroy(session_id)
		if response.is_ok():
			return True
		return abort(500)

	def put(self, session_id=None):
		self._validate_session()
		pass


#from app.utils import auth
#
# class AuthSession(Resource):
# 	"""Create new authenticated session"""

# 	def post(self):
# 		schema = manager.load("api/session/auth_create")
# 		data = schema.data()
# 		model = SessionModel()
# 		user = g.get("user")
# 		if user:
# 			response = model.read(user.get_session_id())
# 			if response.is_ok():
# 				return response.data()
# 		data["user"] = request.json.get("user")
# 		data["password"] = request.json.get("password")
# 		data["client_origin"] = request.remote_addr
# 		data["client_agent"] = str(request.user_agent)
# 		if schema.validate(data):
# 			response = model.auth_create(
# 				data["user"],
# 				data["password"],
# 				data["client_origin"],
# 				data["client_agent"]
# 			)
# 			if response.is_ok():
# 				session["session_id"] = response.data("session_id")
# 				session["user_id"] = response.data("uid")
# 				session["tstamp"] = time.time()
# 				session["auth_bits"] = auth.hash_user_bits(request)
# 				return response.data()
# 			elif response.is_communication_error():
# 				abort(503)
# 		abort(401)
