define([
	"jquery",
	"underscore",
	"core/controller",
	"modules/search/views/search",
	"modules/posts/models/posts",
	"modules/posts/views/top_posts",
	"modules/tags/models/tags",
	"modules/tags/views/tags"
], function($, _, Controller, Search, PostsModel, TopPosts, TagsModel, TagsView) {
	var SidePanel = Controller.extend({
		views: {},
		initialize: function(args) {
			this.config = [];
			this.componentHandlers = {
				"search": _.bind(this.initializeSearch, this),
				"tags": _.bind(this.initializeTags, this),
				"topPosts": _.bind(this.initializeTopPosts, this)
			};

			this.attachEvents();
		},
		attachEvents: function() {
			this.api.event.on("view/components", _.bind(this.onViewComponents, this));
		},
		detachEvents: function() {
			this.api.event.off("view/components", _.bind(this.onViewComponents, this));
		},
		onViewComponents: function(config) {
			var self = this;
			var $panel = $("#main-content .layout-active .side-panel");
			config = (config || []);

			var isChanged = config.length != this.config.length;
			if(!isChanged) {
				for(var i = 0; !isChanged && (i < config.length); i++) {
					if(this.config[i] !== config[i]) {
						isChanged = true;
					}
				}
			} 

			if(isChanged) {
				$panel.empty();
				config.forEach(function(el, idx) {
					var f;
					var className;
					if(el instanceof Function) {
						f = el;
						className = "component-" + idx;
					}
					else {
						f =  self.componentHandlers[el];
						className = el;
					}
					var $itemHolder = $("<div></div>");
					$itemHolder.addClass("item").addClass(className);
					if(f) {
						f($itemHolder);
					}
					else {
						console.error("Unresolved component: ", el); 
					}
					$panel.append($itemHolder);
				});
				this.config = config;
			}
		},

		initializeSearch: function($node) {
			var view = new Search({
				el: $node
			});
			var data = {
				search: ""
			};
			view.render(data);
		},

		initializeTopPosts: function($node) {
			var postsModel = new PostsModel();

			var view = new TopPosts({
				el: $node,
				collection: postsModel
			});

			postsModel.fetch({
				reset: true,
				data: $.param({
					limit: 10,
					order_by: "user_score",
					ctime_offset: 3600 * 24 * 7
				})
			});
		},

		initializeTags: function($node) {
			var tagsModel = new TagsModel();
			var view = new TagsView({
				el: $node,
				collection: tagsModel
			});

			tagsModel.fetch({
				reset: true,
				data: $.param({
					limit: 10
				})
			});
		}
	});

	return SidePanel;
});
