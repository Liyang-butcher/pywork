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
















