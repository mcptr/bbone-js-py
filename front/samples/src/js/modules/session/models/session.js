define(["backbone"], function(Backbone) {

	var Session = Backbone.Model.extend({
		id: null,
		urlRoot: '/api/session/',
		initialize: function() {
		},
		validate: function(attrs, options) {
		},

		parse: function(response, options)	{
			return response;
		}
	});

	return Session;
});
