define([
	"core/controller",
	"../views/menu/main"
], function(Controller, MenuView) {

	var BaseController = Controller.extend({
		initialize: function() {
			this.api.page.setLayout("layout-sidebar");
			if(!this.api.user.get("id")) {
				this.api.event.trigger("navigateRoute", ":account:login");
			}

			var $menuEl = $("#main-content .layout-active .sidebar .content");
			var menuView = new MenuView({
				el: $menuEl
			});

			menuView.render();

		},
		getViewComponents: function() {
			if(this.api.user.isAuthenticated()) {
				return [];
			}
			return [];
		}
	});

	return BaseController;
});
