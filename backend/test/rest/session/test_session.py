import json
from test.base import AppTestCase


class SessionTest(AppTestCase):
	CONFIG = dict(
		RESTFUL_APPS=["app.rest.session"],
	)

	def test_invalid(self):
		r = self.client.get("/api/session/invalid", follow_redirects=True)
		self.assert_resource_not_found(r)

	def test_anonymous(self):
		r = self.client.post("/api/session/", follow_redirects=True)
		self.assert_response_ok(r)
		session_id = self.get_response_data(r, "id")
		r = self.client.get(
			"/api/session/{}".format(session_id),
			follow_redirects=True
		)
		self.assert_response_json_equals(r, session_id, "id")
		self.assert_response_json_equals(r, None, "user_id")
		self.assert_response_json_equals(r, False, "permanent")
		self.assert_response_json_equals(r, None, "data")

		r = self.client.delete(
			"/api/session/{}".format(session_id),
			follow_redirects=True
		)
		self.assert_response_ok(r)
		r = self.client.get(
			"/api/session/{}".format(session_id),
			follow_redirects=True
		)
		self.assertEquals(r.status_code, 404)

	def test_update(self):
		r = self.client.post("/api/session/", follow_redirects=True)
		self.assert_response_ok(r)
		session_id = self.get_response_data(r, "id")
		test_data = {"key_1": {"key_2": "value"}}
		r = self.client.put(
			"/api/session/{}".format(session_id),
			data=json.dumps(test_data),
			follow_redirects=True,
			content_type="application/json"
		)
		self.assert_response_ok(r)
		response_data = self.get_response_data(r)
		self.assert_response_json_equals(r, test_data, "data")
