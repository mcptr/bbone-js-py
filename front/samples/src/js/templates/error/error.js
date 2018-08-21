define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div class="error '+encodeHTML(it.data.className)+' error-code-'+encodeHTML((it.data.code || '0'))+'"> <div class="message">'+encodeHTML(it.data.message)+'</div> ';var arr1=it.data.details;if(arr1){var detail,i1=-1,l1=arr1.length-1;while(i1<l1){detail=arr1[i1+=1];out+=' <div class="details">'+encodeHTML(detail)+'</div> ';} } out+=' ';if(it.data.errorId){out+=' <div class="errorId">'+encodeHTML(it.data.errorId)+'</div> ';}out+=' ';if(it.data.traceback){out+=' <div class="traceback">'+encodeHTML(it.data.traceback)+'</div> ';}out+=' ';var arr2=it.data.hints;if(arr2){var hint,i2=-1,l2=arr2.length-1;while(i2<l2){hint=arr2[i2+=1];out+=' <div class="hint">'+encodeHTML(hint)+'</div> ';} } out+='</div>';return out;
}
return anonymous;
});
