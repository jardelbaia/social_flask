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
    posts_schema
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


class SinglePost(Resource):

    def get(self, post_id):
        
        try:
            post_to_view = Post.query.filter_by(id = post_id).first_or_404()
        except:
            return {'error': 'Post not find'}

        return post_schema.dump(post_to_view)
    
    @jwt_required()
    def delete(self, post_id):

        try:
            post_to_delete = Post.query.filter_by(id = post_id).first_or_404()
        except:
            return {'error': 'Post not find'}
        
        if post_to_delete.owner_id != current_user.id:
            return {'error': 'Unauthorized'}

        PostLikes.query.filter_by(post_id = post_id).delete()
        Post.query.filter_by(id = post_id).delete()
        db.session.commit()

        return {'msg': 'Post deleted!'}


class LikePost(Resource):

    @jwt_required()
    def post(self, post_id):
        print(post_id, type(post_id))
        try:
            Post.query.filter_by(id = post_id).first_or_404()
        except:
            return {'error': 'Post not find'}

        user_id = current_user.id

        if not has_liked(user_id, post_id):
            new_like = PostLikes(
                user_id = user_id,
                post_id = post_id
            )
            db.session.add(new_like)
            db.session.commit()

            msg = 'Post liked!'
        else:
            PostLikes.query.filter_by(
                user_id = user_id,
                post_id = post_id
            ).delete()
            db.session.commit()
            msg = 'Post unliked'

        return {'msg': msg}