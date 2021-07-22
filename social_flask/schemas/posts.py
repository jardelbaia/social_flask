from marshmallow import (
    Schema,
    fields,
    validate,
    post_dump
)


class LikeSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    post_id = fields.Int(required=True)


    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'likes' if many else 'like'
        return {key: data}


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
    likes = fields.Nested(LikeSchema, many=True)
    created_on = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'posts' if many else 'post'
        return {key: data}


like_schema = LikeSchema()
likes_schema = LikeSchema(many=True)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
