import os
import logging
import sys
from .base import Config


class DevelopmentConfig(Config):
	DEBUG = True
	DEVELOPMENT = True
	DATABASE = {
		"main": {
			"dsn": "postgresql+psycopg2://portal:portal@localhost/portal",
			"options": dict(
				pool_size=25,
				max_overflow=5,
				pool_timeout=5,
				#echo=True,
			)
		}
	}

	LOGGING = {
		"werkzeug": {
			"level": logging.DEBUG,
			"handler": logging.StreamHandler(sys.stderr)
		}
	}

	MAIL_SERVER = os.environ["MAIL_SERVER"]
	MAIL_PORT = os.environ["MAIL_PORT"]
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_DEBUG = True
	MAIL_USERNAME = os.environ["MAIL_USERNAME"]
	MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
	MAIL_DEFAULT_SENDER = os.environ.get(
		"MAIL_DEFAULT_SENDER", os.environ["MAIL_USERNAME"]
	)
	MAIL_MAX_EMAILS = 1
	MAIL_SUPPRESS_SEND = False
	MAIL_ASCII_ATTACHMENTS = False
