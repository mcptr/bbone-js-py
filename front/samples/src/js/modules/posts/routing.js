define([
	"./controllers/posts",
	"./controllers/post"
], function(Posts, Post) {
	function setUp(dispatcher, options) {
		return {
			namespace: "posts",
			routes: {
				"(/)" : "index",
				":id(/)" : "post"
			},
			index: function() {
				dispatcher(Posts, arguments);
			},
			post: function() {
				dispatcher(Post, arguments);
			}
		};
	}

	return setUp;
});
