from pprint import pprint
from requests import get, post


# pprint(get('http://localhost:5050/api/v2/register/sa/030669').json())
# pprint(get('http://localhost:5050/api/v2/user/15').json())

data = {'login': 'sa', 'password': '030669'}
response = post('http://85.93.48.241:5077/api/login', json=data).json()
print(response['message'])
token = response.get('token', None)
pprint(token)

data = {'idUsers': 512}
headers = {'Authorization': 'Bearer ' + token}
response = get('http://85.93.48.241:5077/api/secret', headers=headers, json=data).json()
print(response)
