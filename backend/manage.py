#!/usr/bin/env python

import os
from flask.ext.script import Manager
from app import App, WebApp


def create_app(config):
	instance = WebApp()
	instance.configure_app(config)
	app = instance.get_app()
	return app


def run_uwsgi():
	#import uwsgi
	return create_app(os.environ["CONFIG_CLASS"])


if __name__ == "__main__":
	manager = Manager(create_app)
	manager.add_option(
		"-c", "--config",
		dest="config",
		default=os.environ.get("CONFIG_CLASS"),
		required=False
	)

	manager.run()
