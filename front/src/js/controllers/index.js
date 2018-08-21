define([
	"core/controller",
	"modules/nav/controllers/navbar-top",
	"modules/panel/controllers/side_panel"
], function(Controller, NavbarTop, SidePanel) {
	var Index = Controller.extend({
		initialize: function(args) {
			this.api.page.setLayout("layout-right");
			var navbarTop = new NavbarTop(this.api);
			var rightView = new SidePanel(this.api);
		}
	});

	return Index;
});
