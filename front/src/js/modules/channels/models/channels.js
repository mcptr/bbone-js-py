define(["backbone"], function(Backbone) {
	var Channels = Backbone.Model.extend({
		url: "/api/channels/",
		initialize: function() {
			this.api.page.setLayout("layout-right");
		},
	});

	return Channel;
});
