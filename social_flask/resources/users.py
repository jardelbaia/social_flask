import datetime as dt
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token
)
from marshmallow import ValidationError, validate


from social_flask import bcrypt, db
from social_flask.models import User
from social_flask.helpers import authenticate
from social_flask.schemas import (
    user_schema,
    users_schema,
    login_schema
)

class Register(Resource):
    #rota para retornar todos os usuários
    def get(self):
        try:
            users = User.query.all()
        except:
            return {'erro': 'deu ruim'}

        return users_schema.dump(users) 


    def post(self):
        register_input = request.get_json()

        try:
            data = user_schema.load(register_input)
            email = data['email']
            name = data['name']
            password = data['password']
        except ValidationError as err:
            return {'errors': err.messages}

        try:
            user = User.query.filter_by(email = email).first_or_404()
            
            return {'error': 'user already registered'}
        except:
            new_user = User(
                email = email,
                name = name,
                password = password,
                created_on = dt.datetime.now()
            )
            db.session.add(new_user)
            db.session.commit()

        data = user_schema.dump(new_user)
        data['msg'] = 'User created! Please login'

        return data

class Login(Resource):

    def post(self):
        login_input = request.get_json()

        try:
            data = login_schema.load(login_input)
            email = data['email']
            password = data['password']
        except ValidationError as err:
            return {'errors': err.messages}
        
        try:
            user = authenticate(email, password)
        except ValueError:
            return {'error': 'Incorrect password'}
        except:
            return {'error': 'User not found'}

        response = user_schema.dump(user)
        response['msg'] = 'User logged in!'
        response['token'] = create_access_token(identity=email)

        return response