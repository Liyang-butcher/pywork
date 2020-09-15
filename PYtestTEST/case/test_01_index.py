#这个文件下面存放所有的首页相关的测试用例
import pytest
import requests
import pymysql
import os, sys
sys.path.append(os.getcwd())
from utils.mysql import query
from utils.exceltools import read_excel
#测试代码
#获取轮播图
def test_01_lbt():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[0][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[0][6]
    

#获取推荐教程
def test_01_hqtjjc():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[1][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[1][6]

#获取热门评论
def test_01_hqrmpl():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[2][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[2][6]

#获取热门文章
def test_01_hqrmwz():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[3][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[3][6]

#获取灵感
def test_01_hqlg():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[4][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[4][6]

#获取活跃用户
def test_01_hqhyyh():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[5][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[5][6]

#获取问题详情
def test_01_hqhyyh():
    data = read_excel("data\测谈网测试用例.xlsx","首页")
    u = data[6][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[6][6]