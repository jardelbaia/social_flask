from sqlalchemy import ForeignKey

from social_flask import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(1500))
    name = db.Column(db.String(100), nullable=False)

    def __init__(
        self,
        email: str,
        password: str,
        name: str
    ) -> None:
        self.email = email
        self.password = password
        self.name = name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self) -> int:
        return self.id