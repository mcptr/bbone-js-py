define([
	"jquery",
	"./base",
	"modules/social/social",
	"../views/login"
], function($, BaseController, Social, View) {
	var Login = BaseController.extend({
		viewComponents: [],
		initialize: function(args) {
			var self = this;
			this.api.page.setLayout("layout-right");
			this.social = new Social(this.api);

			if(this.api.user.get("id")) {
				this.api.event.trigger("navigateRoute", ":account:dashboard");
			}
			else {
				var $mainView = $("#main-content .layout-active .main-view");
				this.view = new View({el: $mainView});
				this.attachEvents();
				this.view.render();
			}
		},
		attachEvents: function() {
			var self = this;
			this.view.on("socialLogin", function(form) {
				self.social.fbLogin(function(data) {
					form.setData(data);
					self.createUser(form);
				});
			});
				
			this.view.on("login", function(form) {
				self.loginUser(form);
			});
		},
		detachEvents: function() {
			if(this.view) {
				this.view.off("login");
				this.view.off("socialLogin");
			}
		},
		createUser: function(form) {
			var self = this;
			if(!form.validate()) {
				this.onError({}, form);
			}
			else {
				this.api.user.save(
					form.getData(),
					{
						wait: true,
						success: function(model, response, opts) {
							self.onSuccess();
						},
						error: function(model, response, opts) {
							self.onError(response, form);
						}
					}
				);
			}
		},
		loginUser: function(form) {
			var self = this;
			if(!form.validate()) {
				this.onError({}, form);
			}
			else {
				$.post("/api/auth/", JSON.stringify(form.getData())).then(
					function(response) { self.onSuccess(response); },
					function() {
						form.setApiError("Login unsuccessful");
						self.view.render();
					}
				);
			}
		},
		onSuccess: function(response) {
			var self = this;
			this.api.session.set({id: response.session_id});
			this.api.session.fetch({
				success: function(model, response) {
					self.api.user.set({id: model.get("user_id")});
					self.api.user.fetch({
						success: function() {
							self.api.event.trigger(
								"navigateRoute",
								":account:dashboard"
							);
						}
					});
				}
			});
		},
	});

	return Login;
});
