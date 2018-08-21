import random


def populate(cursor):
	cursor.execute("select id from storage.posts")
	post_ids = cursor.fetchall()

	sql = (
		"select array_agg(id) from storage.tags " +
		"order by random() limit 3"
	)
	cursor.execute(sql)
	tag_ids = cursor.fetchone()[0]

	for post_id in post_ids:
		t_ids = list(set(list(
			map(
				lambda idx: tag_ids[idx],
				map(
					lambda r: random.randint(0, len(tag_ids) - 1),
					range(1, 5)
				)
			)
		)))
		sql = (
			"INSERT INTO storage.posts_tags_map(post_id, tag_id) " +
			"values(%s, %s)"
		)
		cursor.executemany(sql, [(post_id, tag_id) for tag_id in t_ids])
