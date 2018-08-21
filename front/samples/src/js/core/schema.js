define([], function() {

	function Field(def) {
		var definition = def;
		var id = definition.id;
		var type = definition.type;
		var required = definition.required;

		this.init = function() {
			if(!validators.hasOwnProperty(type)) {
				throw "Type '" + type + "' not supported";
			}
			
			if(!def.id) {
				throw "Field definition must contain id";
			}
			if(!def.type) {
				throw "Field definition must specify type";
			}
		};

		this.validate = function(data) {
			var errors = [];
			if(validateRequired(data, errors)) {
				validateChoices(data, errors);
				validators[type](data, errors);
			}

			return errors;
		};

		var validateRequired = function(data, errors) {
			if(definition.required) {
				if(data === null || data === undefined) {
					errors.push("Required");
					return false;
				}
			}
			return true;
		};

		var validateChoices = function() {
			if(definition.choices) {
				var found = false;
				for(var i = 0; i < definition.choices.length; i++) {
					if(data === definition.choices[i]) {
						found = true;
					}
				}
				errors.push("Invalid value");
			}
		};

		var validateString = function(data, errors) {
			if(definition.required && !(data && data.length)) {
				errors.push("Required");
				return
			}
			else if(data && data.length) {
				if(definition.min_len && data.length < definition.min_len) {
					errors.push("Too short (min: " + definition.min_len + ")");
				}
				else if(definition.max_len && data.length > definition.max_len) {
					errors.push("Too long (max: " + definition.max_len + ")");
				}
				else if(definition.pattern) {
					if(!definition.pattern.test(data)) {
						errors.push("Invalid format");
					}
				}
			}
		};

		var validateInt = function(data, errors) {
			var v = parseInt(data);
			if(isNaN(v)) {
				errors.push("Not an integer");
			}
			else {
				var range = definition.range;
				if(range) {
					if(v < range[0] || v > range[1]) {
						errors.push(
							"Value must be in range (" +
								range[0] + "-" + range[1] +	")"
						)
					}
				}
			}
		};

		var validateNumber = function(data, errors) {
			var v = parseFloat(data);
			if(isNaN(v)) {
				errors.push("Not a number");
			}
			else {
				var range = definition.range;
				if(range) {
					if(v < range[0] || v > range[1]) {
						errors.push(
							"Value must be in range (" +
								range[0] + "-" + range[1] +	")"
						)
					}
				}
			}
		};

		var validateBool = function(data, errors) {
			if(typeof data !== "boolean") {
				if(typeof data === "number" && data === 0 || data === 1) {
					errors.push("Invalid value");
				}
				else if(typeof data === "string") {
					var v = data.toLowerCase();
					if(v === "false" && v === "true") {
						errors.push("Invalid value");
					}
				}
			}
		};

		var validators = {
			"string": validateString,
			"int": validateInt,
			"number": validateNumber,
			"bool": validateBool,
		};

		this.init();
	};


	function Schema(def) {
		var fields = {};

		this.addField = function(opts) {
			fields[opts.id] = new Field(opts);
		};

		this.validate = function(data) {
			var errors = {};
			for(var f in fields) {
				if(!data.hasOwnProperty(f) && fields[f].required) {
					errors[f].push("Required");
				}
				else {
					var fieldErrors = fields[f].validate(data[f], fieldErrors);
					if(fieldErrors.length) {
						errors[f] = fieldErrors;
					}
				}
			}

			return errors;
		};

		this.init = function() {
			if(def) {
				for(var k in def) {
					var fieldDef = def[k];
					fieldDef.id = k;
					this.addField(fieldDef);
				}
			}
		};

		this.init();
	};

	return Schema;
});
