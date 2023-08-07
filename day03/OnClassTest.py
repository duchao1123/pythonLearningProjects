"""
================== eval将字符串的值转换为原数据类型 ==================
"""
'''
while循环入门案例：使用while循环，循环输出100遍“老婆大人，我错了”
'''
for i in range(0, 100):
    print(i)


# while 注意要对i进行自增
i = 0
while i < 100:
    print(i)
    i += 1


print('=================================')
'''
案例1：使用while循环求1..100的和
'''
sum_value = 0
i = 1
while i <= 100:
    sum_value += i
    i += 1
print(sum_value)

list_value = [value for value in range(1, 101)]
print(sum(list_value))


print('=================================')
'''
案例1：使用while循环求1..100中所有偶数的和
能被2整除的数就是偶数（整数）  =>  if 数字 % 2 == 0:
2、4、6、8、10...
while循环三步走 + if判断结构
'''
sum_value = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        sum_value += i
    i += 1
print(sum_value)


list_value = list(range(1, 101))
new_list = list(filter(lambda item: item % 2 == 0, list_value))
print(new_list)
print(sum(new_list))


print('=================================')
'''
如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第五个苹果，即是吃苹果的动作停止，
这里就是break控制循环流程，即终止此循环。
'''
i = 0
while True:
    if i <= 10:
        print(i)
    elif 11 <= i <= 20:
        i += 1
        continue
    else:
        break
    i += 1



print('=================================')
'''
需求：计算机从1 ~ 10之间随机生成一个数字，然后提示输入数字，如果我们输入的数字与随机数相等，则提示恭喜你，答对了。
如果输入的数字比随机数大，则提示，猜大了。反之，则提示猜小了，一共有3次机会。
'''
import random

total_times = 3
want_value = random.randint(1, 11)
while total_times > 0:
    result_desc = ''
    guess_value = int(input('请猜：'))
    if want_value == guess_value:
        result_desc = '回答正确'
    elif want_value > guess_value:
        result_desc = '猜小了'
    else:
        result_desc = '猜大了'
    print(result_desc)
    total_times -= 1

if total_times <= 0:
    print('回答错误，没机会了！')


print('=================================')
'''
使用双层循环打印5x5的正方形
外层循环 控制一共有多少行
内层循环 控制每行打印多少个星星（列数）
while
  while
外层循环次数 * 内层循环次数
'''
i, j = 0, 0
while i < 5:
    while j < 5:
        print('*', end='\t')  # 修改end,不去换行
        j += 1
    print()
    i += 1
    j = 0  # 真xx，还原j


print('=================================')
'''
打印直角三角形，一般都是通过while嵌套来实现的
外层循环 ：打印行数
内层循环 ：控制1行显示几颗星星
注意：
第1行，打印1颗
第2行，打印2颗
...
第5行，打印5颗
'''
w = 5
for j in range(1, w + 1):
    print('*' * j)


print('=================================')

i, j = 1, 1
h = 4
while i <= h:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1


print('=================================')
'''
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
while嵌套
外层循环 ：一般都是用于控制行数
内层循环 ：一般都是用于控制列数（星星数）
第1行，显示5颗
第2行，显示4颗
第3行，显示3颗
...
第5行，显示1颗
'''
i, j = 5, 5
while i > 0:
    j = i
    while j > 0:
        print('*', end=' ')
        j -= 1
    print()
    i -= 1


print('=================================')
'''
① 打印直角三角形
② 把直角三角形中的小星星替换为9x9乘法表公式
'''
i, j = 1, 1

while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    print()
    i += 1


print('=================================')
'''
for 临时变量 in 数据序列（字符串/列表/元组/字典/集合）:
    循环体代码
    每次循环时，系统会自动将序列中的元素放入临时变量中，序列中有多少个元素，则整个循环会自动执行多少次

例如：有一个字符串str1 = 'hello'
for i in str1:
    print(i)
    # 由于hello一共有5个字符，所以本循环一共循环5次
    # 第一次循环，获取hello中的h字符放入变量i中，然后print(i)打印h
    # 第二次循环，获取hello中的e字符放入变量i中，然后print(i)打印e
    # 第三次循环，获取hello中的l字符放入变量i中，然后print(i)打印l
    # 第四次循环，获取hello中的l字符放入变量i中，然后print(i)打印l
    # 第五次循环，获取hello中的o字符放入变量i中，然后print(i)打印o
'''
str_value = 'abcde'
for char_v in str_value:
    print(char_v)


print('=================================')
'''
案例：用for循环实现用户登录
① 输入用户名和密码
② 判断用户名和密码是否正确（username='admin'，password='admin888'）
③ 登录仅有三次机会，超过3次会报错

分析：用户登陆情况有3种:
① 用户名错误(此时便无需判断密码是否正确)  -- 登陆失败
② 用户名正确 密码错误 --登陆失败
③ 用户名正确 密码正确 --登陆成功

扩展：每次登录失败时，都弹出提示，您还剩下几次登录机会
'''


def input_and_check():
    name = input("请输入用户名：")
    pwd = input('请输入密码：')
    return name == 'admin' and pwd == '888'


for time in range(1, 4):  # 1, 2, 3
    login_success = input_and_check()
    if login_success:
        print('登陆成功')
        break
    elif time < 3:
        print(f'登陆失败, 还剩{3 - time}次')
    else:
        print('登陆失败, 稍后再试')


print('=================================')
'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
外层循环控制行数
内层循环控制列数
range(start, stop)
'''
for i in range(1, 6):
    print("* " * i)


print('=================================')
'''
99乘法表
外层循环控制行数
内层循环控制列数
range(start, stop)
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()







