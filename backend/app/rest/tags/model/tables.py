from app import db

tags = db.inspect_table("tags", schema="storage")
