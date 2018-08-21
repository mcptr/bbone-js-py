from app import db


class CommentsModel(object):
	_query_fetch = (
		"select id, parent_id, lvl, post_id, user_id, user_active, author, " +
		"score, ctime, content, deleted, deleted_by " +
		"from storage.get_post_comments_flat(%s) " +
		"as (id bigint, parent_id bigint, lvl int, post_id int, " +
		"user_id int, user_active boolean, author varchar, ctime int, score int, "
		"content text, deleted boolean, deleted_by varchar)"
	)

	_query_create = (
		"insert into storage.post_comments" +
		"(post_id, user_id, parent_id, content) " +
		"values(%(post_id)s, %(user_id)s, %(parent_id)s, %(content)s) " +
		"returning id"
	)

	def fetch(self, post_id):
		with db.session("main") as c:
			rs = c.execute(self._query_fetch, (post_id,))
			return rs.fetchall()

	def create(self, data):
		with db.transaction("main") as tx:
			rs = tx.execute(self._query_create, data)
			comment = rs.fetchone()
			q = self._query_fetch + " WHERE id = %s"
			rs = tx.execute(q, (data.get("post_id"), comment.id))
			tx.connection.commit()
			comment = rs.fetchone()
			return comment

	def delete(self, comment_id, user_id):
		q = (
			"update storage.post_comments " +
			"set deleted = true " +
			"where id = %s and user_id = %s"
		)

		with db.transaction("main") as tx:
			tx.execute(q, (comment_id, user_id))
			return True
		return False

	def update(self, comment_id, user_id, content):
		q = (
			"update storage.post_comments " +
			"set content = %s " +
			"where id = %s and user_id = %s and deleted = false"
		)

		with db.transaction("main") as tx:
			tx.execute(q, (content, comment_id, user_id))
			return True
		return False
