define(["backbone", "templates/search/search"], function(Backbone, Template) {
	var Search = Backbone.View.extend({
		api: null,
		template: Template,
		events: {},

		initialize: function (data) {
		},

		render: function () {
			this.$el.empty();
			return this.appendTemplate({});
		}

	});

	return Search;
});
