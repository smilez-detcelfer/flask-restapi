import requests
import json

BASE = 'http://127.0.0.1:5000/'


headers = {'accept': 'application/json'}
# payload = {#'secret_key': 'jG10xrcBjaqfBWt-ZXC9yVmtooAQQgYzOgGF6yndDAsUVdJtm_14TQ'
#            'username': 'smile123',
#            'email': 'email111xxx@domain.xxx',
#            'password': '1234567'
#            }
# response = requests.post(BASE + 'api/generate_encrypted_secret', json=payload)
payload = {'secret_key': 'Ttc0aGSzKeupM6ai6QjIkYwMftwBV2NZJ2XJ4ZZq0nmLqGPyCw8xIg'}
response = requests.post(BASE + 'api/getuserinfo', json=payload)
print(response.json())