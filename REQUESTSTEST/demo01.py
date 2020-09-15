import requests
from mysql import query
#python调用接口

#1.构造请求
u = "http://118.24.105.78:2333/get_title_img"
res = requests.get(u)
# print(res.json())
# print(res.text)

#2.判断结果：断言实现判断
assert res.status_code == 200  #判断请求码是否为200

assert res.json()["status"] == 200  #判断返回数据中的status值是否为200

data = res.json()["data"]
for i in data:
    sql = "select * from t_title_img where id = {}".format(i["id"])
    r = query(sql)
    assert len(r) != 0

    
# sql = "select * from t_title_img where id = 270 or id = 271"
# r = query(sql)
# print(r)