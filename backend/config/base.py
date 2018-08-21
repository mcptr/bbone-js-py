import os


class Config(object):
	DEBUG = False
	TESTING = False
	DEVELOPMENT = False
	MAX_CONTENT_LENGTH = 1024 * 1024 * 2
	JSONIFY_PRETTYPRINT_REGULAR = True

	SESSION_HEADER = "X-App-Session"

	DATE_FORMAT = "%d-%m-%Y"
	MEDIA_ROOT = os.path.join(
		os.path.abspath(os.path.dirname(__file__)), "media"
	)
	MEDIA_URL = "/media"

	NIX_BACKENDS = dict(
		core=dict(
			address="",
			pool_size=5,
		)
	)

	LOGGING = {}

	RESTFUL_APPS = [
		"app.rest.status",
		"app.rest.auth",
		#"app.rest.geo",
		"app.rest.media",
		"app.rest.posts",
		"app.rest.session",
		"app.rest.tags",
		"app.rest.user",
	]

	DB_CONFIG = dict(
		session_max_age=(60 * 30),
		max_login_failures=10,
	)

	TEMPLATE_DIRS = [
		"app/templates",
	]

	SITE_NAME = "PORTAL"
	SITE_BASE_URL = "http://portal.local"

	MAIL_SERVER = os.environ.get("MAIL_SERVER")
	MAIL_PORT = os.environ.get("MAIL_PORT")
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_DEBUG = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	MAIL_DEFAULT_SENDER = ""
	MAIL_MAX_EMAILS = 1
	MAIL_SUPPRESS_SEND = False
	MAIL_ASCII_ATTACHMENTS = False

	BROKER_URL = "amqp://portal:portal@localhost:5672/portal.local"
	CELERYD_POOL = "celery.concurrency.threads.TaskPool"
	CELERY_RESULT_BACKEND = "db+postgresql://portal:portal@localhost/portal_tasks"
	CELERY_TASK_RESULT_EXPIRES = 3600
	CELERY_TASK_SERIALIZER = "json"
	CELERY_RESULT_SERIALIZER = "json"
	CELERY_ACCEPT_CONTENT = ["json"]
	#CELERYD_CONCURRENCY = 8
	CELERY_ROUTES = {
		"app.tasks.mail.send_mail": {"queue": "mail.low-priority"},
	}
	CELERY_IMPORTS = [
		"app.tasks.mail",
	]
