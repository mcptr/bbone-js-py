from psycopg2.pool import ThreadedConnectionPool


class ConnectionPool(object):
	def __init__(self):
		self._pools = {}

	def create(self, db, maxconn, *args, **kwargs):
		if db in self._pools:
			raise Exception("Pool already initialized for: " + db)
		self._pools[db] = ThreadedConnectionPool(
			1, maxconn, *args, **kwargs
		)

	def get_pool(self, db):
		if db not in self._pools:
			raise Exception("Pool not initialized for: " + db)
		return self._pools[db]
