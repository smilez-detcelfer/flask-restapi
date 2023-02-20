from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse
from pyfiles import db
apipage = Blueprint('api', __name__)
api = Api(apipage)
from .models import User

users = [{'username' : 'smilez', 'password' : '123456'},
        {'username' : 'zelims', 'password' : '654321'}]

# @apipage.route('/', methods = ['GET', 'POST'])
# def first_api():
#     return jsonify({'message': 'welcome'})

args_userinfo = reqparse.RequestParser()
args_userinfo.add_argument('username', type=str, required=True, help='username required')


class GetUserInfo(Resource):
    def get(self, username):
        print(username)
        return (users[0])


api.add_resource(GetUserInfo, '/getuserinfo/<string:username>')

########## json 1st try #############
# userlist = [{'name': 'smilez', 'surname': 'detcelfer'},
#             {'name': 'hui', 'surname': 'sobachi'},
#             {'name': 'smilez', 'surname': 'thesecond'}]
# @apipage.route('/<string:name>', methods=['GET'])
# def checkuser(name):
#     user_filtered = [user for user in userlist if user['name'] == name]
#     return jsonify(user_filtered)
########## json 1st try #############