def populate(cursor):
	items = [
		dict(iso_code="en", ident="English"),
		dict(iso_code="fr", ident="French"),
		dict(iso_code="pl", ident="Polish"),
		dict(iso_code="de", ident="German"),
		dict(iso_code="ru", ident="Russian"),
		dict(iso_code="ee", ident="Estonian"),
		dict(iso_code="fi", ident="Finnish"),
		dict(iso_code="se", ident="Swedish"),
		dict(iso_code="no", ident="Norwegian"),
	]

	sql = (
		"INSERT INTO l10n.languages(iso_code, ident) "
		"values(%(iso_code)s, %(ident)s)"
	)
	cursor.executemany(sql, items)
