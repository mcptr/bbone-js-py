# from nix.core.client import NixClient
# from nix.core.response import Response
# from nix.core.request import Request
# from nix.schema import manager
# from nix.lib.yami import YAMIError
import logging
import time


class Model(object):
	def __init__(self, module, endpoint=None, **kwargs):
		pass


# class NixModel(object):
# 	_api_key = None
# 	_default_timeout = 3000

# 	def __init__(self, module, endpoint=None, **kwargs):
# 		self._module = module
# 		self._endpoint = endpoint
# 		self._backend = kwargs.pop("backend", "core")
# 		logger_name = "::".join(["Model", self._module])
# 		if endpoint:
# 			logger_name = "::".join([logger_name, endpoint])
# 		self._logger = logging.getLogger(logger_name)

# 	def set_api_key(self, key):
# 		self._api_key = key

# 	def call(self, route, data=None, **kwargs):
# 		data = (data or {})
# 		return self._call_backend(route, data, **kwargs)

# 	def call_safe(self, route, data=None, **kwargs):
# 		data = (data or {})
# 		response = None
# 		try:
# 			response = self._call_backend(route, data, **kwargs)
# 		except Exception as e:
# 			self._logger.error(str(e))
# 			schema = None
# 			default_value = None
# 			if "default_schema" in kwargs or "default" in kwargs:
# 				schema = manager.load(kwargs.get("default_schema", None))
# 				if schema:
# 					default_value = schema.data()
# 				else:
# 					default_value = kwargs.get("default", None)
# 				response = Response(default=default_value)
# 				response.set_error(str(e))
# 		return response

# 	def _call_backend(self, route, req, **kwargs):
# 		self._logger.debug(
# 			"%s %s::%s",
# 			self._backend, self._module, route)
# 		response = None
# 		if self._endpoint:
# 			route = "/".join([self._endpoint, route])
# 		data = req.data if isinstance(req, Request) else req
# 		client_params = dict(
# 			timeout=kwargs.get("timeout", self._default_timeout)
# 		)
# 		kwargs["api_key"] = kwargs.get("api_key", self._api_key)
# 		try:
# 			with NixClient(self._backend, **client_params) as c:
# 				response = c.call(self._module, route, data, **kwargs)
# 		except YAMIError as e:
# 			error = "Communication error: " + str(e)
# 			self._logger.error(error)
# 			response = Response()
# 			response.set_error(error)
# 		return response
