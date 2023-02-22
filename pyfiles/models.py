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
    public_key = db.Column(db.Text(), nullable=False)

    def __init__(self, username, email, password, public_key):
        self.username = username
        self.email = email
        self.password = password
        self.public_key = public_key

    def __repr__(self) -> str:
        return 'User >> {self.username}'