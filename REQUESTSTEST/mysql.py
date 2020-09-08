import pymysql # 要想用pymysql，就必须要导入它


def query(sql):
    # 固定的方法
    db = pymysql.connect(host='118.24.105.78', user='root', password="1qaz!QAZ123***123", db='ljtestdb')
    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    db.close()#关闭数据库
    return res

if __name__ == "__main__":
    a = query("select price from t_goods")
    if a[0][0] > 5488:
        print("买不起")
    else:
        print("买得起")
    