define([
	"core/controller",
	"../views/categories",
	"../models/categories"
], function(Controller, CategoriesView, CategoriesModel) {
	var CategoriesController = Controller.extend({
		initialize: function(args) {
			this.api.page.setLayout("layout-right");
			var categoriesModel = new CategoriesModel();
			var view = new CategoriesView({
				el: "#main-content .layout-active .main-view",
				model: categoriesModel
			});
			categoriesModel.fetch();
		}
	});

	return CategoriesController;
});
