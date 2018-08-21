from flask import abort, request, jsonify, g, current_app
from flask_restful import Resource

from app import auth
from .model.confirmations import ConfirmationsModel


class Confirmation(Resource):
	@auth.requires_auth
	def put(self, action_type, key):
		model = ConfirmationsModel()
		if model.confirm(g.user, action_type, key):
			return True
		abort(404)
