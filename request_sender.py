import requests
import json

BASE = 'http://127.0.0.1:5000/'

# payload = {'username': 'smilez', 'secret_key': '123456'}
# headers = {'accept': 'application/json'}
# response = requests.post(BASE + 'api/getuserinfo', json=payload)
# print(response.json())

payload = {'username': 'smifdsddleddfgsz2', 'email': '15dddsd6fddg@d123.ru', 'password': '1234567'}
headers = {'accept': 'application/json'}
response = requests.post(BASE + 'api/generate_encrypted_secret', json=payload)
print(response.json())