from .development import DevelopmentConfig


class TestingConfig(DevelopmentConfig):
	TESTING = True
	DATABASE = {
		"main": {
			"dsn": "postgresql+psycopg2://portal-test:portal-test@localhost/portal_test",
			"options": dict(
				pool_size=5,
				max_overflow=0,
				pool_timeout=3,
				#echo=True,
			)
		}
	}
