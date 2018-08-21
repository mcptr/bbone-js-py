from app.rest import api
from . user import User
from . user import UserDetails

from . confirmation import Confirmation

api.add_resource(User, "/user/", endpoint="user")
api.add_resource(UserDetails, "/user/<int:uid>")
api.add_resource(
	Confirmation,
	"/confirmation/<string:action_type>/<string:key>"
)
