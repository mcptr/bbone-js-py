define([], function() {function anonymous(it) {
var out='<div> <form class="form-group" role="search" action="/"> <div class="input-group"> <input type="text" class="form-control form-control-inline" placeholder="'+(it.search || '...')+'" name="search"> <div class="input-group-btn"> <button class="btn btn-default" type="submit"><i class="fa fa-search"></i></button> </div> </div> </form></div>';return out;
}
return anonymous;
});
