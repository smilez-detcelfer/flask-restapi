from flask import Blueprint, jsonify, request, make_response
from flask_restful import Api, Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import uuid
from pyfiles import db
apipage = Blueprint('api', __name__)
api = Api(apipage)
from .models import User


# get user info
args_userinfo = reqparse.RequestParser()
args_userinfo.add_argument('username', type=str, required=True, help='username required')
class UserInfo(Resource):
    def get(self):
        return {'message': 'get request received'}

    def post(self):
        args = args_userinfo.parse_args()
        user = User.query.filter_by(username = args['username']).first()
        if user:
            userdata = {
                'username': f'{user.username}',
                'user password': f'{user.password}'
            }
            return userdata
        return {'message': 'user not found'}

api.add_resource(UserInfo, '/getuserinfo')


# add new user
args_user_add = reqparse.RequestParser()
args_user_add.add_argument('username', type=str, required=True, help='username required')
args_user_add.add_argument('password', type=str, required=True, help='password required')
args_user_add.add_argument('email', type=str, required=True, help='email required')
class UserAdd(Resource):
    def post(self):
        args = args_user_add.parse_args()
        user = User.query.filter_by(username = args['username']).first()
        if user:
            return {'message': 'username has already taken'}
        user = User.query.filter_by(email=args['email']).first()
        if user:
            return {'message': 'email has already taken'}
        user = User(username=args['username'],
                    password=generate_password_hash(args['password'], method='sha256'),
                    email=args['email'],
                    secret_key=uuid.uuid4())
        db.session.add(user)
        db.session.commit()
        return {'message': 'user created'}

api.add_resource(UserAdd, '/useradd')

#generate encrypted api key
args_generate_encrypted_secret = reqparse.RequestParser()
args_generate_encrypted_secret.add_argument('username', type=str, required=True, help='username required')
args_generate_encrypted_secret.add_argument('password', type=str, required=True, help='password required')
args_generate_encrypted_secret.add_argument('email', type=str, required=True, help='email required')
class generate_encrypted_secret(Resource):
    def post(self):
        args = args_generate_encrypted_secret.parse_args()
        user = User.query.filter_by(username = args['username']).first()
        if user:
            return {'message': 'username has already taken'}
        user = User.query.filter_by(email=args['email']).first()
        if user:
            return {'message': 'email has already taken'}
        secret_key = secrets.token_urlsafe(40)
        user = User(value=secret_key,
                    username=args['username'],
                    password=generate_password_hash(args['password'], method='sha256'),
                    email=args['email'],
                    secret_key=secret_key
                    )
        db.session.add(user)
        db.session.commit()
        decrypted_key = user.value
        user = User.query.filter_by(value = decrypted_key).first()
        print(user.value)
        return {'message': 'user created'}

api.add_resource(generate_encrypted_secret, '/generate_encrypted_secret')