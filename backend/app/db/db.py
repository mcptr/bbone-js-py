import logging
from sqlalchemy import create_engine, MetaData, Table


logger = logging.getLogger("db")

__DBS = {}
meta = MetaData()


def initialize(app):
	global __DBS
	cfg = app.config.get("DATABASE")
	for alias in cfg:
		__DBS[alias] = create_engine(
			cfg[alias]["dsn"],
			**cfg[alias].get("options", {})
		)
		__DBS[alias].connect()
	d = __DBS["main"]


def session(name="main", **kwargs):
	return __DBS[name].connect()


def transaction(name="main", **kwargs):
	return __DBS[name].begin()


def inspect_table(name, *args, **kwargs):
	logger.info("Inspecting table {}.{}".format(
		kwargs.get("schema", ""),
		name,
	))
	dbname = kwargs.pop("database", "main")
	kwargs["autoload"] = True
	kwargs["autoload_with"] = session(dbname)
	return Table(name, meta, *args, **kwargs)
