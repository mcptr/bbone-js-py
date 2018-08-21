import random


def populate(cursor):
	comment = (
		"LEVEL 0: This is a comment text. " +
		"This started a new thread in comments section " +
		"under the post you are viewing. " +
		"This text should be long, but i do not have a lorem ipsum helper")

	first_reply = (
		"LEVEL 1: This is a reply for the comment above. " +
		"This text should be long, but it is not...")

	second_reply = "LEVEL 2: This is a nested reply for the reply above. "
	third_reply = (
		"LEVEL 3: This is a nested reply for " +
		"the second nested reply above. "
	)

	fourth_reply = (
		"LEVEL 4: This is a fourth nested reply." +
		"Let's make this text a little longer." +
		"13 października ok. godz. 21:00 na telefony korporacyjne " +
		"MON w sieci Plus GSM, wykonano setki, jeśli nie tysiące " +
		"prób połączeń z numeru rozpoczynającego się od +79, " +
		"czyli pochodzącego z Rosji. O sprawie dowiadujemy się od " +
		"jednego z żołnierzy pewnej podwarszawskiej jednostki. " +
		"Telefony mieli otrzymać praktycznie wszyscy pracownicy jednostki, " +
		"zarówno wojskowi jak i cywile."
	)

	fifth_reply = (
		"LEVEL 5: This is a fifth nested reply." +
		"""Pierwsze godziny w pracy upłynęły jej tak jak zwykle.
		Najpierw weryfikacja zaległych umów i dodawanie komentarzy
		do losowo wybranych zdań. Jej złota zasada: co najmniej jedna
		uwaga na stronę. “Jeśli prawnik niczego nie dopisze,
		pomyślą, że to stanowisko jest zbędne“. Potem pisanie wniosków.
		To lubiła najbardziej. Szło jej błyskawicznie, bo miała kilka
		gotowych szablonów jeszcze z czasów studiów i kolejne pisma
		tworzyła na zasadzie copy & paste. Przed stworzeniem pliku
		cofała systemowy zegar o godzinę. Robiła to odkąd jej były
		chłopak, informatyk, powiedział jej że w metadanych dokumentu widać,
		że nad 10 stronnicowym pismem pracowała tylko 5 minut,
		a każdy klient może to zweryfikować za pomocą narzędzia exiftool."""
	)

	sql = "select array_agg(id) from storage.posts"
	cursor.execute(sql)
	post_ids = cursor.fetchone()[0]

	for post_id in post_ids:
		for lvl_0 in range(0, random.randint(1, 8)):
			q = (
				"insert into storage.post_comments " +
				"(post_id, user_id, content, parent_id) " +
				"values(%(post_id)s, " +
				"(select u.id from auth.users u order by random() limit 1), " +
				"%(content)s, %(parent_id)s)" +
				"returning id")
			cursor.execute(q, {
				"post_id": post_id,
				"content": comment,
				"parent_id": None,
			})
			thread_id = cursor.fetchone()
			print(".", thread_id)

			for lvl_1 in range(0, random.randint(1, 3)):
				cursor.execute(q, {
					"post_id": post_id,
					"content": first_reply,
					"parent_id": thread_id
				})
				first_reply_id = cursor.fetchone()
				print("\t.", first_reply_id)

				for lvl_2 in range(0, random.randint(1, 3)):
					cursor.execute(q, {
						"post_id": post_id,
						"content": second_reply,
						"parent_id": first_reply_id
					})
					second_reply_id = cursor.fetchone()
					print("\t\t.", second_reply_id)

					for lvl_3 in range(0, random.randint(1, 3)):
						cursor.execute(q, {
							"post_id": post_id,
							"content": third_reply,
							"parent_id": second_reply_id
						})
						third_reply_id = cursor.fetchone()
						print("\t\t\t.", third_reply_id)

					for lvl_4 in range(0, random.randint(1, 3)):
						cursor.execute(q, {
							"post_id": post_id,
							"content": fourth_reply,
							"parent_id": third_reply_id
						})
						fourth_reply_id = cursor.fetchone()
						print("\t\t\t.", fourth_reply_id)

					for lvl_5 in range(0, random.randint(1, 3)):
						cursor.execute(q, {
							"post_id": post_id,
							"content": fifth_reply,
							"parent_id": fourth_reply_id
						})
						fifth_reply_id = cursor.fetchone()
						print("\t\t\t.", fifth_reply_id)
