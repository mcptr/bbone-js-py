define(
	[
		"../base",
		"../../views/profile/userdata"
	],
	function(BaseController, View) {

		var Ctrl = BaseController.extend({
			initialize: function(args) {
				BaseController.prototype.initialize.apply(this, args);
				console.log($("#main-content .layout-active .main-view"));
				this.view = new View({
					el: $("#main-content .layout-active .main-view")
				});
				this.view.render();
			}
		});

		return Ctrl;
	}
);
