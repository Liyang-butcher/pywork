import requests
import pytest
import os, sys
sys.path.append(os.getcwd())

from utils.mysql import query
from utils.filetools import read_file
from utils.exceltools import read_excel

#获取文章详情
def test_04_hqarticle():
    data = read_excel("data\测谈网测试用例.xlsx", "文章")
    u = data[0][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[0][6]

#获取用户文章列表
def test_04_hqyharticle():
    data = read_excel("data\测谈网测试用例.xlsx", "文章")
    u = data[1][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[1][6]


#用户写文章接口
def test_04_yhxarticle():
    data = read_excel("data\测谈网测试用例.xlsx", "文章")
    u = data[2][2]
    h = eval(data[2][5])
    h["token"] = read_file()
    d = eval(data[2][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    global articleId
    articleId = res.json()["data"]["articleid"]
    assert res.status_code == 200
    assert res.json()["status"] == data[2][6]
    sql = "select * from t_article where id = '{}' ".format(articleId)
    assert query(sql) != 0

#用户修改文章接口
def test_04_updatearticle():
    data = read_excel("data\测谈网测试用例.xlsx", "文章")
    u = data[3][2]
    h = eval(data[3][5])
    h["token"] = read_file()
    d = eval(data[3][4])
    d["aid"] = articleId
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    assert res.status_code == 200
    assert res.json()["status"] == data[3][6]
    sql = "select title from t_article where id = '{}' ".format(articleId)
    assert query(sql)[0][0] == d["title"]

#用户删除文章接口
def test_04_deletearticle():
    data = read_excel("data\测谈网测试用例.xlsx", "文章")
    u = data[4][2]
    h = eval(data[4][5])
    h["token"] = read_file()
    d = eval(data[4][4])
    d["aid"] = articleId
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == 200
    assert res.json()["status"] == data[4][6]
    sql = "select status from t_article where id = '{}' ".format(articleId)
    assert int(query(sql)[0][0]) == 1