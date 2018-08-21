define(["backbone", "templates/tags/tags"], function(Backbone, Template) {
	var Tags = Backbone.View.extend({
		template: Template,

		tagName: "div",

		id: "",

		className: "",

		events: {},

		initialize: function(data) {
			this.listenTo(this.collection, "change reset", function() {
				this.render(this.collection.toJSON());
			});
		},

		render: function(data) {
			data = (data || {});
			this.$el.empty();
			return this.appendTemplate(data);
		}

	});

	return Tags;
});
