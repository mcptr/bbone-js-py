define(["core/schema"], function(Schema) {

	var schema = new Schema({
		ident: {
			type: "string",
			required: true,
			min_len: 3,
			max_len: 255
		},
		password: {
			type: "string",
			required: false,
			min_len: 6,
			max_len: 64
		},
		social_uid: {
			type: "string",
			min_len: 1,
			max_len: 64,
		},
		social_provider: {
			type: "string",
			min_len: 1,
			max_len: 32,
		},
		social_access_token: {
			type: "string",
			min_len: 1,
			max_len: 512,
		}
	});

	return function() {
		return schema;
	};
});
