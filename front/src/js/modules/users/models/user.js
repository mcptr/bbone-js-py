define(["backbone"], function(Backbone) {

	var User = Backbone.Model.extend({
		id: null,
		urlRoot: "/api/user/",

		initialize: function() {
		},

		validate: function(attrs, options) {
		},

		parse: function(response, options)	{
			return response;
		},
		isAuthenticated: function() {
			return this.id;
		}
	});

	return User;
});
