from pjxxs import fields

schema = fields.Schema("post", 1)
schema.add_field(fields.String("title", required=True))
