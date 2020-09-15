import requests
import pytest
import os, sys
sys.path.append(os.getcwd())

from utils.mysql import query
from utils.filetools import read_file
from utils.exceltools import read_excel

#获取用户问题列表
def test_04_hqquestion():
    data = read_excel("data\测谈网测试用例.xlsx", "问题")
    u = data[0][2]
    res = requests.get(u)
    assert res.status_code == 200
    assert res.json()["status"] == data[0][6]


#用户提问接口
def test_04_yhtquestion():
    data = read_excel("data\测谈网测试用例.xlsx", "问题")
    u = data[1][2]
    h = eval(data[1][5])
    h["token"] = read_file()
    d = eval(data[1][4])
    res = requests.post(url=u,json=d,headers=h)
    print(res.json())
    global questionId
    questionId = res.json()["data"]["questionid"]
    assert res.status_code == 200
    assert res.json()["status"] == data[1][6]
    sql = "select * from t_questions where id = '{}' ".format(questionId)
    assert query(sql) != 0


# 用户修改提问接口
def test_04_yhxgquestion():
    data = read_excel("data\测谈网测试用例.xlsx", "问题")
    u = data[2][2]
    h = eval(data[2][5])
    h["token"] = read_file()
    d = eval(data[2][4])
    d["qid"] = questionId
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == 200
    assert res.json()["status"] == data[2][6]
    sql = "select content from t_questions where id = '{}' ".format(questionId)
    assert query(sql)[0][0] == d["content"]


# #用户删除提问接口
def test_04_yhdelquestion():
    data = read_excel("data\测谈网测试用例.xlsx", "问题")
    u = data[3][2]
    h = eval(data[3][5])
    h["token"] = read_file()
    d = eval(data[3][4])
    d["qid"] = questionId
    res = requests.post(url=u,json=d,headers=h)
    assert res.status_code == 200
    assert res.json()["status"] == data[3][6]
    sql = "select status from t_questions where id = '{}' ".format(questionId)
    assert query(sql)[0][0] == 1