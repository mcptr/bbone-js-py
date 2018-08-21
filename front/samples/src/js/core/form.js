define([], function() {

	function Form(options) {
		var data = (options.data || {});
		var errors = (options.errors || {});
		var schema = options.schema;

		this.reset = function() {
			this.resetData();
			this.resetErrors();
		};

		this.resetData = function() {
			data = {};
		};

		this.resetErrors = function() {
			errors = {};
		};

		this.getData = function(k) {
			return data;
		};

		this.getValue = function(k) {
			return data[k];
		};

		this.setValue = function(k, v) {
			data[k] = v;
		};

		this.setData = function(o) {
			data = o;
		};

		this.getErrors = function(k) {
			return k ? errors[k] : errors ;
		};

		this.setError = function(k, v) {
			if(!errors.hasOwnProperty(k)) {
				errors[k] = [];
			}
			errors[k].push(v);
		};

		this.setErrors = function(o) {
			errors = o;
		};

		this.hasErrors = function(k) {
			if(k) {
				return errors[k] && errors[k].length;
			}
			else {
				for(k in errors) {
					if(errors[k] && errors[k].length) {
						return true;
					}
				}
				return false;
			}
		};

		this.setApiError = function(msg) {
			this.apiError = msg;
		};

		this.getApiError = function() {
			return this.apiError;
		};

		this.validate = function(o) {
			if(!schema) {
				throw "No Schema defined for form";
			}

			errors = schema.validate((o || data));
			return !this.hasErrors();
		};
	}

	return Form;

});
