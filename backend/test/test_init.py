from test.base import AppTestCase


class TestInit(AppTestCase):
	CONFIG = dict(
		RESTFUL_APPS=[
			"app.rest.status",
		],
	)

	def setUp(self):
		self.make_auth()

	def test_init(self):
		r = self.get_json("/api/status/")
		self.assert_response_ok(r)
		self.assert_response_json_equals(r, dict(status=True))
