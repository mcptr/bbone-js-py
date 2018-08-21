import os
import json
from app import db
from test.base import AppTestCase


class AuthTest(AppTestCase):
	CONFIG = dict(
		RESTFUL_APPS=[
			"app.rest.auth",
			"app.rest.user",
			"app.rest.session",
		],
	)

	def setUp(self):
		self.make_session()

	def test_invalid(self):
		r = self.get_json("/api/auth/invalid/", follow_redirects=True)
		self.assertEquals(r.status_code, 404)

		r = self.post_json("/api/auth/", follow_redirects=True)
		self.assertEquals(r.status_code, 400, "Invalid data")

	def test_authenticate(self):
		from app.models.user.tables import users

		self.make_auth()

		r = self.post_json(
			"/api/auth/",
			data={"ident": self.username, "password": None},
		)
		self.assertEquals(r.status_code, 400, "Invalid data: Empty password")
		r = self.post_json(
			"/api/auth/",
			data={"ident": self.username, "password": "invalid"}
		)
		self.assertEquals(r.status_code, 403)

		r = self.post_json(
			"/api/auth/",
			data={"ident": self.username, "password": self.password}
		)
		self.assertEquals(r.status_code, 200, "Auth success")
		data = self.get_response_data(r)
		self.assertNotEqual(data["session_id"], None)
