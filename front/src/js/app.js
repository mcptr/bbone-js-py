define([
	"jquery",
	"backbone",
	"init/setup",
	"core/logger",
	"core/api",
	"core/routing",
	"modules/error/views/error",
	"controllers/index",
	"modules/users/models/user",
	"modules/sidebar/controllers/sidebar"
], function($, Backbone, Setup, Logger, Api, Routing,
			ErrorView, IndexCtrl, UserModel, SidebarCtrl) {

	var App = {
		Models: {},
		Collections: {},
		Views: {},
		Routers: {},
		Controllers: {},
		api: new Api(),
		init: function () {
			var self = this;

			var defaultViewComponents = [
				"search", "tags", "topPosts"
			];

			var routing = new Routing(self.api);
			this.setup = new Setup(this.api);
			this.setup.init({
				defaultViewComponents: defaultViewComponents,
				routing: routing
			});

			var ls = this.api.localStorage;

			var sessionId = self.api.localStorage.session_id;
			//console.log("Local SessionID: ", sessionId);

			this.api.event.on("app/ready", function() {
				self.initUI();
				routing.init();
			});

			self.initSesssion(sessionId)

		},
		onSessionSync: function(response) {
			var self = this;
			$.ajaxSetup({
				headers: {
					"X-App-Session": response.id
				}
			});
			var uid = this.api.session.get("user_id");
			if(uid) {
				this.api.user.set({id: uid});
				this.api.user.fetch().always(function() {
				 	self.api.event.trigger("app/ready");
				});
			}
			else {
				self.api.event.trigger("app/ready");
			}
		},
		createSession: function() {
			var self = this;
			console.log("Creating new session");
			$.post(self.api.session.urlRoot).then(
				function(response) {
					self.api.localStorage.session_id = response.id;
					self.api.session.set(response);

					self.onSessionSync(response);
				},
				function(response) {
					console.error("Failed to initialize session.", response);
				}
			);
		},
		initSesssion: function(sessionId) {
			var self = this;
			console.log("Initializing session", sessionId, sessionId == null, typeof sessionId);
			if(sessionId && sessionId.length) {
				self.api.session.set({id: sessionId});
				self.api.session.fetch().then(
					function(response) { self.onSessionSync(response); },
					function(response) { self.createSession(); }
				);
			}
			else {
				self.createSession();
			}

		},
		start: function() {
		},
		initUI : function() {
			var indexCtrl = new IndexCtrl(this.api);
			var sidebarCtr = new SidebarCtrl(this.api);
		},
		onInitError : function(response) {
			var view = new ErrorView({
				el: $(document.body),
				className: "init-error",
			});
			view.render({
				replace: true,
				message: "Service currently unavailable",
				details: [
					"Please try again later."
				],
				errorId: "InitializationError: " + (new Date()).toUTCString(),
				traceback: (response.statusText + " (" + response.status + ")")
			});
		},
		logging: new Logger("APPLICATION")
	};

	return App;
});
