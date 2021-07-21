from social_flask import api
from social_flask.resources.users import (
    Register,
    Login,
    Profile
)

api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(Profile,'/me')