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
from social_flask.helpers import has_liked
from social_flask.schemas.posts import (
    post_schema,
    posts_schema,
    like_schema
)
from social_flask.models import (
    Post,
    PostLikes
)

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


class LikePost(Resource):

    @jwt_required()
    def post(self):
        like_input = request.get_json()

        try:
            data = like_schema.load(like_input)
            user_id = current_user.id
            post_id = data['post_id']
        except ValidationError as err:
            return {'errors': err.messages}

        data = {}

        if not has_liked(user_id, post_id):
            new_like = PostLikes(
                user_id = user_id,
                post_id = post_id
            )
            db.session.add(new_like)
            db.session.commit()

            data = like_schema.dump(new_like)
            data['msg'] = 'Post liked!'
        else:
            PostLikes.query.filter_by(
                user_id = user_id,
                post_id = post_id
            ).delete()
            db.session.commit()
            data['msg'] = 'Post unliked'

        return data