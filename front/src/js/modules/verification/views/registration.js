define(
	["backbone", "templates/verification/registration"],
	function(Backbone, Template) {

	var View = Backbone.View.extend({
		api: null,
		template: Template,
		className: "",
		events: {},
		replace: false,
		initialize: function(data) {
			this.replace = (data.replace || this.replace);
		},

		render: function(data) {
			this.appendTemplate(data);
		}

	});

	return View;
});
