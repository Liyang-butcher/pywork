# 循环

# 遍历：把每个东西都取出来
chengji = (88,60,59,29,99,20,110)
chengji = [88,60,59,29,99,20,110]
hegede = []
nohege = []
for i in chengji:  # for的in去取值 if
    if i < 60:
        nohege.append(i)
    else:
        hegede.append(i)

print(hegede)
print(nohege)


# 遍历字典
zhanghao = {"username":"王美丽", "chengji":88}
# b = "username"
# a[b] # a["username"]
for i in zhanghao:
    print(i)
    print(zhanghao[i]) # 1. zhanghao["username"] 2. zhanghao["chengji"]

# 补充
# for i in zhanghao.keys():
#     print(i)

# for j in zhanghao.values():
#     print(j)

# for i, j in zhanghao.items():
#     print(i)
#     print(j)


# aa = "乔妹儿是个大美女，好想看照片"
# for i in aa:
#     print(i)

# 序列生成器 [0,1,2,3,4,5,6,7,8,9]
# a = ["张三", "李四", "乔妹儿",1, "王美丽", "小云", "路人甲","乔妹儿", "蔡聪", "马超", "mc", "小玉"]
# for i in range(len(a)):  # len(a) = 10; range(10) > [0,1,2,3,4,5,6,7,8,9]
#     print(a[i])


# 进阶的内容
# a = [ [1,2,3], [4,5,6] ]
b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"}]

# for i in a:
#     # 1. i = [1,2,3] > 1 2 3
#     # 2. i = [4,5,6] > 4 5 6
#     for j in i:
#         print(j)

for i in b:
    # 1. i={"username":"郭子", "password":"123456"} j1=username j2=password
    # 2. i={"username":"小玉", "password":"123456"} j1=username j2=password
    for j in i:
        print(j)
        print(i[j])

# 用for循环实现用户登陆: t_user是数据的表
t_user = [{"username":"墩子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
u = input("请输入账号:")
p = input("请输入密码:")
a = 1
for i in t_user:
    print('这是第{}次运行, i的值是{}'.format(a, i))
    if u == i.get("username") and p == i.get("password"):
        print("登陆成功！")
        break  # 终止循环
    else:
        # 最后一次运行都还没有这个账号：再来打印登录失败
        # 怎么来判断是最后一次运行 》 最后一次运行
        if len(t_user) == a:
            print("登陆失败")
    a = a + 1


# 什么算法，怎么实现出来
# a = ["胡", "张", "王", "夏", "张", "李"]，请用python写出a列表中重复元素的下标和值
a = ["胡", "张", "王", "夏", "张", "李"]
for i = range(len(a)):
    if a[i] == a[i+1]:
        print(a[i])
        print(i)


# 排序：
# a = [1,2,3,4,555,333,22211,-1], 请使用python对a列表进行从小到大的排序

# 作业：
# b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
# 输入一个账号和密码，如果b中存在这个账号，那就注册失败，如果b中没有这个账号，就到b里面去添加账号和密码


b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
u = print("请输入注册账号: ")
p = print("请输入注册密码: ")
for i in b:
    if u == i.keys()
    print("账号已存在")








