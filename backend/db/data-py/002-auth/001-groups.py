def populate(cursor):
	items = ["admin", "staff", "moderator", "user"]

	sql = "INSERT INTO auth.groups(ident) values(%s)"
	cursor.executemany(sql, [[group] for group in items])
