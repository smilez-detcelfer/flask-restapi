import requests
import json

BASE = 'http://127.0.0.1:5000/'

payload = {"username": 'zelims'}
headers = {'accept': 'application/json'}
response = requests.post(BASE + 'api/getuserinfo', json=payload)
print(response.json())
