define([
	"underscore",
	"core/controller",
	"../models/post",
	"../views/post_form"
], function(_, Controller, PostModel, NewPostView) {

	var NewPost = Controller.extend({
		viewComponents: [],
		initialize: function(id) {
			var self = this;
			this.api.page.setLayout("layout-right");

			this.postModel = new PostModel();
			var $mainView = $("#main-content .layout-active .main-view");

			this.view = new NewPostView({
				el: $mainView,
				model: this.postModel,
			});

			this.view.render();
		},
	});

	return NewPost;
});
