define([
	"./controllers/tags",
], function(Tags) {
	function setUp(dispatcher, options) {
		return {
			namespace: "tags",
			routes: {
				"(/)" : "index",
				":id(/)" : "tag"
			},
			index: function() {
				dispatcher(Tags, arguments);
			},
			tag: function() {
				dispatcher(Tags, arguments);
			}
		};
	}

	return setUp;
});
