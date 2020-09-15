import pytest
import requests

#将当前PYTESTTEST文件添加到环境变量中就能找到utils实现跨文件夹调用
#添加到环境变量实现跨文件调用
import os, sys
sys.path.append(os.getcwd())

from utils.mysql import query
from utils.filetools import save_file
from utils.exceltools import read_excel

def test_02_login_success():
    data = read_excel("data\测谈网测试用例.xlsx","登录")
    u = data[0][2]
    d = eval(data[0][4])
    h = eval(data[0][5])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == int(data[0][6])
#数据库检验
    sql = "select * from t_user where username = '{}'".format(d["username"])
    assert query(sql) != 0
    save_file(token=res.json()["data"]["token"])