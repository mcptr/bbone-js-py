import os
import logging
from flask import current_app, render_template
from flask_mail import Message

from app import db
from app.tasks.mail import send_mail

from . import tables


def enqueue(subject, rcpt, template, **kwargs):
	txt_tpl = os.path.join("mail", template) + ".txt"
	html_tpl = os.path.join("mail", template) + ".html"
	txt = render(txt_tpl, **kwargs)
	html = render(html_tpl, **kwargs)

	sender = kwargs.get("sender", current_app.config["MAIL_DEFAULT_SENDER"])
	rcpt = rcpt if isinstance(rcpt, list) else [rcpt]

	with db.transaction() as tx:
		st = tables.messages.insert().returning(tables.messages.c.id)
		st = st.values(title=subject, body_text=txt, body_html=html)
		r = tx.execute(st)
		mail_id = r.fetchone()[0]
		st = tables.queue.insert()
		r = tx.execute(st, [
			dict(
				message_id=mail_id,
				sender=sender,
				recipient_id=rcpt_id,
			) for rcpt_id in rcpt
		])

		r = send_mail.apply_async(
			(mail_id, ),
			queue="mail.low-priority",
			max_retries=3,
		)


def render(template, **kwargs):
	content = None
	try:
		content = render_template(template, **kwargs)
		print("CONTENT ############", content)
	except Exception as e:
		logging.getLogger(__name__).exception(e)
	return content
