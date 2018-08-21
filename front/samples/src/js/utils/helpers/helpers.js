define(
	[
		"utils/helpers/url",
		"utils/helpers/datetime",
		"utils/helpers/markup"
	],
	function(UrlHelper, DateTime, Markup) {

		return {
			url: UrlHelper,
			datetime: DateTime,
			markup: Markup
		};

	});
