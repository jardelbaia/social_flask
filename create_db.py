from social_flask import db


db.create_all()
db.session.commit()