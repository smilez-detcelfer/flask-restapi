import requests
import json


BASE = 'http://127.0.0.1:5000/'
# payload = {'username': 'smilez', 'secret_key': '123456'}
# headers = {'accept': 'application/json'}
# response = requests.post(BASE + 'api/getuserinfo', json=payload)
# print(response.json())

headers = {'accept': 'application/json'}
payload = {'username': 'username1',
           'email': 'emailxxx@domain.xxx',
           'password': '1234567'}

response = requests.post(BASE + 'api/generate_encrypted_secret', json=payload)
print(response.json())