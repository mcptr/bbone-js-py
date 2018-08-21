define([], function() {function anonymous(it) {
var out='<p> ';if(it.data.session){out+=' <small>'+(it.data.session.id)+'</small> ';}out+=' ';if(it.data.user){out+=' <small>UID: '+(it.data.user.id)+'</small> ';}out+='</p>';return out;
}
return anonymous;
});
