from marshmallow import (
    Schema,
    fields,
    validate,
    post_dump
)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(
        required=True, 
        validate=validate.Email(error="Invalid email")
    )
    password = fields.Str(
        required=True, 
        validate=[validate.Length(min=6, max=36)],
        load_only=True
    )
    name = fields.Str(
        required=True
    )
    short_bio = fields.Str()
    
    created_on = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'users' if many else 'user'
        return {key: data}


class LoginSchema(Schema):
    email = fields.Str(
        required=True, 
        validate=validate.Email(error="Invalid email")
    )
    password = fields.Str(
        required=True,
        load_only=True
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = LoginSchema()