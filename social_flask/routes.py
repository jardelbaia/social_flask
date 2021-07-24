from social_flask import api
from social_flask.resources.users import (
    Register,
    Login
)
from social_flask.resources.profile import (
    Profile
)
from social_flask.resources.posts import (
    Posts,
    SinglePost,
    LikePost
)


api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(Profile,'/me')
api.add_resource(Posts,'/posts')
api.add_resource(SinglePost,'/post/<post_id>')
api.add_resource(LikePost,'/like_post/<post_id>')
