define(
	["backbone", "templates/verification/generic"],
	function(Backbone, Template) {

	var View = Backbone.View.extend({
		api: null,
		template: Template,
		className: "",
		events: {},
		replace: false,
		initialize: function(data) {
		},

		render: function(data) {
			this.appendTemplate(data, {empty: true});
		}

	});

	return View;
});
