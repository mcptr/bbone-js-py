define([
	"./base",
	"modules/social/social",
	"../views/register",
], function(BaseController, Social, View) {
	var Register = BaseController.extend({
		viewComponents: [],
		initialize: function(args) {
			var self = this;
			this.api.page.setLayout("layout-right");

			this.social = new Social(this.api);

			if(this.api.user.get("id")) {
				this.api.event.trigger("navigateRoute", ":account:dashboard");
			}
			else {
				var $mainView = $("#main-content .layout-active  .main-view");
				this.view = new View({el: $mainView});

				this.attachEvents();
				this.view.render();
			}
		},
		attachEvents: function() {
			var self = this;
			this.view.on("socialUser", function(form) {
				self.social.fbLogin(function(data) {
					form.setData(data);
					self.createUser(form);
				});
			});
				
			this.view.on("createUser", function(form) {
				self.createUser(form);
			});
		},
		detachEvents: function() {
			if(this.view) {
				this.view.off("socialUser");
				this.view.off("createUser");
			}
		},
		onSuccess: function(response) {
			this.api.event.trigger("navigateRoute", ":account:dashboard");
		},
		onError: function(response, form) {
			var data = response.responseJSON;
			for(var field in data) {
				if(data[field]) {
					data[field].forEach(function(el) {
						form.setError(field, el);
					});
				}
			}

			this.view.render();
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
							self.onSuccess(response);
						},
						error: function(model, response, opts) {
							self.onError(response, form);
						}
					}
				);
			}
		}
	});

	return Register;
});
