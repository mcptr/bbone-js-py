import socket
from marshmallow import Schema, fields, validates_schema, ValidationError
from flask import current_app

from app.models.user import UserModel


class User(Schema):
	ident = fields.Email(required=True)
	username = fields.String(required=True)
	password = fields.String(required=True)
	social_uid = fields.String()
	social_provider = fields.String()
	social_access_token = fields.String()

	@validates_schema
	def validate_username(self, data):
		username = data.get("username")
		if username and len(username) < 2:
			raise ValidationError(
				"Username must be at least 2 characters long",
				"username"
			)

		model = UserModel(None)
		if not data.get("social_uid") and model.username_exists(username):
			raise ValidationError("Username already taken", "username")

	@validates_schema
	def validate_password(self, data):
		password = data.get("password")
		if password and len(password) < 6:
			raise ValidationError(
				"Password must be at least 6 characters long",
				"password"
			)

	@validates_schema
	def validate_ident(self, data):
		ident = data.get("ident")
		if ident and "@" in ident:
			host = ident.split("@")[1].lower()
			is_devel = (
				current_app.config.get("TESTING") or
				current_app.config.get("DEVELOPMENT")
			)
			if not is_devel:
				try:
					address = socket.gethostbyname(host)
					if address == host:
						socket.getaddrinfo(host, 25)
				except socket.gaierror:
					raise ValidationError("Invalid address", "ident")
		model = UserModel(None)
		if not data.get("social_uid") and model.ident_exists(ident):
			raise ValidationError("Already registered", "ident")

	@validates_schema
	def validate_social(self, data):
		provider = data.get("social_provider", "").lower()
		supported = ["facebook", "google", "twitter"]
		if provider and provider not in supported:
			raise ValidationError(
				"Unsupported social provider",
				"social_provider"
			)
