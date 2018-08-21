define([], function() {
	var Social = function(api, options) {
		
		var fbLoginCallback = function(response, authCallback) {
			if(response.authResponse) {
				var access_token = response.authResponse.accessToken;
				var user_id = response.authResponse.userID;

				FB.api(
					'/me',
					{
						access_token: access_token,
						fields: "id,name,email,gender"
					},
					function(response) {
						authCallback({
							social_provider: "facebook",
							social_uid: response.id,
							social_access_token: access_token,
							password: "...no-password-for-social",
							username: response.name,
							ident: response.email
						});
					}
				);
			}
		};

		this.fbLogin = function(authCallback) {
			FB.getLoginStatus(function(response) {
				if(response.status !== "connected") {
					FB.login(
						function(response) {
							fbLoginCallback(response, authCallback)
						},
						{
							scope: "public_profile,email",
							enable_profile_selector: true
						}
					);
				}
				else {
					fbLoginCallback(response, authCallback);
				}
			});

		};
	};

	return Social;
});
