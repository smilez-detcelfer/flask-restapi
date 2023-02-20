from . import db
from datetime import datetime
from flask_login import UserMixin
from flask_restful import fields
import secrets


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Integer, default=0)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return 'User >> {self.username}'

# serealisation for marshal_with decarator
resource_fields_user = {
    'id' : fields.Integer,
    'username' : fields.String,
    'password' : fields.String,
    'email' : fields.String,
    'balance' : fields.Integer
}