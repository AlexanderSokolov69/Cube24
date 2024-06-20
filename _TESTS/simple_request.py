from pprint import pprint
from requests import get, post, put, delete

# pprint(get('http://localhost:5050/api/v2/register/sa/030669').json())
# pprint(get('http://localhost:5050/api/v2/user/15').json())

data = {'login': 'mmm', 'password': 'MMM'}
response = post('http://85.93.48.241:5077/api/login', json=data).json()
print(response)
token = response.get('token', None)
# pprint(token)

# data = {'idUsers': 512}
# headers = {'Authorization': 'Bearer ' + token}
# response = get('http://172.16.1.56:5077/api/secret', headers=headers, json=data).json()
# print(response)


# data = {'fam': 'fam',
#         'ima': 'ima',
#         'name': 'name',
#         'login': 'login',
#         'sertificate': '0000000000',
#         'idRoles': 0,
#         'idPlaces': 0,
#         'id': 1050
#         }
data = {'table': 'Groups'}
headers = {'Authorization': 'Bearer ' + token}
response = post('http://85.93.48.241:5077/api/info/dict_by_name', headers=headers, json=data).json()
pprint(response)
