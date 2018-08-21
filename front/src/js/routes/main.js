define([
	"underscore",
	"backbone",
	"controllers/index",
	"modules/categories/controllers/categories",
	"modules/posts/controllers/posts",
	"modules/posts/controllers/post",
	"modules/posts/controllers/new_post",
	"modules/verification/controllers/verification",
	"modules/users/routing",
	"modules/account/routing",
	"modules/posts/routing",
	"modules/categories/routing",
	"modules/tags/routing",
	"modules/languages/routing",
], function(
	_, Backbone,
	IndexCtrl, CategoriesCtrl,
	PostsCtrl, PostCtrl, NewPostCtrl, VerificationCtrl,
	UsersRouting, AccountRouting, PostsRouting, CategoriesRouting,
	TagsRouting, LanguagesRouting) {

	var errorHandler = function() {
		Backbone.history.navigate("/", {replace: true, trigger: true});
	};

	var Main = Backbone.Router.extend({
		postDetailsHandler: function() {
			this.dispatch(PostCtrl, arguments);
		},
		index: function() {
			this.dispatch(PostsCtrl, arguments);
		},
		rising: function() {
			this.dispatch(NewPostCtrl, arguments);
		},
		categories: function() {
			this.dispatch(CategoriesCtrl, arguments);
		},
		category: function() {
			this.dispatch(PostsCtrl, arguments);
		},
		newPostHandler: function() {
			this.dispatch(NewPostCtrl, arguments);
		},
		confirmation: function() {
			this.dispatch(VerificationCtrl, arguments);
		},
		name: "Main",
		routes: {
			"(/)" : "index",
			"search(/)" : "search",
			"confirmation/:type/:key(/)": "confirmation",
			"*error": errorHandler
		},
		appRoutes: {
			"users": {router: UsersRouting, ns: "users"},
			"account": {router: AccountRouting, ns: "account"},
			"posts": {router: PostsRouting, ns: "posts"},
			"fresh": {router: PostsRouting, ns: "fresh", multi: true},
			"categories": {router: CategoriesRouting, ns: "categories"},
			"tags": {router: TagsRouting, ns: "tags"},
			"languages": {router: LanguagesRouting, ns: "languages"},

		},
		apps: {},
		routeMap: {},
		mountApps: function(options) {
			var self = this;
			options = (options || {});
			var modulesRouting = {}
			 _.each(this.routes, function(name, route) {
				 if(!(name instanceof Function)) {
					 self.routeMap[name] = route;
				 }
			 });

			for(var mountPoint in this.appRoutes) {
				var appRouter = this.appRoutes[mountPoint].router(function() {
					self.dispatch.apply(self, arguments);
				}, options);

				this.apps[mountPoint] = appRouter;

				for(var pattern in (appRouter.routes || {})) {
					var mountRoute;
					if(pattern.length) {
						mountRoute = mountPoint + (
							(pattern.charAt(0) == "/") ? ""  : "/") + pattern;
					}
					else {
						mountRoute = mountPoint + "(/)";
					}

					if(appRouter.routes[pattern] instanceof Function) {
						this.route(mountRoute, appRouter.routes[pattern]);
					}
					else  {
						this.route(mountRoute, appRouter[appRouter.routes[pattern]]);
					}
					var ns;
					if(this.appRoutes[mountPoint].multi) {
						ns = this.appRoutes[mountPoint].ns + ":" + appRouter.namespace;
					}
					else {
						ns = (this.appRoutes[mountPoint].ns || appRouter.namespace);
					}

					var routeKey = ns + ":" + appRouter.routes[pattern];

					self.routeMap[routeKey] = mountRoute;
				}
			}

			//console.dir(self.routeMap);
		}
	});


	// making the router a singleton to control mountApps() - supporting
	// mounting the apps to specific urls and still having a
	// single router in the application

	var instance = null;
	var init = function(api) {
		if(!instance) {
			instance = new Main(api);
			instance.mountApps();
		}
		return instance;
	};

	return init;
});
