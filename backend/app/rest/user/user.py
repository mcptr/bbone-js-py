import json
import uuid
import time
from flask import abort, request, jsonify, g, current_app, make_response
from flask_restful import Resource
from datetime import datetime

from app import auth
from app.models.user import UserModel
from app.models.session import Session
from app.schema.user import User as UserSchema

from app.utils.social import SocialError, Facebook
from app.modules.email import email

from .model.confirmations import ConfirmationsModel


DATE_FORMAT = "%d-%m-%Y"


def prepare_user_result(user):
	columns = [
		"id", "username", "ctime", "confirmed",
		"last_success", "last_failure", "failures",
		"city", "country", "gender", "groups",
		"about"
	]
	result = {}
	for c in columns:
		result[c] = user.get(c)
	return result


class User(Resource):
	def post(self):
		schema = UserSchema()
		(data, errors) = schema.load(request.json)

		response = None
		user = None
		if errors:
			response = jsonify(errors)
			response.status_code = 400
			return response

		if data.get("social_uid") or data.get("social_provider"):
			try:
				user = self._handle_social_user(data)
			except SocialError as e:
				pass
		else:
			user = self._handle_regular_user(data)
		if user:
			g.user.ident = user.ident
			g.user.username = user.username
			cm = ConfirmationsModel()
			cm_key = cm.create(user, "registration")
			params = dict(user=user, request=request, confirmation_key=cm_key)
			email.enqueue("Welcome", user.id, "registration", **params)
			return jsonify(prepare_user_result(dict(user)))
		return make_response("", 400)

	def _validate_social_auth(self, data):
		uid = data.get("social_uid")
		provider = data.get("social_provider")
		if provider.lower() == "facebook":
			social = Facebook(access_token=data.get("social_access_token"))
			return social.validate_user(uid)
		return False

	def _handle_social_user(self, data):
		# generate random password for social users
		if not self._validate_social_auth(data):
			raise SocialError("Invalid social auth")
		user = None
		data["password"] = str(uuid.uuid4()) + str(time.time())
		session_id = g.get("session_id", None)
		model = UserModel(session_id)
		registered = model.ident_exists(data["ident"])
		session_model = Session()
		if registered:  # social auth already checked
			user = model.get(data["ident"])
		else:
			if model.username_exists(data["username"]):
				data["username"] += "-%s" % (time.strftime("%H%M%S"))
			user = model.create(data)

		if user:
			session_model.update(
				session_id,
				user_id=user.id,
				social_access_token=data.get("social_access_token")
			)
		return user

		# check if ident exists
		#- if true - load and return
		#- else

	def _handle_regular_user(self, data):
		session_model = Session()
		session_id = g.get("session_id", None)
		model = UserModel(session_id)
		user = model.create(data)
		if user:
			session_model.update(
				session_id,
				user_id=user.id
			)
			return user
		return None


	# def delete(self, session_id):
	# 	pass


class UserDetails(Resource):
	@auth.requires_auth
	def get(self, uid):
		if auth.is_same_user(uid):
			user = g.user
			# data = user.get_data()
			# dob = data.get("date_of_birth", None)
			# if dob:
			# 	d = datetime.fromtimestamp(dob)
			# 	data["date_of_birth"] = d.strftime("%d-%m-%Y")
			return jsonify(prepare_user_result(user.__dict__))
		abort(403)

	@auth.requires_auth
	def put(self, uid):
		if auth.is_same_user(uid):
			user = g.get("user")
			data = request.json
			self._prepare_data(data)
			errors = self._validate_data(data)
			if errors:
				result = jsonify(errors)
				result.status_code = 400
				return result
			else:
				self._transform_data(data)
				response = user.update(data)
				data = response.data()
				result = jsonify(data)
				if response.is_failed():
					result.status_code = 400
				return result
		abort(403)

	def _prepare_data(self, data):
		fields = [
			"name", "country", "city", "gender",
			"address", "phone", "date_of_birth"
		]
		for f in fields:
			if data.get(f):
				v = data[f].strip()
				data[f] = v if v else None

	def _validate_data(self, data):
		errors = {}
		try:
			if "date_of_birth" in data:
				d = datetime.strptime(data["date_of_birth"], DATE_FORMAT)
		except Exception as e:
			errors["date_of_birth"] = ["Invalid date"]
		return errors

	def _transform_data(self, data):
		if "date_of_birth" in data:
			d = datetime.strptime(data["date_of_birth"], DATE_FORMAT)
			data["date_of_birth"] = int(d.timestamp())
