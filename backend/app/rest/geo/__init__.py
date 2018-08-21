import json
from flask import Resource, abort, request, jsonify, g
from app.rest import api

# from app.models.geo import Geo


# class GeoCountries(Resource):
# 	def get(self):
# 		geo = Geo()
# 		result = geo.get_countries(request.args.get("pattern"))
# 		return jsonify((result.data() or {}))

# 	@auth.requires_auth
# 	def put(self, session_id):
# 		print(request.json)

# rest_api.add_resource(GeoCountries, "/geo/countries/")


# class GeoCities(Resource):
# 	def get(self, country=None):
# 		geo = Geo()
# 		result = geo.get_cities(request.args.get("pattern"), country)
# 		return jsonify((result.data() or {}))

# 	@auth.requires_auth
# 	def put(self, session_id):
# 		print(request.json)


# rest_api.add_resource(
# 	GeoCities,
# 	"/geo/cities/",
# 	"/geo/countries/<string:country>/"
# )
