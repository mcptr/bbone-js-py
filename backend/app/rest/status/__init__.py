from flask_restful import Resource
from flask import jsonify
from app.rest import api

from app.modules.email import email


class Status(Resource):
	def get(self):
		return jsonify({"status": True})

api.add_resource(Status, "/status/")
