from app.models.base import Model


class Geo(Model):
	def __init__(self):
		Model.__init__(self, "ejobs", "geo")

	def fetch(self, tp, **kwargs):
		return self.call_safe(tp, kwargs, verbose=True)

	def get_countries(self, pattern=None):
		return self.fetch("countries", pattern=pattern)

	def get_cities(self, pattern=None, country=None):
		return self.fetch("cities", pattern=pattern, country=country)

	def get_locations(self, pattern=None):
		return self.fetch("locations", pattern=pattern)
