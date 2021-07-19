from social_flask import bcrypt
from social_flask.models import User

def authenticate(email, password):
    user = User.query.filter_by(email = email).first_or_404()
    
    if bcrypt.check_password_hash(user.password, password):
        return user
    
    raise ValueError
