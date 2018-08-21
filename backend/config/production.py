from .base import Config


class ProductionConfig(Config):
	DEBUG = False
	SESSION_COOKIE_SECURE = True

	MAIL_SERVER = "localhost"
	MAIL_PORT = 25
	MAIL_USE_TLS = False
	MAIL_USE_SSL = False
	MAIL_DEBUG = False
	MAIL_USERNAME = ""
	MAIL_PASSWORD = ""
	MAIL_DEFAULT_SENDER = ""
	MAIL_MAX_EMAILS = 1
	MAIL_SUPPRESS_SEND = False
	MAIL_ASCII_ATTACHMENTS = False
