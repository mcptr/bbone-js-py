define([
	"core/controller",
	"backbone",
	"../views/navbar-top",
	"modules/categories/models/categories"
], function(Controller, Backbone, NavTopView, CategoriesModel) {
	var NavbarTop = Controller.extend({
		initialize: function(args) {
			var self = this;

			this.view = new NavTopView({
				el: "#navbar-top",
				model: this.api.user
			});

			this.listenTo(
				this.api.session,
				"sync change destroy reset",
				function(model, response, options) {
					self.view.render();
				}
			);

			Backbone.history.on("route", function() {
				self.handleRoute();
			});
		},
		handleRoute: function() {
			var fragment = Backbone.history.getFragment();
			this.view.render({});
			this.view.setActive(fragment);
		}
	});

	return NavbarTop;
});
