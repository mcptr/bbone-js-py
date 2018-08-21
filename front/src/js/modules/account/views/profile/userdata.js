define(
	[
		"backbone",
		"core/form",
		"../../schema/profile/userdata",
		"templates/account/profile/userdata"
	],
	function(Backbone, Form, UserSchema, Template) {
		var View = Backbone.View.extend({
			template: Template,
			events: {},
			initialize: function(data) {
				this.schema = UserSchema();
				this.form = new Form({
					schema: this.schema
				});
				this.form.setData(this.getAPI().user.toJSON());
				console.log(this.form.getData());
			},
			render: function(data) {
				this.$el.empty();
				this.appendTemplate(this.form);
			}
		});

		return View;
	}
);
