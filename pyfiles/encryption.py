import binascii
import uuid

from Crypto.Cipher import AES

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import Comparator
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Session

key = b'12345678901234561234567890123456'
"""The encryption key.   Random for this example."""

nonce = b'nonce'
"""for WHERE criteria to work, we need the encrypted value to be the same
each time, so use a fixed nonce if we need that feature.
"""

def aes_encrypt(data):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = data + (" " * (16 - (len(data) % 16)))
    print(f'data: {data}, lenght: {len(data)}')
    return cipher.encrypt(data.encode("utf-8")).hex()


def aes_decrypt(data):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(binascii.unhexlify(data)).decode("utf-8").rstrip()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    encrypted_value = Column(String, nullable=False)

    @hybrid_property
    def value(self):
        return aes_decrypt(self.encrypted_value)

    @value.setter
    def value(self, value):
        self.encrypted_value = aes_encrypt(value)

    class encrypt_comparator(Comparator):
        def operate(self, op, other, **kw):
            return op(
                self.__clause_element__(), aes_encrypt(other),
                **kw
            )

    @value.comparator
    def value(cls):
        return cls.encrypt_comparator(
                    cls.encrypted_value
                )

e = create_engine('sqlite://', echo='debug')

Base.metadata.create_all(e)

s = Session(e)

# attribute set
u1 = User(value="some value")
s.add(u1)
s.commit()

# comparison
u2 = s.query(User).filter_by(value="some value").first()
assert u1 is u2

# attribute get
assert u1.value == "some value"