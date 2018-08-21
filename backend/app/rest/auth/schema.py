from marshmallow import Schema, fields


class AuthSchema(Schema):
	ident = fields.String(required=True)
	password = fields.String(required=True)
	social_uid = fields.String()
	social_provider = fields.String()
	social_access_token = fields.String()
