from sqlalchemy import ForeignKey

from social_flask import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(1500))
    name = db.Column(db.String(100), nullable=False)
    short_bio = db.Column(db.String())
    created_on = db.Column(db.DateTime)
    
    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        created_on,
        short_bio: str = None
    ) -> None:
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf8')
        self.name = name
        self.short_bio = short_bio
        self.created_on = created_on
