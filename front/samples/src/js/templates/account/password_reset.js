define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div class="account-form"> <div class="row"> <div class="col-md-6"> <h4>Password recovery</h4> <form name="password-reset-form" class="password-reset-form" method="post"><hr/><div class="form-group"> <input type="text" name="email" id="email" tabindex="1" class="form-control" placeholder="Email"></div><div class="form-group"> <button tabindex="4" class="btn btn-primary">Continue</button></div> </form> <hr/> <a href="'+encodeHTML(it.helpers.route(':account:login'))+'">Go back to login page</a> </div> <div class="col-md-6 col-hidden-sm"> </div> </div></div>';return out;
}
return anonymous;
});
