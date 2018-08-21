define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div class="posts top-posts grid-striped"> <ul class="list-inline"> <li class="disabled"><a href="#a">Day</a></li> <li><a href="#b">Week</a></li> <li><a href="#c">Month</a></li> </ul> ';var arr1=it.data;if(arr1){var post,i1=-1,l1=arr1.length-1;while(i1<l1){post=arr1[i1+=1];out+=' <div class="row category '+encodeHTML( (post.category || 'undef'))+'"> <div class="col-xs-4"> <div class="image">';if(post.img_url && post.img_url.length){out+='<img src="'+encodeHTML( post.img_url)+'" alt="..." title="image"/>';}else{out+='<i class="fa fa-eye-slash"></i>';}out+=' </div> </div> <div class="col-xs-8"> <div><a href="'+encodeHTML(it.helpers.route(':posts:post', {id: post.id}))+'">'+encodeHTML(post.title)+'</a></div> <div class="score"><span class="user-score"> ';if(post.top){out+=' <i class="fa fa-bolt top"></i> ';}else if(post.rising){out+=' <i class="fa fa-star-o rising"></i> ';}out+=' +'+encodeHTML( post.stat_votes_plus || "0")+' / -'+encodeHTML( post.stat_votes_minus || "0")+'</span> </div> </div> </div> ';} } out+='</div>';return out;
}
return anonymous;
});
