from flask import request, abort, jsonify, g
from flask_restful import Resource, reqparse

from app.models.session import Session
from app.models.user import UserModel

from .schema import AuthSchema
from .model.auth import AuthModel


class Auth(Resource):
	def __init__(self, *args, **kwargs):
		self._model = AuthModel()

	def post(self):
		if request.json:
			data = {}
			errors = {}
			(data, errors) = AuthSchema().load(request.json)
			if errors:
				abort(400, errors)
			r = self._model.authenticate(
				data["ident"],
				data["password"],
				(request.remote_addr or "0.0.0.0"),
				str(request.user_agent),
				g.get("session_id", ""),
			)
			if r:
				g.user = UserModel(g.get("session_id", ""))
				g.user.load()
				return jsonify(r)
			abort(403)
		abort(400)

	def _authenticate(self):
		pass
