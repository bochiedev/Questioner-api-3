from flask import Blueprint
from flask_restplus import Api
from .views.auth import User




version2 = Blueprint('apiv2', __name__)


api = Api(version2)

# home user
api.add_resource(User,'/accounts')
