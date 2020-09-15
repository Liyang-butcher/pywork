import requests
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.mysql import query
from utils.filetools import read_file
from utils.exceltools import read_excel

#获取用户关注列表
def test_06_hqyhgzlb():
    data = read_excel("data\测谈网测试用例.xlsx","关注")
    u = data[0][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[0][6]


#点赞/取消点赞
def test_06_fellgoods():
    data = read_excel("data\测谈网测试用例.xlsx", "关注")
    u = data[1][2]
    h = eval(data[1][5])
    h["token"] = read_file()
    d = eval(data[1][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[1][6]
    sql = "select gstatus from t_coures_user_status where uid = '{}' and cid = '{}' ".format(1333385544,d["gid"])
    assert int(query(sql)[0][0]) == 0

def test_06_qxfellgoods():
    data = read_excel("data\测谈网测试用例.xlsx", "关注")
    u = data[1][2]
    h = eval(data[1][5])
    h["token"] = read_file()
    d = eval(data[1][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[1][6]
    sql = "select gstatus from t_coures_user_status where uid = '{}' and cid = '{}' ".format(1333385544,d["gid"])
    assert int(query(sql)[0][0]) == 1


#收藏成功
def test_06_follections():
    data = read_excel("data\测谈网测试用例.xlsx", "关注")
    u = data[2][2]
    h = eval(data[2][5])
    h["token"] = read_file()
    d = eval(data[2][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[2][6]
    sql = "select cstatus from t_coures_user_status where uid = '{}' and cid = '{}' ".format(1333385544,d["cid"])
    assert int(query(sql)[0][0]) == 0

#取消收藏
def test_06_qxfollections():
    data = read_excel("data\测谈网测试用例.xlsx", "关注")
    u = data[2][2]
    h = eval(data[2][5])
    h["token"] = read_file()
    d = eval(data[2][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[2][6]
    sql = "select cstatus from t_coures_user_status where uid = '{}' and cid = '{}' ".format(1333385544,d["cid"])
    assert int(query(sql)[0][0]) == 1


#关注
def test_06_yhfollows():
    data = read_excel("data\测谈网测试用例.xlsx", "关注")
    u = data[3][2]
    h = eval(data[3][5])
    h["token"] = read_file()
    d = eval(data[3][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[3][6]
    sql = "select fstatus from t_coures_user_status where uid = '{}' and cid = '{}' ".format(1333385544,d["fid"])
    assert int(query(sql)[0][0]) == 0



#取消关注
def test_06_qxyhfollows():
    data = read_excel("data\测谈网测试用例.xlsx", "关注")
    u = data[3][2]
    h = eval(data[3][5])
    h["token"] = read_file()
    d = eval(data[3][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[3][6]
    sql = "select fstatus from t_coures_user_status where uid = '{}' and cid = '{}' ".format(1333385544,d["fid"])
    assert int(query(sql)[0][0]) == 1