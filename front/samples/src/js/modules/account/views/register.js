define(
	[
		"backbone",
		"core/form",
		"modules/users/models/user",
		"modules/users/schema/user",
		"templates/account/register"
	],
	function(Backbone, Form, User, UserSchema, Template) {
		var View = Backbone.View.extend({
			template: Template,
			id: "",
			className: "",
			events: {
				"click #fb-login-button": "fbLogin",
				"submit form[name='registration-form']": "submit"
			},
			viewComponents: [],
			initialize: function(data) {
				this.schema = UserSchema();
				this.form = new Form({
					schema: this.schema
				});
			},
			render: function() {
				this.appendTemplate(this.form, {empty: true});
				this.$formNode = this.$el.find("form[name='registration-form']");
			},
			submit: function(e) {
				var self = this;
				e.preventDefault();
				this.form.setData(this.$formNode.serializeObject());
				var valid = this.form.validate();
				if(valid) {
					this.trigger("createUser", this.form);
				}
				else {
					this.render(this.form);
				}
			},
			fbLogin: function(e) {
				e.preventDefault();
				this.trigger("socialUser", this.form);
			}
		});

		return View;
	}
);
