define([
	"core/controller",
], function(Controller) {

	var Ctrl = Controller.extend({
		initialize: function(args) {
			var self = this;
			this.api.page.setLayout("layout-right");
			console.log("Users initialize", args);
		}
	});

	return Ctrl;
});
