define([
	"underscore",
	"jquery",
	"backbone",
	"core/logger",
	"core/page",
	"core/service/cache",
	"core/service/session",
	"modules/session/models/session",
	"modules/users/models/user",
	"utils/helpers/helpers"
], function(_, $, Backbone, Logger, Page, CacheService, SessionService, SessionModel, UserModel, Helpers) {
	var Api = function() {
		var event = _.extend({}, Backbone.Events);
		var debug = function(msg, data) {
			event.trigger("debug", {
				message: msg,
				data: data
			});
		};

		var modules = {
			session: new SessionModel(),
			user: new UserModel(),
			localStorage: window.localStorage,
			sessionStorage: window.sessionStorage,
			event: event,
			helpers: Helpers,
			cacheService: new CacheService()
		};

		modules.logging = new Logger("MAIN", modules);
		modules.page = new Page(modules);

		event.listenTo(modules.session, "sync change reset", function(data) {
			var id = data.get("id");
			$.ajaxSetup({
				headers: {
					"X-App-Session": id
				}
			});
		});

		event.listenTo(modules.session, "destroy", function() {
			modules.localStorage.clear();
			window.location.href = "/";
		});

		window.user = modules.user;
		event.listenTo(modules.user, "change:id", function(data) {
			modules.session.set({user_id: data.get("id")});
		});

		return modules;
	};

	return Api;
});
