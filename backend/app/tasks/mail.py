from datetime import datetime
from celery import current_app
from flask_mail import Message
from sqlalchemy import exc

from app import db
from app.modules.email import tables

celery = current_app


@celery.task(bind=True, default_retry_delay=5)
def send_mail(self, message_id):
	mailq = []
	with db.transaction("main") as tx:
		st = tables.mail_queue.select()
		st = st.where(
			tables.mail_queue.c.message_id == message_id
		)
		mailq = tx.execute(st).fetchall()
	if mailq:
		with current_app.app.mail.connect() as mx:
			for item in mailq:
				msg = None
				with db.transaction("main") as mtx:
					msg = Message(
						item.title,
						recipients=[item.ident]
					)
					msg.body = (item.body_text or "")
					if item.body_html:
						msg.html = item.body_html

				if not msg:
					continue

				try:
					mx.send(msg)
				except Exception as e:
					with db.transaction("main") as mtx:
						st = tables.queue.update().values(
							delivery_failures=(tables.queue.c.delivery_failures + 1),
							delivery_time=datetime.now()
						)
						st = st.where(tables.queue.c.id == item.id)
						mtx.execute(st)
						mtx.connection.commit()
						raise self.retry(exc=e)

				with db.transaction("main") as mtx:
					st = tables.queue.update().values(
						sent=True,
						success=True,
						delivery_time=datetime.now()
					)
					st = st.where(tables.queue.c.id == item.id)
					mtx.execute(st)
		return True
