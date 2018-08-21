from flask import jsonify, request, abort
from flask_restful import Resource
from . model.posts import PostsModel


class Posts(Resource):
	def __init__(self):
		self._model = PostsModel()

	def get(self, category_id=None):
		offset = 0
		limit = int(request.args.get("limit", 30))
		page = int(request.args.get("page", 1))
		channel_id = int(request.args.get("channel_id", 0))

		if page > 1:
			offset = page * limit

		criteria = dict(
			category_id=category_id,
			channel_id=channel_id,
			offset=offset,
			limit=limit,
			ctime_offset=int(request.args.get("ctime_offset", 0))
		)

		data = self._model.fetch(criteria)
		return jsonify({"list": [dict(d) for d in data]})
