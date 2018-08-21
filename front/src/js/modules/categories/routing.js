define([
	"./controllers/categories",
], function(Categories) {
	function setUp(dispatcher, options) {
		return {
			namespace: "categories",
			routes: {
				"(/)" : "index",
				":id(/)*rest" : "category"
			},
			index: function() {
				console.log("CATEGORIES INDEX");
				dispatcher(Categories, arguments);
			},
			category: function() {
				//dispatcher(Category, arguments);
			}
		};
	}

	return setUp;
});
