define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div class="verification success '+encodeHTML(it.data.className)+'"> <div class="message">'+encodeHTML(it.data.message || "Verification successful")+'</div> <div class="details">'+encodeHTML(it.data.details)+'</div></div>';return out;
}
return anonymous;
});
