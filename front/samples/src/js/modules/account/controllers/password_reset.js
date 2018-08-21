define([
	"./base",
	"../views/password_reset"
], function(BaseController, View) {
	var Ctrl = BaseController.extend({
		initialize: function(args) {
			this.api.page.setLayout("layout-right");
			var $mainView = $("#main-content .layout-active .main-view");
			var view = new View({
				el: $mainView
			});

			view.render();
		}
	});

	return Ctrl;
});
