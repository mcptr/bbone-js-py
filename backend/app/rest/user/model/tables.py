from app import db

users = db.inspect_table("users", schema="auth")
confirmations = db.inspect_table("user_confirmations", schema="auth")
