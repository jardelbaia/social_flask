from social_flask import api
from social_flask.resources.users import (
    Register,
    Login
)

api.add_resource(Register,'/register')
api.add_resource(Login,'/login')