define([
	"core/controller",
	"../views/tags",
	"../models/tags"
], function(Controller, TagsView, TagsModel) {
	var Tags = Controller.extend({
		initialize: function(args) {
			this.api.page.setLayout("layout-right");
			var model = new TagsModel();
			var view = new TagsView({
				el: "#main-content .layout-active .main-view",
				collection: model
			});
			model.fetch();
		}
	});

	return Tags;
});
