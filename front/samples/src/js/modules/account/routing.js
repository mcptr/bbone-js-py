define([
	"./controllers/login",
	"./controllers/register",
	"./controllers/password_reset",
	"./controllers/dashboard",
	"./controllers/logout",
	"./controllers/profile/settings",
	"./controllers/profile/password",
	"./controllers/profile/userdata",
	"./controllers/profile/notifications",
	"./controllers/content/posts",
	"./controllers/content/comments",
	"./controllers/content/channels",
	"./controllers/content/favorite",
	"./controllers/subscriptions/channels",
	"./controllers/subscriptions/users",
	"./controllers/blacklist/users",
	"./controllers/blacklist/categories",
	"./controllers/blacklist/tags"
], function(LoginCtrl, RegisterCtrl, PasswordResetCtrl, DashboardCtrl, LogoutCtrl,
			ProfileSettingsCtrl, ProfilePasswordCtrl, ProfileUserDataCtrl,
			ProfileNotificationsCtrl,
			ContentPostsCtrl, ContentCommentsCtrl, ContentChannelsCtrl,
			ContentFavoriteCtrl,
			SubscriptionsChannelsCtrl, SubscriptionsUsersCtrl,
			BlacklistUsersCtrl, BlacklistCategories, BlacklistTags) {
	function setUp(dispatcher, options) {
		return {
			namespace: "account",
			routes: {
				"(/)" : "dashboard",
				"login(/)" : "login",
				"logout(/)" : "logout",
				"register(/)" : "register",
				"password-reset(/)" : "passwordReset",
				"dashboard(/)" : "dashboard",
				"notifications(/)" : "notifications",

				"profile/settings(/)": "profileSettings",
				"profile/password(/)": "profilePassword",
				"profile/data(/)": "profileData",
				"profile/notifications(/)": "profileNotifications",

				"content/posts(/)": "contentPosts",
				"content/comments(/)": "contentComments",
				"content/channels(/)": "contentChannels",
				"content/favorite(/)": "contentFavorite",

				"subscriptions/users(/)": "subscriptionsUsers",
				"subscriptions/channels(/)": "subscriptionsChannels",

				"blacklist/users(/)": "blacklistUsers",
				"blacklist/categories(/)": "blacklistCategories",
				"blacklist/tags(/)": "blacklistTags",

			},
			login: function() {
				dispatcher(LoginCtrl, arguments);
			},
			register: function() {
				dispatcher(RegisterCtrl, arguments);
			},
			passwordReset: function() {
				dispatcher(PasswordResetCtrl, arguments);
			},
			dashboard: function() {
				dispatcher(DashboardCtrl, arguments);
			},
			logout: function() {
				dispatcher(LogoutCtrl, arguments);
			},
			notifications: function() {
				//dispatcher(LogoutCtrl, arguments);
			},

			profileSettings: function() {
				dispatcher(ProfileSettingsCtrl, arguments);
			},
			profileData: function() {
				dispatcher(ProfileUserDataCtrl, arguments);
			}

		};
	}

	return setUp;
});
