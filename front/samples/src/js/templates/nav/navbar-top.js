define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<!-- Static navbar --><nav class="navbar navbar-default navbar-static-top navbar-fixed-top"> <div class="container"> <div class="navbar-header"> <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar"> <span class="sr-only">Toggle navigation</span><i class="fa fa-bars"></i> Menu </button> <a class="navbar-brand" href="'+encodeHTML(it.helpers.route('index'))+'">[ TEX ] </a> </div> <div id="navbar" class="navbar-collapse collapse"> <ul class="nav navbar-nav"> <li><a href="'+encodeHTML(it.helpers.route('fresh:posts:index'))+'">fresh</a></li> <li> <a href="'+encodeHTML(it.helpers.route('categories:index'))+'">categories</a></li> </ul> <ul class="nav navbar-nav navbar-right"> <li class="utility-link"> <a href="'+encodeHTML(it.helpers.route('search'))+'"> <i class="fa fa-search"></i> <span class="text">Search</span> </a></li>';if(it.user.isAuthenticated()){out+=' <li class="notifications-link"> <a href="'+encodeHTML(it.helpers.route('account:notifications'))+'"> <i class="fa fa-bell"></i> <small>'+encodeHTML(it.data.notifications_count)+'12</small> <span class="text">Notifications</span> </a></li> <li class="profile-link"> <a href="'+encodeHTML(it.helpers.route('account:dashboard'))+'"> <small>'+encodeHTML(it.user.get("username"))+'</small> <i class="fa fa-user"></i> </a></li> <li class="logout-link"> <a href="'+encodeHTML(it.helpers.route('account:logout'))+'"> <i class="fa fa-sign-out"></i> <span class="text">Logout</span> </a></li>';}else{out+=' <li><a href="'+encodeHTML(it.helpers.route(':account:login'))+'">account</a></li>';}out+=' </ul> </div><!--/.nav-collapse --> </div></nav>';return out;
}
return anonymous;
});
