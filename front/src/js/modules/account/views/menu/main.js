define(
	[
		"backbone",
		"templates/account/menu/main"
	],
	function(Backbone, Template) {
		var Login = Backbone.View.extend({
			template: Template,
			events: {},
			initialize: function(data) {
			},

			render: function(data) {
				this.appendTemplate(data, {empty: true});
			},
		});

		return Login;
	}
);
