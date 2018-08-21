define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div clsas="account dashboard"> <div class="login-info list-unstyled"> ';if(it.user.get("last_success") && false){out+=' Last successful login: '+encodeHTML(it.helpers.datetime.unixToUTCDateTime(it.user.get("last_success")))+' ';}out+=' ';if(it.user.get("failures")){out+=' <span class="warning"> <i class="fa fa-warning"></i> <strong><a href="#"> Failed login attempts: '+encodeHTML(it.user.get("failures"))+'   (Last: '+encodeHTML(it.helpers.datetime.unixToUTCDateTime(it.user.get("last_failure")))+') &raquo;</a> </strong> </span> ';}out+=' </div></div>';return out;
}
return anonymous;
});
