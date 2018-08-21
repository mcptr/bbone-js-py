define(
	[
		"backbone",
		"templates/account/password_reset"
	],
	function(Backbone, Template) {
		var View = Backbone.View.extend({
			api: null,
			template: Template,
			id: "",
			className: "",
			events: {
			},
			viewComponents: [],
			initialize: function(data) {
			},

			render: function(data) {
				this.$el.empty();
				this.appendTemplate(data);
			},
		});

		return View;
	}
);
