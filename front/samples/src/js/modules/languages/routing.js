define([
	"./controllers/languages",
], function(Languages) {
	function setUp(dispatcher, options) {
		return {
			namespace: "languages",
			routes: {
				"" : "index",
				":id(/)" : "language",
			},
			index: function() {
				dispatcher(Languages, arguments);
			},
			language: function() {
				dispatcher(Languages, arguments);
			},
		};
	}

	return setUp;
});
