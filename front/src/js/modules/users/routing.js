define([
	"./controllers/users",
], function(Users) {
	function setUp(dispatcher, options) {
		return {
			namespace: "users",
			routes: {
				"" : "index",
				":id(/)" : "user",
			},
			index: function() {
				dispatcher(Users, arguments);
			},
			user: function() {
				dispatcher(Users, arguments);
			},
		};
	}

	return setUp;
});
