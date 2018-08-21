define([
	"core/controller",
	"utils/string",
	"modules/error/views/error",
	"../views/generic"
], function(Controller, StringUtil, ErrorView, View) {

	var Ctrl = Controller.extend({
		initialize: function(type, key) {
			var self = this;
			this.api.page.setLayout("layout-right");
			type = type.toLowerCase();

			var url = StringUtil.format("/api/confirmation/{type}/{key}", {
				type: type,
				key: key
			});

			$.ajax({
				url: url,
				method: "PUT",
				success: function(response) {
					var data = self.getSuccessData(type);
					data.className = "big";

					var view = new View({
						el: "#main-content .layout-active .main-view"
					});
					view.render(data);
				},
				error: function(response) {
					var details;
					var hints;
					if(response.status == 403) {
						details = ["You have to sign-in to complete this action"];
					}
					else {
						details = ["Verification failed due to invalid or expired URL/token"];
						hints = [
							"You may need to generate a new verification request. ",

							"NOTE: Generating a new verification " +
							"key for an action will invalidate all previously " +
							"generated requests for the same action."
						];
					}

					self.renderError({
						message: "Request failed",
						details: details,
						hints: hints,
						className: "big"
					});
				}
			});
		},
		renderError: function(data) {
			var errorView = new ErrorView({
				el: "#main-content .layout-active .main-view"
			});
			errorView.render(data);
		},
		getSuccessData: function(type) {
			message = "Verification successful";
			if(type == "registration") {
				details = "Your profile is verified";
			};
			return {
				message: message,
				details: details
			};
		}
	});

	return Ctrl;
});
