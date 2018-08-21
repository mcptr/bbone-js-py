DBUTIL		= ../db/bin
UWSGI_CONFIG	=  etc/uwsgi.ini

CELERY_QUEUES	= default,high-priority,low-priority,mail.high-priority,mail.low-priority


all:

initdb:
	$(DBUTIL)/initdb -sd -U portal -P portal -D portal -w . --sql-schema-in=db/schema -v

populatedb:
	$(DBUTIL)/populatedb -U portal -P portal -D portal -w db/data-py -a -v

run-production:
	uwsgi --ini  $(UWSGI_CONFIG) --py-autoreload 0 --env CONFIG_CLASS=config.ProductionConfig

run-devel:
	uwsgi --ini  $(UWSGI_CONFIG) --py-autoreload 1 --env CONFIG_CLASS=config.DevelopmentConfig

run-testing:
	uwsgi --ini  $(UWSGI_CONFIG) --py-autoreload 1 --env CONFIG_CLASS=config.TestingConfig

run:
	python manage.py -c config.DevelopmentConfig runserver -d

shell:
	python ./manage.py -c config.DevelopmentConfig shell

test:
	@nosetests -vs test/ --logging-format "%(levelname)s (%(name)s): %(message)s"

rabbit-devel:
	sudo rabbitmqctl add_user portal portal
	sudo rabbitmqctl add_vhost portal.local
	sudo rabbitmqctl set_permissions -p portal.local portal ".*" ".*" ".*"

celery-run:
	celery --app=app.celery worker --loglevel=info --no-color -Q $(CELERY_QUEUES)

celery-purge:
	celery --app=app.celery --no-color purge

flower:
	celery flower --port=5555 \
		--broker=amqp://portal:portal@localhost:5672/portal.local \
		--broker_api=http://admin:admin@localhost:15672/api/

.PHONY: test
