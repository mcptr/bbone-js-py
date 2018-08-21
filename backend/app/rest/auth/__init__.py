from app.rest import api
from . auth import Auth


api.add_resource(Auth, "/auth/")
