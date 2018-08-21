def populate(cursor):
	items = ["channel#1", "turboMonkeys", "penetration", "tor users"]
	sql = "INSERT INTO storage.post_channels(ident) values(%(value)s)"
	cursor.executemany(sql, [dict(value=item) for item in items])
