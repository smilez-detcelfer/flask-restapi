import binascii
from Crypto.Cipher import AES
from os import getenv as env

encryption_key = str.encode(env('ENCRYPTION_KEY'))
encryption_nonce = str.encode(env('ENCRYPTION_NONCE'))


def aes_encrypt(data):
    cipher = AES.new(encryption_key, AES.MODE_EAX, nonce=encryption_nonce)
    #adding spaces for necessary size
    data = data + (" " * (16 - (len(data) % 16)))
    return cipher.encrypt(data.encode("utf-8")).hex()


def aes_decrypt(data):
    cipher = AES.new(encryption_key, AES.MODE_EAX, nonce=encryption_nonce)
    return cipher.decrypt(binascii.unhexlify(data)).decode("utf-8").rstrip()

