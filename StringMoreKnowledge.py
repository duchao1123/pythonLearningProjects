"""
====================   字符串常用方法   ====================
"""

str_value = 'abcdefgh'
# print(str_value[::-1])  # hgfedcba
# print(str_value[::-2])  # hfdb
# print(str_value[1::-1])  # ba
# print(str_value[2::-1])  # cba
# print(str_value[3::-1])  # dcba
# print(str_value[3:1:-1])  # dc
# print(str_value[3:6:-1])  # 空: 证明步长为负数时，需要交换开始结束索引
print(str_value[6:3:-2])  # [3:6] defg -> [6:3:-1] gfed -> [6:3:-2] ge


'''
大小写相关
title() 每个单词， 首字母大写
upper() 全大写
lower() 全小写
capitalize() 首字母大写，其他字母小写
casefold()  所有字母小写
swapcase()  所有字母大小写转换
'''
# str_value = 'hello'
# print(str_value.title())  # Hello
# print(str_value.upper())  # HELLO
# str_value = 'HELLO'
# print(str_value.lower())  # hello
# str_value = "hello World"
# print(str_value.capitalize())  # Hello world
# print(str_value.casefold())  # hello world
# print(str_value.swapcase())  # HELLO wORLD
# print('================================')
#
#
# '''
# 左中右对齐
# center(width=width, fillchar=''), 如果width小于等于字符串长度，原字符串输出；如果width大于字符串长度，会剧中显示，左右实用fillchar填充
# ljust(), 左对齐
# rjust(), 右对齐
# zfill(), 左侧用0填充，实际实用：数据报表
# '''
# str_value = 'abc'
# print(str_value.center(10))  #    abc
# print(str_value.center(10, '@'))  # @@@abc@@@@
# print(str_value.ljust(10, '@'))  # abc@@@@@@@
# print(str_value.rjust(10, '@'))  # @@@@@@@abc
# print(str_value.zfill(10))  # 0000000abc
# print('================================')
#
# '''
# 查找
# count 数量; start, end 限制数量范围
# find  查找子字符串索引，从左开始找 ; start, end 限制数量范围; 找不到返回-1
# rfind  查找子字符串索引，从右开始找
# index  类似find， 找不到报错 ValueError: substring not found
# rindex
# '''
# str_value = 'abcdefgahiacccbcdjk'
# print(str_value.count('a'))  # 3
# print(str_value.count('a', 5))  # 2
# print(str_value.count('a', 5, 8))  # 1
# print(str_value.find('bcd'))  # 1
# print(str_value.rfind('bcd'))  # 14
# print(str_value.index('b'))  # 1
# print(str_value.rindex('b'))  # 14
#
#
# '''
# 替换
# expandtabs()  替换tabs占几个空格' '
# replace(x, y, count)  用y替换x，替换count个， 不设置count=-1，全部替换
# translate(table) 转换，根据规则table, table生成
# '''
# # expandtabs(), 找不到合适的例子
#
# str_value = 'aaabbbcccdddeee'
# new_str_value = str_value.replace('a', 'g')
# print(new_str_value)  # gggbbbcccdddeee
# str_value = 'aaabbbcccdddeee'
# new_str_value = str_value.replace('a', 'g', 2)
# print(new_str_value)  # ggabbbcccdddeee
# # print(str_value.replace('d', '1'))  # aaabbbccc, 替换不存在的字符，不会报错，无法替换
#
# # 生成规则table
# table = str.maketrans("a", 'p')
# table1 = str.maketrans("a", 'p', 'b')  # 第三个参数是忽略该字符
# print(table)  # {97: 112} acsill码表值
# print(type(table))  # <oopclass 'dict'>
# str_value = 'aaabbbccc'
# # 根据规则转换字符串
# new_str_value = str_value.translate(table)
# print(new_str_value)  # pppbbbccc
# new_str_value_1 = str_value.translate(table1)
# print(new_str_value_1)  # pppccc
# print('================================')
#
#
# '''
# 判断
# startswith 以啥开头 start, end限制匹配范围
# endswith 以啥结尾
# __contains__ 是否包含
#
# isascii 是否是ascill code
# islower 所有字母小写
# isupper 所有字母大写
# istitle 所有字母，首字母大写
# isalpha 字符串中只有字母
# isspace 字符串是空白字符串 （''、' '、'   '、\n、\t转译等都是空字符串）
# isprintable 字符串中是否所有字符都可以打印，（转译字符不可打印）
# isnumeric 是否是数字（可判断中文，繁体等特殊数字类型）
# isdigit 是否是数字（可判断科学计数等类型）
# isdecimal 是否是数字（判断简单数字）
# isalnum = isalpha or isdecimal or isdigit or isnumeric 有一个返回True, 即返回True
# isidentifier 判断字符串是否是一个python合法的标志符（比如判断变量名是否合理）
#
# '''
# str_value = 'aabccdeefg'
# print(str_value.startswith('a'))  # T
# print(str_value.startswith('aab'))  # T
# print(str_value.endswith('b'))  # F
# print(str_value.endswith('efg'))  # T
# print(str_value.__contains__('hijk'))
#
# # 元组匹配
# print(str_value.startswith(('g', 'h', 'a')))  # True, 只要元组内有匹配的就返回True
# print('================================')
# '''
# 拓展
# 判断字符串是否是python关键字
# '''
# import keyword
# print(keyword.iskeyword('if'))  # True
# print(keyword.iskeyword('str_v'))  # False
#
#
# '''
# 截取
# rstrip(str) 删除右空白, str默认=None，就是删除空格，设置了str可以删除指定字符
# lstrip() 删除左空白
# strip() 删除俩边空白
# removeprefix(val)/removesuffix(val)  移除字符串中指定的前后缀 可能是3.11后的api
# '''
# str_value = ' hello world '
# print(str_value.lstrip())  # 'hello world '
# print(str_value.rstrip())  # ' hello world'
# print(str_value.strip())  # 'hello world'
# print(str_value.lstrip(' hld'))  # 'ello world'
# print(str_value.rstrip(' hld'))  # ' hello wor'
# print(str_value.strip(' hld'))  # 'ello wor'
# # removeprefix / removesuffix 删除指定的前后缀，可能是3.11后的api
# print('================================')
#
#
# '''
# 拆分
# partition  从左到右找到第一个分隔符，切割返回三元组
# rpartition  从右到左
# split   全部切分
# rsplit  从右开始全部切分
# splitlines  按行开始切分; keepends 默认False不保存换行符
# '''
# str_value = 'abcabcabcabc'
# print(str_value.partition('b'))  # ('a', 'b', 'cabcabcabc')
# print(str_value.rpartition('b'))  # ('abcabcabca', 'b', 'c')
#
# str_value = 'abcabcabc'
# print(str_value.split())  # ['aaabbbccc'],
# print(str_value.split('b'))  # ['a', 'ca', 'ca', 'c'], 切割，拆分，按照'b'切割，会移除'b'。 返回结果为字符串列表list
# # 实际使用场景可能为
# data_value = 'name=xiaoming&age=18&weight=120'
# key_value_list = data_value.split('&')
# result_dict = {}
# for kv in key_value_list:
#     kv_list = kv.split('=')
#     result_dict[kv_list[0]] = kv_list[1]
# print(result_dict)
#
# str_value = 'aaaaa\nbbbbb\nccccc'
# print(str_value.splitlines())  # ['aaaaa', 'bbbbb', 'ccccc']
# print('================================')
#
#
# '''
# 拼接
# join A.join(B) 把A插入到B中
# join效率比 + 高
# 原因：
# '''
# str_value = 'abc'
# #  Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs' 官方实例
# print(str_value.join('..'))  # .abc.  A.join(B) 把A插入到B中
# print(str_value.join('123'))  # 1abc2abc3
# print(str_value.join(['1', '2', '3']))  # 1abc2abc3, join的对象可以是list， 返回的是字符串, 但是前提元素是字符串，否则有内置方法代替
# # print(str_value.join([1, 2, 3]))  # TypeError: sequence item 0: expected str instance, int found； list元素必须是字符串
# print(str_value.join(('1', '2', '3')))  # 1abc2abc3，tuple
# print(str_value.join({'1', '2', '3'}))  # 1abc2abc3，set
# print(str_value.join({'1': 1, '2': 2, '3': 3}))  # 1abc2abc3，dict
# print('================================')
#
#
# '''
# 获取长度
# len
# '''
# print(len(str_value))  # 9, str
# print(len([1, 2, 3]))  # 3, list
# print(len((1, 2, 3)))  # 3, tuple
# print(len({1, 2, 3}))  # 3, set
# print(len({1: '1', 2: '2', 3: '3'}))  # 3, dict
#
# '''
# format
# '''
# print('{arg1}{arg2}{arg1}{arg2}'.format(arg1='哈', arg2='呵'))  # 哈呵哈呵

