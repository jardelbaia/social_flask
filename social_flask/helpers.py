from social_flask import bcrypt, jwt
from social_flask.models import User

def authenticate(email, password):
    user = User.query.filter_by(email = email).first_or_404()
    
    if bcrypt.check_password_hash(user.password, password):
        return user
    
    raise ValueError


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(id=identity).one_or_none()


