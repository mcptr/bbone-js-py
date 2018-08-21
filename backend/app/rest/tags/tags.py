from flask import jsonify, request, abort
from flask_restful import Resource
from . model.tags import TagsModel


class Tags(Resource):
	def __init__(self):
		self.model = TagsModel()

	def get(self):
		limit = request.args.get("limit", 20)
		top = request.args.get("top", False)
		pattern = request.args.get("pattern", None)
		params = dict(
			pattern=pattern,
			limit=limit
		)
		reader = self.model.fetch_popular if top else self.model.fetch_list
		data = reader(**params)
		return jsonify({"list": [dict(d) for d in data]})
