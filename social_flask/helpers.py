from social_flask import bcrypt, jwt
from social_flask.models import (
    User,
    PostLikes
)

def authenticate(email: str, password: str) -> User:
    user: User = User.query.filter_by(email = email).first_or_404()
    
    if bcrypt.check_password_hash(user.password, password):
        return user
    
    raise ValueError


@jwt.user_identity_loader
def user_identity_lookup(user: User) -> int:
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(id=identity).one_or_none()


def has_liked(user_id: int, post_id: int) -> bool:
    return PostLikes.query.filter(
            PostLikes.user_id == user_id,
            PostLikes.post_id == post_id
        ).count() > 0
