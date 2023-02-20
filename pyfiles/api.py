from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse, marshal_with
from pyfiles import db
from .models import User, resource_fields_user
apipage = Blueprint('api', __name__)
api = Api(apipage)


args_userinfo = reqparse.RequestParser()
args_userinfo.add_argument('username', type=str, required=True, help='username required')

class GetUserInfo(Resource):
    def get(self):
        return {'message': 'get request received'}
    @marshal_with(resource_fields_user) # convert class instance to dictionary with resource_field template
    def post(self):
        args = args_userinfo.parse_args()
        user = User.query.filter_by(username = args['username']).first()
        print(user)
        if user == None:
            return {'message': 'user is not exist'}
        else:
            return user




api.add_resource(GetUserInfo, '/getuserinfo')

########## json 1st try #############
# userlist = [{'name': 'smilez', 'surname': 'detcelfer'},
#             {'name': 'hui', 'surname': 'sobachi'},
#             {'name': 'smilez', 'surname': 'thesecond'}]
# @apipage.route('/<string:name>', methods=['GET'])
# def checkuser(name):
#     user_filtered = [user for user in userlist if user['name'] == name]
#     return jsonify(user_filtered)
########## json 1st try #############