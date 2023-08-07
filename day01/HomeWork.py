"""
================== 课后作业 ==================
"""

'''
## 题目1

### 题干
打印自己的名片。具体信息如下：

- 姓名
- 年龄
- 体重
- 手机号
- 家庭住址
'''
home_work_name = 'duchao'
home_work_age = 30
home_work_weight = 130.5
home_work_phone = '17316290739'
home_work_address = '中国北京'
print(f'我的名字{home_work_name}, 我今年{home_work_age}岁， '
      f'体重是{home_work_weight}斤， 电话号码:{home_work_phone}, '
      f'家庭住址：{home_work_address}')

'''
## 题目2 

### 题干 
按照定义变量的语法要求，定义变量，存储个人信息。 例如：姓名、年龄、体重。
'''
# 小驼峰
myName = 'haha'
# 下划线
my_age = 18
# 加数字
weight_2_me = 120.5

'''
## 题目3 

### 题干
已知用户姓名、年龄、体重数据，要求在控制台格式化输出用户信息，例如：姓名: TOM,  年龄：18。

name = "TOM"
age = 18
weight = 66.6
'''
print('name = %s' % myName, 'age = {}'.format(my_age), f'weight = {weight_2_me}', sep='\n')

'''
## 题目1

### 题干

用户登录系统：用户输入用户名和密码， 并控制台格式化输出用户输入的用户名和密码。
'''
email = input("请输入邮箱：")  # 账号英文忘了...
password = input("请输入密码：")
print(f'email: {email}', end=';\n')
print(f'password: {password}', end=';\n')

'''
## 题目2

### 题干

书写程序，制作一个加法计算器。

用户依次输入2个整数，系统自动进行加法运算，并打印结果。
'''
num1 = int(input("num1: "))
num2 = int(input("num2: "))
print('sum = %d' % (num1 + num2))

'''
## 题目3

### 题干

开发程序：购物车功能。

已知A网站苹果和橘子两种水果单价(具体如下)，用户根据自己的需求输入斤数， 系统计算总价并打印结果。
'''
price = float(input("apple price: "))
weight = float(input("apple weight: "))


def cale_total():
    return price * weight


print("Total is %.2f元" % cale_total())
'''
1. print调用Python中底层的什么方法?
'''
# System.out, 下来百度下..
