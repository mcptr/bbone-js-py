define(
	[
		"backbone",
		"core/form",
		"../schema/login",
		"modules/social/social",
		"templates/account/login"
	],
	function(Backbone, Form, UserSchema, Social, Template) {
		var Login = Backbone.View.extend({
			api: null,
			template: Template,
			events: {
				"click #fb-login-button": "fbLogin",
				"submit form[name='login-form']": "submit"
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
				this.$formNode = this.$el.find(
					"form[name='login-form']"
				);
			},

			submit: function(e) {
				var self = this;
				e.preventDefault();
				this.form.setData(this.$formNode.serializeObject());
				var valid = this.form.validate();
				if(valid) {
					this.trigger("login", this.form);
				}
				else {
					this.render(this.form);
				}
			},

			fbLogin: function(e) {
				e.preventDefault();
				this.trigger("socialLogin", this.form);
			}
		});

		return Login;
	}
);
