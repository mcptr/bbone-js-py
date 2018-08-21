from flask import jsonify, request, abort, g
from flask_restful import Resource
from . model.post import PostModel
from . model.comments import CommentsModel


class Post(Resource):
	def __init__(self):
		self._model = PostModel()

	def get(self, post_id):
		data = self._model.fetch(post_id)
		if data:
			return jsonify({
				"post": dict((data or {})),
			})
		abort(404)

	def post(self):
		self._model.create(request.data)
