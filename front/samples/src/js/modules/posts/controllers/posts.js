define([
	"core/controller",
	"../models/posts",
	"../views/posts"
], function(Controller, PostsCollection, PostsView) {

	var PostsController = Controller.extend({
		initialize: function(args) {
			var self = this;
			this.api.page.setLayout("layout-right");

			this.collection = new PostsCollection(args);
			var $mainView = $("#main-content .layout-active .main-view");
			this.view = new PostsView({
				el: $mainView,
				collection: this.collection
			});

			self.view.setLoadingIndicator();

			this.collection.fetch({reset: true}).then(
				function() {},
				function(response) {
					self.view.renderError(response.status, {
						message: "No posts found"
					});
				}
			).always(function() {
				self.view.removeLoadingIndicator();
			});
		}
	});

	return PostsController;
});
