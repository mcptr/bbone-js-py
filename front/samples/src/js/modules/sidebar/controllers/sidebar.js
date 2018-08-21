define([
	"core/controller",
], function(Controller) {
	var Ctrl = Controller.extend({
		viewComponents: [],
		initialize: function() {
			var self = this;

			self.detachEvents();
			self.attachEvents();

			this.api.event.on("layout/changed", function(name) {
				self.detachEvents();
				self.attachEvents();
			});
		},
		detachEvents: function() {
			if(this.$sidebar) {
				this.$control.off("click");
			}
		},
		attachEvents: function() {
			var self = this;
			this.detachEvents();
			this.$sidebar = $("#main-content .layout-sidebar.layout-active");
			this.$control = this.$sidebar.find(".control");
			this.$control.click(function(e) {
				e.preventDefault();
				self.$sidebar.toggleClass("toggled");
			});

		}
	});

	return Ctrl;
});
