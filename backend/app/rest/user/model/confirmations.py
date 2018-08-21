import uuid
from datetime import datetime
from app import db

from . tables import confirmations, users


class ConfirmationsModel(object):
	def create(self, user, action_type, max_age=None):
		confirmation_key = str(uuid.uuid4())
		values = dict(
			confirmation_key=confirmation_key,
			user_id=user.id,
			action_type=action_type,
		)
		if max_age:
			values["max_age"] = max_age

		st = confirmations.insert().values(**values)
		with db.transaction() as tx:
			tx.execute(st)
			return confirmation_key

	def confirm(self, user, action_type, key):
		handlers_map = {
			"registration": self._confirm_user_registation
		}
		handler = handlers_map[action_type.lower()]
		success = False
		if handler:
			success = handler(user, action_type, key)
		else:
			q = "SELECT * from auth.verify_confirmation(%s, %s, %s)"
			with db.transaction("main") as tx:
				rs = tx.execute(q, (user.id, action_type, key))
				success = rs.fetchone()[0]
		return success

	def _confirm_user_registation(self, user, action_type, key):
		q = "SELECT * from auth.confirm_user_registration(%s, %s, %s)"
		with db.transaction("main") as tx:
			rs = tx.execute(q, (user.id, action_type, key))
			return rs.fetchone()[0]
