from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = \
                                'postgresql://{}:{}@db:5432/{}'\
                                .format(
                                    os.environ.get('POSTGRES_USER'),
                                    os.environ.get('POSTGRES_PASSWORD'),
                                    os.environ.get('POSTGRES_DB')
                                    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db, compare_type=True)

from social_flask.models import User
@app.route('/')
def hello_world():
    return '<h1>salvee</h1>'
