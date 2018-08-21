def populate(cursor):
	int_values = [
		{
			"ident": "session_max_age",
			"option_type": "INT",
			"int_value": 900
		},
		{
			"ident": "max_login_failures",
			"option_type": "INT",
			"int_value": 10
		},
	]

	sql = (
		"INSERT INTO core.config(ident, option_type, int_value) " +
		"values(%(ident)s, %(option_type)s, %(int_value)s)"
	)
	cursor.executemany(sql, int_values)
