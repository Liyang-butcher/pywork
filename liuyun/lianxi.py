# print("xixi ",end="")
# print(23333,2.33,(),[],{})

# print("xixi"+"haha")
# print(233+322)

# name = "李四"
# print(name)

# res = (1+10%3+10/5+1*3)
# print(res)
# 
# a = input("请输入: ")
# print("刚才输入的值: ",a)

# res = (2**4)
# print(res)
# a = input()
# print(type(a))
# a = input("请输入: ")
# b = input("请输入: ")
# print("输出: ",float(a)+float(b))

# print(1>2)
# print(1<2)



# print(type(None))

# a = float(input("请输入: "))
# b = float(input("请输入: "))
# print("输出: ",a+b)


# print(type({}))

# print(len("sfdsfsfsg"))
# print(len(12345))

# a = (1,3,5,7,9,"哈哈",True,None,)
# # print(a[6])
# print(a.index(1))
# print(a.count(1))
# a = ((1,2),(3,4))
# print(a[0][1])

# a = ((1,2,(3,4)),(1,2))
# print(a[0][2][1])
# print(a[0][2].index(3))
# print(a[0].count(1))

# a = [1,3,5,7,9,"哈哈",True,None]
# name = input("请输入值: ")
# a.append(name)
# a.insert(4,name)
# xx = a.pop(4)
# print(a)

# a = [(1,2),3,4]
# i = a.pop(1)
# print(i)
# print(a)

a = [1,3]
c = ["da"]
d = [4,5]
a = a + c + d
# a.extend(c)
# a.extend(d)
print(a)


#字典
# a = {"name":"李杨","age":"18"}
# a["xinq"] = "喔嚯"
# del a["age"]
# print(a["xinq"])


# a = 20
# if a > 18:
#     print("已成年")
# else:
#     print("未成年")

# a = int(input("请输入年龄: "))
# if a > 18:
#     print("黄花大闺女")
# else:
#     print("钢铁直男")

# b = len(input("请输入字符串: "))
# if b > 6:
#     print("内容合格")
# else:
#     print("内容不合格")

# a = 16
# if a > 18:
#     print("中年")
# elif a > 16:
#     print("青年")
# else:
#     print("小孩")


# a = input("请输入账号: ")
# b = input("请输入密码: ")
# if len(a) > 5 and len(a) < 8:
#     if b == "123456":
#         print("登录成功")
#     else:
#         print("登录失败")
# else:
#     print("登陆失败")


# a = 15
# if a > 30:
#     print("大了")
# else:
#     if a > 20:
#         print("还是大了")
#     else:
#         print("小了")

# a = 60
# while a > 0:
#     if a <= 35:
#         print("红灯")
#     elif a >= 36 and a <= 55:
#         print("绿灯")
#     elif a >= 56 and a <= 60:
#         print("黄灯")
#     a = a - 1
# a = 45
# if a > 50:
#     print("太大")
# elif a > 40:
#     print("小了")

# a = [1,2,3,4,5]
# for i in a[0]:
#     print(i)

# a = {"use":"李杨","age":"18"}
# for i in a:
#     print(i)
#     print(a[i])



# 什么算法，怎么实现出来
# a = ["胡", "张", "王", "夏", "张", "李"]，请用python写出a列表中重复元素的下标和值

# 排序：
# a = [1,2,3,4,555,333,22211,-1], 请使用python对a列表进行从小到大的排序

# 作业：
# b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
# 输入一个账号和密码，如果b中存在这个账号，那就注册失败，如果b中没有这个账号，就到b里面去添加账号和密码



# name = {"username":"小美", "password":"123456"}
# # name = {"username":u,"password":p}
# # b.append(name)
# # print(b)
def regist(u,p):
    b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
    
    a = 1
    for i in b:
        if u == i.get("username"):
            print("账号注册失败")
            break
        else:
            if a == len(b):
                tj = {"username":u,"password":p}
                b.append(tj)
                print("账号注册成功")
                print(b)
                break
        a = a + 1
u = input("请输入注册账号: ")
p = input("请输入注册密码: ")
regist(u,p)

# 算法去重题
# a = ["胡", "张", "王", "夏", "张", "李","胡","钱","孙"]
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[i] == a[j+1+i]:
#             print("重复元素为:{}，它的下标为:{}".format(a[i],i))
            
 
# 练习：自定义一个减法方法/函数，要求去调用这个方法，显示返回值

# def jian(s1,s2):
#     s = s1 - s2
#     return s

# a = jian(s2=8,s1=2)
# print(a)


