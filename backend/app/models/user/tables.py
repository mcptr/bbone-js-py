from app import db

users = db.inspect_table("users", schema="auth")
authenticated_users = db.inspect_table("authenticated_users", schema="views")
