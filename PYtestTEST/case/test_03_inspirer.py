import requests
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.mysql import query
from utils.exceltools import read_excel
from utils.filetools import read_file

#获取灵感详情
def test_03_hqlgxq():
    data = read_excel("data\测谈网测试用例.xlsx", "灵感")
    u = data[0][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[0][6]

#获取用户灵感列表
def test_03_hqyhlglb():
    data = read_excel("data\测谈网测试用例.xlsx", "灵感")
    u = data[1][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[1][6]

#用户发表灵感
def test_03_yhfblg():
    data = read_excel("data\测谈网测试用例.xlsx", "灵感")
    u = data[2][2]
    h = eval(data[2][5])
    h["token"] = read_file()
    d = eval(data[2][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    global inspirerId
    inspirerId = res.json()["data"]["inspirerid"]
    assert res.status_code == 200
    assert res.json()["status"] == data[2][6]
    sql = "select * from t_inspirer where content = '{}' ".format(d["content"])
    assert query(sql) != 0

#用户修改灵感接口
def test_03_updateyhlg():
    data = read_excel("data\测谈网测试用例.xlsx", "灵感")
    u = data[3][2]
    h = eval(data[3][5])
    h["token"] = read_file()
    d = eval(data[3][4])
    d["iid"] = inspirerId
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[3][6]
    sql = "select * from t_inspirer where content = '{}' ".format(d["content"])
    assert query(sql) != 0

#用户删除灵感接口
def test_03_deleteyhlg():
    data = read_excel("data\测谈网测试用例.xlsx", "灵感")
    u = data[4][2]
    h = eval(data[4][5])
    h["token"] = read_file()
    d = eval(data[4][4])
    d["iid"] = inspirerId
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[4][6]
    sql = "select status from t_inspirer where id = '{}' ".format(d["iid"])
    print(query(sql))
    assert int(query(sql)[0][0]) == 1