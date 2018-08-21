import os
from app import FlaskCeleryApp
from multiprocessing.util import register_after_fork

flask_app = FlaskCeleryApp()
flask_app.configure_app(os.environ.get("CONFIG_CLASS"))
celery = flask_app.get_app().celery
flask_app.get_app().app_context().push()
