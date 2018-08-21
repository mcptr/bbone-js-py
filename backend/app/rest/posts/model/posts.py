import time
from app import db
from sqlalchemy import select, text

from . tables import posts


class PostsModel(object):
	def fetch(self, criteria):
		posts_list = []
		category_id = criteria.get("category_id", None)
		channel_id = criteria.get("channel_id", None)
		ctime_start = criteria.get("ctime_start", None)
		ctime_end = criteria.get("ctime_end", None)
		limit = criteria.get("limit", 10)
		offset = criteria.get("offset", 0)

		st = posts.alias("v").select()

		if category_id:
			st = st.where(posts.c.category_id == category_id)

		if ctime_start and ctime_end:
			st = st.where(posts.c.ctime.between(ctime_start, ctime_end))

		if channel_id:
			st = st.where(posts.c.channel_id == channel_id)

		if offset:
			st = st.offset(offset)

		st = st.limit(limit)

		with db.session() as c:
			rs = c.execute(st)
			return rs.fetchall()
