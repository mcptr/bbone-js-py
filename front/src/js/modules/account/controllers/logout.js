define([
	"core/controller",
], function(Controller) {
	var Ctrl = Controller.extend({
		initialize: function(args) {
			var self = this;
			this.api.page.setLayout("layout-left");
			this.api.session.destroy({
				wait: true,
				success: function(model, response) {
					self.api.event.trigger("navigateRoute", "index");
				},
				error: function(model, response) {
					console.error("UNABLE TO LOG OUT", response);
				}
			});
		}
	});

	return Ctrl;
});
