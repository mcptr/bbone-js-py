define(
	[],
	function() {

		function Session() {
		};

		var instance = Session();
		
		return function() {
			return instance;
		};
	}
);
