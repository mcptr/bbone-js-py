from app import db
from .. schema.post import schema

from . tables import posts


class PostModel(object):
	def _validate(self, data):
		print(schema)
		pass

	def fetch(self, post_id):
		st = posts.select().where(posts.c.id == post_id)
		with db.session() as c:
			return c.execute(st).fetchone()

	def create(self, data):
		if self._validate(data):
			return True
