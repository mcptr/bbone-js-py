def populate(cursor):
	items = ["dev", "sys", "net", "mobile", "legal", "security", "hardware", "c++", "python", "javascript"]
	sql = "INSERT INTO storage.tags(ident) values(%(value)s)"
	cursor.executemany(sql, [dict(value=item) for item in items])
