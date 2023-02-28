from . import db
from datetime import datetime
from flask_login import UserMixin
import secrets


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Integer, default=0)
    secret_key = db.Column(db.Text(), nullable=False)

    def __init__(self, username, email, password, secret_key):
        self.username = username
        self.email = email
        self.password = password
        self.secret_key = secret_key

    def __repr__(self) -> str:
        return 'User >> {self.username}'