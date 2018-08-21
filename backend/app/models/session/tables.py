from app import db

sessions = db.inspect_table("sessions", schema="auth")
