from . import db
from pyfiles.aes_encryption import  aes_encrypt, aes_decrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.hybrid import Comparator

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Integer, default=0)
    secret_key = db.Column(db.Text(), nullable=False)
    enc_secret_key = db.Column(db.Text(), unique=True, nullable=False)

    @hybrid_property
    def value(self):
        return aes_decrypt(self.enc_secret_key)

    @value.setter
    def value(self, value):
        self.enc_secret_key = aes_encrypt(value)

    class encrypt_comparator(Comparator):
        def operate(self, op, other, **kw):
            return op(
                self.__clause_element__(), aes_encrypt(other),
                **kw
            )

    @value.comparator
    def value(cls):
        return cls.encrypt_comparator(
                    cls.enc_secret_key
                )
    # init consturtion should be disabled
    # def __init__(self, username, email, password, secret_key):
    #     self.username = username
    #     self.email = email
    #     self.password = password
    #     self.secret_key = secret_key

    def __repr__(self) -> str:
        return 'User >> {self.username}'