define(["core/schema"], function(Schema) {

	var schema = new Schema({
		username: {
			type: "string",
			required: false,
			min_len: 3,
			max_len: 64
		},
		gender: {
			type: "string",
			required: false
		},
		city: {
			type: "string",
			required: false
		},
		country: {
			type: "string",
			required: false
		},
		date_of_birth: {
			type: "string",
			required: false
		},
		about: {
			type: "string",
			required: false,
			max_len: 1024
		}

	});

	return function() {
		return schema;
	};
});
