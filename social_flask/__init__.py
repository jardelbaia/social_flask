from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()
print('teste')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = \
                                'postgresql://{}:{}@localhost:5432/{}'\
                                .format(
                                    os.environ.get('POSTGRES_USER'),
                                    os.environ.get('POSTGRES_PASSWORD'),
                                    os.environ.get('POSTGRES_DB')
                                    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return '<h1>HELLO</h1>'
