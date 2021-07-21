from marshmallow import (
    Schema,
    fields,
    validate,
    post_dump
)

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        required=True, 
        validate=[validate.Length(min=2, max=100)]
    )
    text = fields.Str(
        required=True, 
        validate=[validate.Length(min=10, max=1500)]
    )
    created_on = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'posts' if many else 'post'
        return {key: data}


post_schema = PostSchema()
posts_schema = PostSchema(many=True)