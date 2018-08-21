def populate(cursor):
	items = [
		{
			"ident": "admin@localhost",
			"password": "admin",
			"groups": ["admin"],
			"username": "Administrator",
			"active": True,
		},
		{
			"ident": "test-user-001@localhost",
			"password": "test-user",
			"groups": ["user"],
			"username": "Test User 01",
			"active": False,
		},
		{
			"ident": "example-user-001@localhost",
			"password": "example-user",
			"groups": ["user"],
			"username": "ExampleUser",
			"active": False,
		},
		{
			"ident": "fake-moderator@localhost",
			"password": "fake-moderator",
			"groups": ["moderator", "user"],
			"username": "Fake Moderator",
			"active": False,
		},
		{
			"ident": "staff@localhost",
			"password": "staff-user",
			"groups": ["user", "staff"],
			"username": "Staff User",
			"active": False,
		},
	]

	sql = (
		"INSERT INTO auth.users(ident, username, password, active)" +
		"values(%(ident)s, %(username)s, %(password)s, %(active)s)"
		)
	cursor.executemany(sql, items)
	for user in items:
		sql = (
			"insert into auth.user_group_map(user_id, group_id)" +
			"values(" +
			"((select u.id from auth.users u where LOWER(ident) = LOWER(%s)))," +
			"((select g.id from auth.groups g where LOWER(ident) = LOWER(%s))))"
		)
		print([[user["ident"], group] for group in user["groups"]])
		cursor.executemany(sql, [
			[user["ident"], group] for group in user["groups"]
		])
