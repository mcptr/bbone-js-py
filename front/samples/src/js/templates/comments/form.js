define([], function() {function anonymous(it) {
var encodeHTML = typeof _encodeHTML !== 'undefined' ? _encodeHTML : (function (doNotSkipEncoded) {
		var encodeHTMLRules = { "&": "&#38;", "<": "&#60;", ">": "&#62;", '"': "&#34;", "'": "&#39;", "/": "&#47;" },
			matchHTML = doNotSkipEncoded ? /[&<>"'\/]/g : /&(?!#?\w+;)|<|>|"|'|\//g;
		return function(code) {
			return code ? code.toString().replace(matchHTML, function(m) {return encodeHTMLRules[m] || m;}) : "";
		};
	}());var out='<div class="row comment-form"> <div class="error-box"></div> <div class="form-group"> <textarea class="form-control" rows="1" name="comment" placeholder="Comment...">'+encodeHTML(it.data.initialText || "")+'</textarea> </div> <div class="form-group formatting-helpers"> <div class="pull-left"><ul class="list-inline list-unstyled"> <li><button class="btn btn-default btn-mini" data-id="BOLD" title="Bold"><strong>B</strong></button></li> <li><button class="btn btn-default btn-mini" data-id="ITALIC" title="Italic"><strong><i>I</i></strong></button></li> <li><button class="btn btn-default btn-mini" data-id="QUOTE" title="Quote"><strong>" "</strong></button></li> <li><button class="btn btn-default btn-mini" data-id="CODE" title="Code"><strong>&lt;/&gt;</strong></button></li> <li> <button class="btn btn-default btn-mini" data-id="LINK" title="Link"> <strong><i class="fa fa-link"></i></strong> </button> </li> <li> <button class="btn btn-default btn-mini" data-id="IMAGE" title="Image URL"> <strong><i class="fa fa-picture-o"></i> </strong> </button> </li> <!-- 2DO: Implement file upload --> <!-- <li> --> <!--   <button class="btn btn-default btn-mini" data-id="IMAGE_UPLOAD" title="Image upload"> --> <!--     <strong><i class="fa fa-camera"></i></strong> --> <!--   </button> --> <!-- </li> --></ul> </div> <div class="pull-right"><ul class="list-inline list-unstyled"> <li><button class="btn btn-default" data-id="CANCEL">Cancel</button></li> <li><button class="btn btn-primary" data-id="SUBMIT" disabled="disabled">Comment</button></li></ul> </div> </div></div>';return out;
}
return anonymous;
});
