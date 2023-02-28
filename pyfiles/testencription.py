import binascii
import uuid

from Crypto.Cipher import AES
encrytpiton_key = b'12345678901234561234567890123456'
encryption_nonce = b'nonce'
secret_key = '9V5JDGiFK3kJAL_AcFjcnIcxoczsHNvyD9SZufV1grjqXo3FJFuxVg'


def aes_encrypt(data):
    cipher = AES.new(encrytpiton_key, AES.MODE_EAX, nonce=encryption_nonce)
    data = data + (" " * (16 - (len(data) % 16)))
    print(f'data: {data}, lenght: {len(data)}')
    return cipher.encrypt(data.encode("utf-8")).hex()


def aes_decrypt(data):
    cipher = AES.new(encrytpiton_key, AES.MODE_EAX, nonce=encryption_nonce)
    return cipher.decrypt(binascii.unhexlify(data)).decode("utf-8").rstrip()

encrypted_secret_key = aes_encrypt(secret_key)
print(encrypted_secret_key)
decrypted_secret_key = aes_decrypt(encrypted_secret_key)
print(f'key: {decrypted_secret_key}')