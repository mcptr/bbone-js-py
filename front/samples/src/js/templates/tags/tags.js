define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div><ul class="list-inline"> ';var arr1=it.data;if(arr1){var tag,idx=-1,l1=arr1.length-1;while(idx<l1){tag=arr1[idx+=1];out+=' <li class="tag"><a href="/tags/'+encodeHTML(tag.ident)+'">'+encodeHTML(tag.ident)+'</a></li> ';} } out+='</ul></div>';return out;
}
return anonymous;
});
