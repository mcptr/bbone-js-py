define(["backbone"], function(Backbone) {
	var Link = Backbone.Model.extend({
		url: "/api/tags/",
		initialize: function(id) {
			this.id = id;
			if(id) {
				this.url += id + "/";
			}
		},

		parse: function(response, options)	{
			return response;
		}
	});

	return Link;
});
