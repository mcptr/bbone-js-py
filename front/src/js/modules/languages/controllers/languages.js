define([
	"core/controller",
], function(Controller) {

	var LanguagesController = Controller.extend({
		initialize: function(args) {
			var self = this;
			console.log("Languages initialize", args);
		}
	});

	return LanguagesController;
});
