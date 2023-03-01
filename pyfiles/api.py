from flask import Blueprint, jsonify, request, make_response
from flask_restful import Api, Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import uuid
from pyfiles import db
apipage = Blueprint('api', __name__)
api = Api(apipage)
from pyfiles.models import User

#generate encrypted api key
args_generate_encrypted_secret = reqparse.RequestParser()
args_generate_encrypted_secret.add_argument('username', type=str, required=True, help='username required')
args_generate_encrypted_secret.add_argument('password', type=str, required=True, help='password required')
args_generate_encrypted_secret.add_argument('email', type=str, required=True, help='email required')
class generate_encrypted_secret(Resource):
    def post(self):
        args = args_generate_encrypted_secret.parse_args()

        #conditions for uniq user and email
        user = User.query.filter_by(username = args['username']).first()
        if user:
            return {'message': 'username has already taken'}
        user = User.query.filter_by(email=args['email']).first()
        if user:
            return {'message': 'email has already taken'}

        gen_secret_key = secrets.token_urlsafe(40)
        user = User(value=gen_secret_key,  # encrypted secret key in column 'enc_secret_key' (check in models)
                    username=args['username'],
                    password=generate_password_hash(args['password'], method='sha256'),
                    email=args['email'],
                    secret_key=gen_secret_key  # as before (unencrypted)
                    )
        db.session.add(user)
        db.session.commit()

        #show decrypted secret key
        user = User.query.filter_by(value = gen_secret_key).first()
        print(f'decrypted secret: {user.value}')
        return {'message': 'user created'}

api.add_resource(generate_encrypted_secret, '/generate_encrypted_secret')