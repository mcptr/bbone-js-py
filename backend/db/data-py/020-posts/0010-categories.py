def populate(cursor):
	categories = ["news", "reviews", "tests", "security", "self"]
	sql = "INSERT INTO storage.post_categories(ident) values(%(value)s)"
	cursor.executemany(sql, [dict(value=cat) for cat in categories])
