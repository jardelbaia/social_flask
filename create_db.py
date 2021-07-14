from social_flask import db
from social_flask import models

def create_db():
    db.create_all()
    db.session.commit()