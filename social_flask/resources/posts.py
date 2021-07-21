import datetime as dt
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    current_user
)
from sqlalchemy import desc
from marshmallow import ValidationError, validate

from social_flask import db
from social_flask.schemas.posts import (
    post_schema,
    posts_schema
)
from social_flask.models import Post


class Posts(Resource):


    def get(self):
        posts = Post.query.order_by(desc(Post.created_on)).all()

        return posts_schema.dump(posts)


    @jwt_required()
    def post(self):
        post_input = request.get_json()

        try:
            data = post_schema.load(post_input)
            title = data['title']
            text = data['text']
        except ValidationError as err:
            return {'errors': err.messages}

        new_post = Post(
            title = title,
            text = text,
            owner_id = current_user.id,
            created_on = dt.datetime.now()
        )
        db.session.add(new_post)
        db.session.commit()

        data = post_schema.dump(new_post)
        data['msg'] = 'Post created!'

        return data