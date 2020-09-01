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

# a = [1,3,5,7,9,"哈哈",True,None,]
# name = input("请输入值: ")
# a.append(name)
# a.insert(4,name)
# xx = a.pop(4)
# print(xx)

#字典
# a = {"name":"李杨","age":"18"}
# a["xinq"] = "喔嚯"
# del a["age"]
# print(a.get("xinq"))


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


a = input("请输入账号: ")
b = input("请输入密码: ")
if len(a) > 5 and len(a) < 8:
    if b == "123456":
        print("登录成功")
    else:
        print("登录失败")
else:
    print("登陆失败")




