from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from social_flask import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(1500), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    short_bio = db.Column(db.String(250))
    created_on = db.Column(db.DateTime)
    
    posts = relationship(
        'Post', 
        backref='owner'
    )
    liked_posts = relationship(
        'PostLikes',
        backref='user'
    )
    
    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        created_on: datetime,
        short_bio = None
    ) -> None:
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf8')
        self.name = name
        self.short_bio = short_bio
        self.created_on = created_on


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer, ForeignKey('users.id'))
    created_on = db.Column(db.DateTime)
    
    likes = relationship(
        'PostLikes',
        backref='post'
    )
    
    def __init__(
        self,
        title: str,
        text: str,
        owner_id: int,
        created_on: datetime
    ) -> None:
        self.title = title
        self.text = text
        self.owner_id = owner_id
        self.created_on = created_on


class PostLikes(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    post_id = db.Column(db.Integer, ForeignKey('posts.id'))

    def __init__(
        self,
        user_id: int,
        post_id: int
    ) -> None:
        self.user_id = user_id
        self.post_id = post_id
