from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
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
api = Api(app)
jwt = JWTManager(app)
