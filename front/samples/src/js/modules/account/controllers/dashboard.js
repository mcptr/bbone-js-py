define([
	"./base",
 	"../views/dashboard"
], function(BaseController, View) {
	var Ctrl = BaseController.extend({
		initialize: function(args) {
			BaseController.prototype.initialize.apply(this, args);

			var $mainEl = $("#main-content .layout-active .main-view");
			var mainView = new View({
				el: $mainEl
			});

			mainView.render();
		}
	});

	return Ctrl;
});
