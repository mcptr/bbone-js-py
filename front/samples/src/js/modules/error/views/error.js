define(["backbone", "templates/error/error"], function(Backbone, Template) {
	var Error = Backbone.View.extend({
		api: null,
		template: Template,
		className: "",
		events: {},
		replace: false,
		initialize: function(data) {
			this.replace = (data.replace || this.replace);
		},

		render: function(data) {
			data = (data || {});
			data.className = (data.className || this.className);
			if(data.replace) {
				this.$el.empty();
			}
			if(data.details && !(data.details instanceof Array)) {
				data.details = [ data.details ];
			}

			if(data.hints && !(data.hints instanceof Array)) {
				data.hints = [ data.hints ];
			}
			return this.prependTemplate(data);
		}

	});

	return Error;
});
