from app import db

queue = db.inspect_table("queue", schema="mail")
messages = db.inspect_table("messages", schema="mail")
mail_queue = db.inspect_table("mail_queue", schema="views")
