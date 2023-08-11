"""
20、接收用户输入的账号和密码，如果账号为'admin'，密码为'admin888'，则提示用户登录成功，其他情况则提示用户名或密码输入错误，只有3次输入机会
"""
try_times = 3

while try_times > 0:
    account = input("请输入账号：")
    password = input("请输入密码：")
    if account == 'admin' and password == 'admin888':
        print("登陆成功")
        break
    else:
        try_times -= 1
        print(f"用户名或密码输入错误, 剩余重试次数:{try_times}")









