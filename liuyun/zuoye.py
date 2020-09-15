# 1. 计算1000之内，偶数的个数  (x % n ==0)
# a = 1
# b = []
# while a <= 100:
#     if a % 2 == 0:
#         b.append(a)
#     a = a + 1
# print(len(b))

# 2. 将一个数组逆序输出 [22,33,1,4,5,6,7]
# a = [22,33,1,4,5,6,7]
# a.sort(reverse=True)
# print(a)

# 3.输入一个整数，判断改整数的因数有哪些？ 4  （2）10 （2/5）
# a = int(input("请输入数字:"))
# b = []
# for i in range(a):
#     if a % (i+1) == 0:
#         b.append(i+1)
# print(b)

# 4.把这个字典中用户名包含“美”字的名字，复制到新的列表中
#  {"username":"乔美丽"，"username2":"刘美丽", "username3"：“郭美丽”：“username3”："username4:"郭然然""}  > 结果为 
#  ["乔美丽", "刘美丽", "郭美丽"]
# a = {"username":"乔美丽","username2":"刘美丽","username3":"郭美丽","username4":"李杨","username5":"郭然然"}
# b = []
# # c = "美"
# for i in a.values():
#     if "美" in i:
#         b.append(i)
# print(b)

# 一个函数有两个参数a、b ，a是列表，b是一个数字，找出a列表中两数之和等于b，打印出这些数

# a=[1,1,2,2,3,3,4,4,5,6,6,7,8,9]
# b=9
# answer=[]
# for x in a:
#     if x<=b/2:
#         y=b-x
#     if y in a :
#         answer.append((x,y))
# print(answer)

# 给你一个包含n个整数的数组a，判断a中是否存在三个元素a,b,c,使得a+b+c=0,请找出满足条件的不重复三元组
# a = [-1,-2,-3,0,1,2,3]
# b = 0
# c = []
# for i in a:
#     if i <= b/3:
#         y = b - i
#         a.remove(i)
#         for x in a:
#             if x <= y:
#                 z = y - x
#                 if z in a:
#                     c.append((i,x,z))
# print(c)

a = [1,2,3,4,5,6,7,8]
for i in a:
    if i < 8:
        a.remove(i)
    print(a)
#         for x in a:
#             b.append(x)
# print(b)








