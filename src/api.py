from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from werkzeug.security import generate_password_hash
import secrets
from src.models import db

apipage = Blueprint('api', __name__)
api = Api(apipage)

from src.models import User
from src.utils.update_user import update_user_login
from src.utils.scheduled_tasks import delete_old_users

#create user with encrypted api key
args_add_user = reqparse.RequestParser()
args_add_user.add_argument('username', type=str, required=True, help='username required')
args_add_user.add_argument('password', type=str, required=True, help='password required')
args_add_user.add_argument('email', type=str, required=True, help='email required')


class AddUser(Resource):
    def post(self):
        args = args_add_user.parse_args()

        #conditions for uniq user and email
        user = User.query.filter_by(username = args['username']).first()
        if user:
            return {'message': 'username has already taken'}
        user = User.query.filter_by(email=args['email']).first()
        if user:
            return {'message': 'email has already taken'}

        gen_secret_key = secrets.token_urlsafe(40) # secret key generation (as before_
        user = User(value=gen_secret_key,  # encrypted secret key in column 'enc_secret_key' (check in models)
                    username=args['username'],
                    password=generate_password_hash(args['password'], method='sha256'),
                    email=args['email'],
                    secret_key=gen_secret_key  # as before (unencrypted)
                    )
        db.session.add(user)
        db.session.commit()
        return {'message': 'user created', 'user secret token (decrypted)': f'{user.value}'}

api.add_resource(AddUser, '/generate_encrypted_secret')

args_get_user_info = reqparse.RequestParser()
args_get_user_info.add_argument('secret_key', type=str, required=True, help='secret key required')

class GetUserInfo(Resource):
    def post(self):
        args = args_get_user_info.parse_args()
        user = User.query.filter_by(value=args['secret_key']).first()
        delete_old_users()
        if user:
            update_user_login(user)
            return {'username': f'{user.username}', 'secret key': f'{user.value}'}
        else:
            return {'message': 'incorrect secret key'}


api.add_resource(GetUserInfo, '/getuserinfo')

# check user balance
args_check_user_balance = reqparse.RequestParser()
args_check_user_balance.add_argument('secret_key', type=str, required=True, help='secret key required')

class CheckUserBalance(Resource):
    def post(self):
        args = args_check_user_balance.parse_args()
        user = db.session.query(User).filter_by(secret_key=args['secret_key']).with_for_update().first()
        if user:
            update_user_login(user)
            return {'user balance': f'{user.balance}'}
        else:
            return {'message': 'incorrect secret key'}


api.add_resource(CheckUserBalance, '/checkuserbalance')