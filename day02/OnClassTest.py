"""
================== eval将字符串的值转换为原数据类型 ==================
"""
int_str = '10'
float_str = '3.14'
bool_str = 'True'
list_str = '[1, 2, 3]'
tuple_str = '(1, 2, 3)'
set_str = '{1, 2, 3}'
dict_str = "{'name': 'key', 'age': '18'}"
str_str = 'aaa'

# 如果明确知道字符串的原始数据类型，可以直接强转
print(int(int_str))


# 但是如果不确定，强转就可能出现错误
# print(int(str_str))  # ValueError: invalid literal for int() with base 10: 'aaa'

# string 的 eval方法可以用于判断原始数据类型


def print_eval(no_case_str):
    print(type(eval(no_case_str)))


print_eval(int_str)
print_eval(float_str)
print_eval(bool_str)
print_eval(list_str)
print_eval(tuple_str)
print_eval(set_str)
print_eval(dict_str)

'''
eval()函数常见作用有： 
1、计算字符串中有效的表达式，并返回结果
2、将字符串转成相应的对象（如list、tuple、dict和string之间的转换）
3、将利用反引号转换的字符串再反转回对象
'''
# 1、计算字符串中有效的表达式，并返回结果
print('1 + 1')  # 1 + 1
print(eval('1 + 1'))  # 2
print('pow(1, 1)')  # pow(1, 1)
pow(1, 1)
print(eval('pow(1, 1)'))  # 1
'''
# string 自身不能eval?
# print_eval(str_str)  # NameError: name 'aaa' is not defined
# 解释：eval的原理就是去掉""，然后执行里面内容
str_str = 'aaa'  -> aaa
aaa此时解释器认为它是变量，所以执行aaa, 发现变量没有定义'aaa' is not defined， 报错
'''

# 2、将字符串转成相应的对象（如list、tuple、dict和string之间的转换）
list_eval_str = '[1, 2, 3]'


def eval_and_sum():
    # 转为list，参与逻辑
    origin_l = eval(list_eval_str)
    result = 0
    # 1
    # index 0 value = 1
    print(f'index 0 value = {origin_l[0]}')
    # <oopclass 'list'>
    print(type(origin_l))
    for v in origin_l:
        result += v
    print(f'sum = {result}')


eval_and_sum()

# 3、将利用反引号转换的字符串再反转回对象
list_value = [1, 2, 3]
list_value_str = str(list_value)
print(list_value_str)  # [1, 2, 3]
print(type(list_value_str))  # <oopclass 'str'>


def eval_and_get():
    set_local_value = eval(list_value_str)
    print(type(set_local_value))  # <oopclass 'list'>
    print(set_local_value[0])  # 1


eval_and_get()

print('======================================================')
"""
================== 数据类型转换 ==================
"""
# float可以转为int，但是会丢失精度，小数点后面被丢弃
float_value = 3.1415
print(int(float_value))

# int转为float，增加.0
int_value = 10
print(float(int_value))

print('======================================================')
"""
================== 运算符 ==================
"""

'''
+ - * /
// 除法取整 （整除）
% 取余
** 幂次运算
注意： / 除法运算结果强制浮点型
注意：幂次计算优先级高于* /
比如
2 * 3 ** 2 =  2乘3的平方，先算平方，再乘除
'''

# / 除
print(5 / 2)  # 2.5
print(4 / 2)  # 2.0
# // 整除
print(5 // 2)  # 2
# % 取余
print(5 % 2)  # 1
# ** 幂次
print(3 ** 2)  # 9

# 运算优先级
print(1 + 2 * 3 ** 2)  # 19
'''
step0、3 ** 2 = 9
step1、2 * 9 = 18
step2、1 + 18 = 19
'''

print('======================================================')
"""
================== 多个变量同时赋值: 元组拆包 ==================
"""
int_v, float_v, str_v, bool_v = 1, 1.1, 'aaa', True
int_v1, list_v, tuple_v, set_v, dict_v \
    = 1, [1, 2], (1, 2, 3), {1, 2}, {'name': 'key', 'age': 18}

# 基本用法
someone = ('xiaoming', 18, '女', 90)
name, age, sex, weight = someone
print(f'name = {name}, age = {age}')

# 交换变量值
x = 10
y = 5
x, y = y, x
'''
in java:
int x = 10;
int y = 5;
int tmp;
void swap() {
    tmp = x;
    x = y;
    y = tmp;
}
'''

print('======================================================')
"""
================== 字符串大小比较 ==================
"""
print(1 == '1')  # python没有全等和非全等的概念， 不同类型可以比较，但一定不等

# 字符串之间可以进行比较运算
print('3' > '2')  # True
print('3.2' > '2')  # True
print('20' > '3')  # False, 按位比较
print('ABC' > 'BCD')  # False A = 65 B = 66
print('ABC' > 'ACD')  # False A = 65 B = 66 C = 67

'''
ASCII 一共127位， 代表127个常用字符
规则：数字 < 大写字母 < 小写字母 < 汉字（GBK）
GBK：国标扩展码
unicode: 万国码，包含大部分国家语言，符号，表情等, 包含utf-8, utf-16
'''

print('======================================================')
"""
================== 逻辑运算符 ==================
"""
'''
and 与: 全真才真
or  或: 全假才假
not 非: 非真即假，非假即真
'''
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or False)  # False

print(not True)  # False
print(not False)  # True

print('======================================================')
"""
================== 三元/三目运算符 ==================
"""
int_a = 10
int_b = 20
max_int = int_a if int_value > int_b else int_b
print(max_int)
print(int_a)

# 元组基础
int_c = 30
tuple_v = (int_a, int_b, int_c)
index = int_a < int_b
print(type(index))

# 2个元素的元组，索引为0，1；bool值 False = 0； True = 1， 所以使用比较结果bool，代替索引，获取元组结果
print((int_a, int_b)[int_a < int_b])
# 类似的字典，也可以使用bool作为key，比较结果获取字典值

# lambda 注意后面的（）相当于invoke method
print((lambda: int_a, lambda: int_b)[int_a < int_b]())

# 三元运算符选择执行操作


def get_min(a, b):
    return min(a, b)


def get_max(a, b):
    return max(a, b)


a, b = 3, 4
select_type = int(input("请选择(0：min，1：max)："))
result = get_min(a, b) if select_type == 0 else get_max(a, b)
print(f'result = {result}')

