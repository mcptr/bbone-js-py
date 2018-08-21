from app import db
from datetime import datetime


class CategoriesModel(object):
	def fetch(self, **kwargs):
		with db.session("main") as c:
			q = ["select * from views.post_categories"]
			if kwargs.get("pattern", None):
				q.append("where ident ~* %(pattern)s")
				kwargs["pattern"] = "^" + kwargs["pattern"]
			q.append("order by ident asc")
			if kwargs.get("limit", None):
				q.append("limit %(limit)s")
			rs = c.execute(" ".join(q), kwargs)
			return rs.fetchall()
