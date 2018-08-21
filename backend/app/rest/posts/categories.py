from flask import jsonify, request, abort
from flask_restful import Resource
import time
from datetime import timedelta

from . model.categories import CategoriesModel


class Categories(Resource):
	def __init__(self):
		self._model = CategoriesModel()

	def get(self, **kwargs):
		return self._model.fetch(**dict(
			limit=request.args.get("limit", None),
			pattern=request.args.get("pattern", None)
		))
