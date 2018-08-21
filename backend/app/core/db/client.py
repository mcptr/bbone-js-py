from psycopg2.extras import RealDictCursor, NamedTupleCursor


class DBClient(object):
	def __init__(self, pool, **kwargs):
		self._pool = pool
		self._conn = None

	def __enter__(self):
		self._conn = self._pool.getconn()
		return self._conn

	def __exit__(self, etype, e, tb):
		self._pool.putconn(self._conn)


class DBCursor(object):
	def __init__(self, pool, **kwargs):
		self._pool = pool
		self._conn = None
		self._kwargs = kwargs
		cursor_type = kwargs.get("cursor_type", tuple)
		if cursor_type == dict:
			self._cursor_factory = RealDictCursor
		else:  # cursor_type == tuple:
			self._cursor_factory = NamedTupleCursor

	def __enter__(self):
		self._conn = self._pool.getconn()
		return self._conn.cursor(cursor_factory=self._cursor_factory)

	def __exit__(self, etype, e, tb):
		if not e and self._kwargs.get("autocommit", False):
			self._conn.commit()
		else:
			self._conn.rollback()
		self._pool.putconn(self._conn)


class DBConnection(object):
	def __init__(self, pool, **kwargs):
		self._pool = pool
		self._conn = None

	def cursor(self, cursor_type=tuple):
		if cursor_type == dict:
			cursor_type = RealDictCursor
		else:
			cursor_type = NamedTupleCursor
		return self._conn.cursor(cursor_factory=cursor_type)

	def commit(self):
		self._conn.commit()

	def rollback(self):
		self._conn.rollback()

	def __enter__(self):
		self._conn = self._pool.getconn()
		return self

	def __exit__(self, etype, e, tb):
		self._pool.putconn(self._conn)
