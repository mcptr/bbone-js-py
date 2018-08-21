import os
import mimetypes
from flask import jsonify, request, abort, g
from flask_restful import Resource

#from app import app
from . model.media import MediaModel


class Media(Resource):
	def __init__(self):
		self._model = MediaModel()

	def post(self):
		ids = {}
		for f in request.files:
			fo = request.files[f]
			filename = fo.filename
			mime = (fo.mimetype or mimetypes.guess_type(filename))
			result = self._model.save(fo, mime, **dict(
				title=request.args.get("title", None)
			))
			ids[filename] = {
				"id": result.id,
				# FIXME
				# "url" : os.path.join(app.config.get("MEDIA_URL", ""), result.path)
			}
		if ids:
			return jsonify(ids)
		abort(500)

	def get(self, media_id):
		data = self._model.fetch(media_id)
		if data:
			return jsonify(data)
		abort(404)

	def delete(self, media_id):
		self._model.delete(media_id)
