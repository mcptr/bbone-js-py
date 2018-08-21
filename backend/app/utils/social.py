import json
import requests


class SocialError(Exception):
	pass


class Social(object):
	def __init__(self, **kwargs):
		pass


class Facebook(Social):
	def __init__(self, **kwargs):
		self._access_token = kwargs.get("access_token")
		self._version = kwargs.get("version", "v2.5")

	def validate_user(self, uid):
		url = "https://graph.facebook.com/{}/me?access_token={}".format(
			self._version, self._access_token
		)
		r = requests.get(url)
		if r.status_code != 200:
			return False

		data = json.loads(r.text)
		return data.get("id") == uid
