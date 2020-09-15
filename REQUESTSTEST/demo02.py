import requests
from mysql import query

url = "http://118.24.105.78:2333/login"
data = {"username":"liyang","password":"a1234567"}
res = requests.post(url=url,json=data)
assert res.status_code == 200
assert res.json()["status"] == 200
print(res.json())