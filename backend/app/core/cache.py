import time


class CacheEntry(object):
	def __init__(self, data, **kwargs):
		self._data = data
		self._ctime = time.time()
		self._max_age = kwargs.pop("max_age", )

	def is_expired(self):
		if self._max_age:
			return time.time() - self._ctime <= self._max_age
		return False

	def data(self):
		return self._data


class Cache(object):
	def __init__(self, **kwargs):
		self._default_max_age = kwargs.pop("default_max_age", 0)
		self._values = {}

	def set(self, k, data, **kwargs):
		kwargs["max_age"] = kwargs.get("max_age", self._default_max_age)
		self._values[k] = CacheEntry(data, **kwargs)

	def get(self, k, default=None):
		if k in self._values:
			return self._values.get(k).data()
		return default
