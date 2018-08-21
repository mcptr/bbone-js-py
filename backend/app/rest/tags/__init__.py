from app.rest import api
from . tags import Tags

api.add_resource(Tags, "/tags/")
