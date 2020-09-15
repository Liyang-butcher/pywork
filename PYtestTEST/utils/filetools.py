#1.保存信息到文件中
def save_file(file_path="./conf/token.txt", token=""):
    with open(file_path, "w") as f:
        f.writelines(token)

#2.读取txt文件
def read_file(file_path="./conf/token.txt"):
    with open(file_path, "r") as f:
        token = f.read()
    return token