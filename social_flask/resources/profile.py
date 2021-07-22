from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    current_user
)
from marshmallow import ValidationError, validate

from social_flask.schemas.users import user_schema


class Profile(Resource):

    @jwt_required()
    def get(self):
        return user_schema.dump(current_user)
