from app.rest import api
from . categories import Categories
from . posts import Posts
from . post import Post
from . comments import Comments


api.add_resource(Categories, "/post/categories/")

api.add_resource(
	Posts,
	"/posts/",
	"/posts/<int:category_id>/",
)

api.add_resource(
	Post,
	"/post/",
	"/post/<int:post_id>/"
)
api.add_resource(
	Comments,
	"/post/<int:post_id>/comments",
	"/post/<int:post_id>/comments/<int:comment_id>"
)
