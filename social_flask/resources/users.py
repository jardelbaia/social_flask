import datetime as dt
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    current_user
)
from marshmallow import ValidationError, validate
from typing import Dict

from social_flask import bcrypt, db, jwt
from social_flask.models import User
from social_flask.helpers import authenticate
from social_flask.schemas.users import (
    user_schema,
    users_schema,
    login_schema
)


class Register(Resource):

    def post(self) -> Dict:
        register_input = request.get_json()

        try:
            data: Dict = user_schema.load(register_input)
            email: str = data['email']
            name: str = data['name']
            password: str = data['password']
            short_bio = None 
            if 'short_bio' in data:
                short_bio: str = data['short_bio']
        except ValidationError as err:
            return {'errors': err.messages}

        try:
            user: User = User.query.filter_by(email = email).first_or_404()
            
            return {'error': 'user already registered'}
        except:
            new_user = User(
                email = email,
                name = name,
                password = password,
                short_bio = short_bio,
                created_on = dt.datetime.now()
            )
            db.session.add(new_user)
            db.session.commit()

        data: Dict = user_schema.dump(new_user)
        data['msg'] = 'User created! Please login'

        return data

class Login(Resource):

    def post(self) -> Dict:
        login_input = request.get_json()

        try:
            data: Dict = login_schema.load(login_input)
            email = data['email']
            password = data['password']
        except ValidationError as err:
            return {'errors': err.messages}
        
        try:
            user: User = authenticate(email, password)
        except ValueError:
            return {'error': 'Incorrect password'}
        except:
            return {'error': 'User not found'}

        response: Dict = user_schema.dump(user)
        response['msg'] = 'User logged in!'
        response['token'] = create_access_token(identity=user)

        return response


class Profile(Resource):

    @jwt_required()
    def get(self) -> Dict:
        return user_schema.dump(current_user)
