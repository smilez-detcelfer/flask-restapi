import requests
import json


BASE = 'http://127.0.0.1:5000/'
# payload = {'username': 'smilez', 'secret_key': '123456'}
# headers = {'accept': 'application/json'}
# response = requests.post(BASE + 'api/getuserinfo', json=payload)
# print(response.json())

headers = {'accept': 'application/json'}
payload = {'secret_key': 'R-N8vwKapMWyRGtr39uSLB97rizDdXOfI8Ube_OCa9cykJeH6G6xJg'
           #'email': 'emailxxx@domain.xxx',
           #'password': '1234567'
           }

response = requests.post(BASE + 'api/checkuserbalance', json=payload)
print(response.json())