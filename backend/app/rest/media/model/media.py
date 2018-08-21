import os
import time
from flask import current_app
from app import db


class MediaModel(object):
	def fetch(self, media_id=None):
		q = "select * from media where id = %s"
		with db.session("main") as c:
			rs = c.execute(q, (media_id,))
			return rs.fetchone()

	def save(self, file_object, mime_type, **kwargs):
		media_root = current_app.config.get("MEDIA_ROOT")
		if not media_root:
			raise Exception("MEDIA_ROOT not configured.")
		letter = file_object.filename[0]
		destdir = os.path.join(media_root, mime_type, letter)
		if not os.path.isdir(destdir):
			os.makedirs(destdir)
		fname = "%s-%s" % (
			str(time.time()).replace(".", "-"),
			file_object.filename
		)
		fpath = os.path.join(mime_type, letter, fname)
		full_path = os.path.join(destdir, fname)
		file_object.save(full_path)
		file_size = os.stat(full_path).st_size
		params = (
			file_object.filename,
			kwargs.get("title", None),
			file_size,
			mime_type,
			media_root,
			fpath,
		)

		q = " ".join([
			"insert into storage.media",
			"(original_name, title, file_size, mime_type, media_root, path)",
			"values(%s) returning id, path" % ",".join(["%s"] * len(params))
		])
		with db.transaction("main") as tx:
			rs = tx.execute(q, params)
			return rs.fetchone()

	def delete(self, media_id):
		q = (
			"delete from storage.media where id =  %s " +
			"returning (media_root || path) as fs_path"
		)
		with db.transaction("main") as tx:
			rs = tx.execute(q, (media_id,))
			record = rs.fetchone()
			if record.fs_path:
				try:
					os.unlink(record.fs_path)
				except OSError as e:
					print("model::Media::delete", e)
