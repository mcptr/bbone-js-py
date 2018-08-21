import random


def populate(cursor):
	items = []
	for i in range(1, 50):
		items.append(
			dict(
				user="admin@localhost",
				title="Some title (post #%d)" % i,
				description="This is post's #%d description text" % i,
				content="Some content (post #%d)" % i,
				content_type="TEXT",
				src_url="http://localhost/src/%d" % i,
				thumbnail_url="thumb-%06d.jpg" % i,
				stat_views=random.randint(10, 5000),
				stat_votes_plus=random.randint(10, 200),
				stat_votes_minus=random.randint(10, 200),
				stat_anon_votes_plus=random.randint(10, 200),
				stat_anon_votes_minus=random.randint(10, 200),
			)
		)
	sql = (
		"""
		INSERT INTO storage.posts(
			category_id,
			user_id,
			title,
			description,
			content,
			language_id,
			content_type,
			src_url,
			thumbnail_url,
			stat_views,
			stat_votes_plus,
			stat_votes_minus,
			stat_anon_votes_plus,
			stat_anon_votes_minus,
			channel_id)
		values(
			(select c.id from storage.post_categories c order by random() limit 1),
			(select u.id from auth.users u where ident=%(user)s),
			%(title)s,
			%(description)s,
			%(content)s,
			(select l.id from l10n.languages l order by random() limit 1),
			%(content_type)s,
			%(src_url)s,
			%(thumbnail_url)s,
			%(stat_views)s,
			%(stat_votes_plus)s,
			%(stat_votes_minus)s,
			%(stat_anon_votes_plus)s,
			%(stat_anon_votes_minus)s,
			(select ch.id from storage.post_channels ch order by random() limit 1)
		)
		""")
	cursor.executemany(sql, items)
