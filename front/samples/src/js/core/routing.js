define([
	"jquery",
	"backbone",
	"routes/main",
], function($, Backbone, Main) {

	function Routing(api) {
		var router;

		this.init = function(errorHandler) {
			router = new Main(api);
			this.setListeners();
			Backbone.history.start({pushState: true});
		};

		this.setListeners = function() {
			var self = this;
			api.event.on("navigateHash", function(hash) {
				Backbone.history.location.hash = hash;
			});

			api.event.on("navigateRoute", function(route, params) {
				var url = self.getUrlFor(route, params);
				if(url) {
					Backbone.history.navigate(url, true);
				}
			});

			api.event.on("navigateUrl", function(url) {
				Backbone.history.navigate(url);
			});
		};

		this.getUrlFor = function(name, params) {
			params = (params || {});

			var resultUrl = "/";
			var route = null;
			if(name.charAt(0) == ":") {
				var ns = Backbone.history.getFragment();
				var nestedRouteName = (ns.length ? ns + name : name.substr(1));
				route = router.routeMap[nestedRouteName];
				route = (route || router.routeMap[name.substr(1)]);
			}

			route = (route || router.routeMap[name]);

			if(route) {
				for(var p in params) {
					route = route.replace(':' + p, params[p]);
				}
				route = route.replace(/(\(\/\))?(\*\w+)?$/, "");
				resultUrl = "/" + route;
				if(params["_hash"]) {
					resultUrl += "#" + params["_hash"];
				}
			}
			else {
				console.error("getUrlFor(): route not found", name);
			}

			return resultUrl;
		};
	};

	return Routing;
});
