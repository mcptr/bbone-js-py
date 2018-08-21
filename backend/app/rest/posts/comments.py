from flask import jsonify, request, abort, g
from flask_restful import Resource

from . model.comments import CommentsModel


class Comments(Resource):
	def __init__(self):
		self._model = CommentsModel()

	def get(self, post_id):
		result = {}
		comments = self._model.fetch(post_id)
		return jsonify({
			"comments": list(map(lambda r: dict(r), comments))
		})

	def post(self, post_id):
		content = request.json.get("content", "").strip()
		if not content:
			abort(422, "Invalid content")
		data = dict(
			post_id=post_id,
			user_id=int(request.json.get("user_id", 0) or 1),
			parent_id=(int(request.json.get("parent_id", 0)) or None),
			content=content,
		)
		result = self._model.create(data)
		return jsonify(result)

	def delete(self, post_id, comment_id):
		if g.user:
			self._model.delete(comment_id, g.user.get_id())
			return True
		abort(403)

	def patch(self, post_id, comment_id):
		if g.user:
			content = request.json.get("content")
			self._model.update(comment_id, g.user.get_id(), content)
			return True
		abort(403)
