from app.rest import api
from . session import Session


api.add_resource(
	Session,
	"/session/",
	"/session/<string:session_id>"
)
