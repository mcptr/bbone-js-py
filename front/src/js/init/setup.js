define([
	"underscore",
	"jquery",
	"backbone",
	"core/controller",
	"utils/helpers/url",
	"modules/error/views/error"
], function(_, $, Backbone, Controller, UrlHelper, ErrorView) {

	var Setup = function(api) {
		var self = this;
		self._api = api;

		var currentController = null;

		var animateOnHashChange = function() {
			var anchor = Backbone.history.location.hash;
			var $anchor = $(anchor);
			if($anchor.length) {
				$(window).scrollTop($anchor.offset().top - 100);
				$anchor.flash();
			}
		};

		var extendRouter = function(config) {
			Backbone.Router.prototype.getAPI = function() {
				return self._api;
			};

			Backbone.Router.prototype.dispatch = function(controller, args) {
				try {
					var request = UrlHelper.parse(Backbone.history.getLocation().toString());
					if(currentController) {
						currentController.destroy();
					}

					currentController = (
						(controller instanceof Controller)
							? controller
							: new controller(self._api, args, request)
					);

					if(!(currentController instanceof Controller)) {
						throw "Expected instance of Controller";
					}

					var viewComponents = currentController.getViewComponents();
					//console.log("Dispatching", ctrl, viewComponents);
					viewComponents = (
						viewComponents
							? viewComponents : config.defaultViewComponents
					);
					self._api.event.trigger("view/components", viewComponents);
				}
				catch(e) {
					console.error(e);
					var logger = api.logging.getLogger(this.name);
					logger.error("Dispatching failed", {
						args: args,
						controller: controller,
						exception: e
					});
				}
			};

			Backbone.Router.prototype.setViewConfig = function(config) {
				self._api.trigger(config);
			};

		};

		var extendView = function(config) {
			var helpers = _.extend(self._api.helpers, {
				route: function() {
					return config.routing.getUrlFor.apply(config.routing, arguments);
				}
			});


			Backbone.View.prototype.getAPI = function() {
				return self._api;
			};

			Backbone.View.prototype.attachEvents = function($html) {
				$html.find("a").on("click", function(e) {
					//var origHash = Backbone.history.location.hash;
					if(e.target.getAttribute("data-bypass") === null) {
						e.preventDefault();
						Backbone.history.navigate(e.currentTarget.pathname, {trigger: true});
					}
				});

				// for all anchors without the href - set "#"
				$html.find("a.btn").each(function(idx, el) {
					var $a = $(el);
					if(!$a.prop("href").length) {
						$a.prop("href", "#");
					}
				});
			};

			Backbone.View.prototype.renderError = function(code, options) {
				options = (options || {});
				var msgMap = {
					404: "Resource not found"
				};
				options.message = (options.message || msgMap[code] || "Error");
				options.code = code;
				var errorView = new ErrorView({
					el: this.$el,
					replace: true
				});
				this.$el.empty();
				errorView.render(options);
				this.removeLoadingIndicator();
			};

			Backbone.View.prototype.renderTemplate = function(data) {
				var $result = null;
				try {
					var params = {
						data: (data || {}),
						helpers: helpers,
						user: self._api.user
					};

					$result = $(this.template(params));
					this.attachEvents($result);
				}
				catch(e) {
					var logData = {
						params: data,
						exception: e
					};
					self._api.logging.error("renderTemplate() failed", logData);
					console.error(e);
					return null;
				}
				return $result;
			};

			Backbone.View.prototype.prependTemplate = function(data, options) {
				options = (options || {});
				if(options.empty) {
					this.$el.empty();
				}
				var content = this.renderTemplate(data);
				this.$el.prepend(
					(content === null ? "<p>Rendering failed</p>" : content)
				);
				this.renderFinished(this.id);
				return this;
			};

			Backbone.View.prototype.appendTemplate = function(data, options) {
				options = (options || {});
				if(options.empty) {
					this.$el.empty();
				}
				var content = this.renderTemplate(data);
				this.$el.append(
					(content === null ? "<p>Rendering failed</p>" : content)
				);
				this.renderFinished();
				return this;
			};

			Backbone.View.prototype.renderFinished = function(data) {
				this.trigger("renderFinished", {
					id: this.id,
					data: data
				});

				if(this.restoreScrollPosition) {
					self._api.page.restoreOffsetY();
				}
			};

			Backbone.View.prototype.setLoadingIndicator = function() {
				this.$el.addClass("loading-indicator");
			};

			Backbone.View.prototype.removeLoadingIndicator = function() {
				this.$el.removeClass("loading-indicator");
			};

			Backbone.View.prototype.setLoadError = function(options) {
				this.removeLoadingIndicator();
				if(options.clear) {
					this.$el.empty();
					this.$el.text((options.text || "[ Loading failed ]"));
				}
				this.$el.addClass("load-error");
			};

			Backbone.View.prototype.navigateLocationHash = function() {
				if(!this.anchorVisited) {
					animateOnHashChange();
				}
			};

		};

		var extendHistory = function(config) {
			Backbone.History.prototype.getLocation = function() {
				return this.location;
			};

			var originalLoadUrl = Backbone.History.prototype.navigate;
			Backbone.History.prototype.navigate = function(fragment, soft, options) {
				self._api.page.saveOffsetY(this.getFragment());
				originalLoadUrl.apply(this, arguments);
				self._api.page.restoreOffsetY(this.getFragment());
			};
		};

		var attachEvents = function() {
			var $window = $(window);
			$window.on("hashchange", function() {
				$window.scrollTop($window.scrollTop() - 100);
				animateOnHashChange();
			});
		};

		this.init = function(config) {
			$.ajaxSetup({
				contentType: "application/json; charset=utf-8"
			});

			extendRouter(config);
			extendHistory(config);
			extendView(config);
			attachEvents(config);
		};

	}; // Setup

	return Setup;
});
