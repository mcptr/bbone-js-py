from app import db


class TagsModel(object):
	def fetch_list(self, **kwargs):
		pattern = kwargs.pop("pattern", None)
		limit = kwargs.pop("limit", None)
		params = []
		q = (
			"select * from storage.tags " +
			"where active = true "
		)

		if pattern:
			q += "and ident ~ %s"
			params.append("^" + pattern)
		if limit:
			q += " limit %s "
			params.append(limit)
		with db.session("main") as c:
			rs = c.execute(q, params)
			return rs.fetchall()

	def fetch_popular(self, **kwargs):
		params = []
		limit = kwargs.pop("limit", None)
		q = "select * from views.tags_popularity where active = true "
		if limit:
			q += " limit %s "
			params.append(limit)
		with db.session("main") as c:
			rs = c.execute(q, params)
			return rs.fetchall()
