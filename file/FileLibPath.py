"""
====================   文件操作库pathlib、配合json本地化数据   ====================
"""

from pathlib import Path

'''
获取文件
解析文件
重写文件
'''
data_file = 'testfilelocation/jingyesi.txt'


def create_path(file_path):
    """
    构造path
    :param file_path: 相对路径 or 绝对路径
    :return: path的实例(不论文件是否存在，path都不为空)
    """
    return Path(file_path)


'''
test:
print(create_path(data_file))  # testfilelocation/data.json
print(type(create_path(data_file)))  # <oopclass 'pathlib.PosixPath'>
'''


def exists_file(path):
    """
    判定文件是否存在
    :return: True 存在； False 不存在
    """
    return path.exists()


'''
test:
print(exists_file(create_path(data_file)))  # False
'''


def read_file():
    """
    1、创建path
    """
    path = create_path(data_file)
    '''
    2、判断文件是否存在，否则报错
    FileNotFoundError: [Errno 2] No such file or directory: 'testfilelocation/data.json'    
    '''
    if exists_file(path):
        '''
        3、读取文件，可以不指定编码，默认utf-8
        '''
        contents = path.read_text(encoding='utf-8')
        print(contents)
        print(type(contents))


def write_file(contents):
    """
    1、创建path
    """
    path = create_path(data_file)
    '''
    2、写入内容，如果文件不存在会先创建文件
    '''
    result = path.write_text(contents)
    '''
    3、返回结果
    返回写入字符数量
    '''
    print(f'result = {result}')


'''
test
1、返回结果为：写入字符数量； 文件不存在则先创建文件
write_file('Hello Python')  # result = 12
print(len('Hello Python'))  # 12

2、同一文件，再次write_text，则会覆盖原有内容
write_file('Hello Python')
write_file('Hello World')
read_file()  # Hello World
'''

'''
需求：
添加标点符号
分析：
读出内容，按行分割，奇数行末尾加'，'，偶数行末尾加'。'
'''
str_value = '白日依山尽\n' \
            '黄河入海流\n' \
            '欲穷千里目\n' \
            '更上一层楼\n'


def update_file():
    path = create_path(data_file)
    if exists_file(path):
        contents = path.read_text()
        lines = contents.splitlines()
        print(lines)
        index = 0
        # 练习了下list -> str，感觉不好用，复杂情况可能还得遍历
        # 使用str作为结果会好处理一点, python核心理念：越简单越好
        # result = []
        str_result = ''
        while index < len(lines):
            if (index + 1) % 2 == 1:
                # result.append(lines[index].rstrip() + ',')
                str_result += f'{lines[index].rstrip()},\n'
            else:
                # result.append(lines[index].rstrip() + '.')
                str_result += '%s%s' % (lines[index].rstrip(), '.\n')
            index += 1
        # new_contents = '\n'.join(result)
        # write_file(new_contents)
        write_file(str_result)


write_file(str_value)
update_file()


"""
====================   配合json本地化数据   ====================
"""
'''
需求：保存用户登陆信息，快捷登录
分析：
本地化用户登陆成功的信息
登陆前先去查询是否存在，存在直接登陆，否则的话去录入
'''

import json
login_file = 'testfilelocation/login_info.json'


def login():
    cached = check_login_info_cache()
    if cached:
        print('使用保存信息登陆。')
    else:
        result = do_input()
        if result.get('success'):
            print('登陆成功.')
            save_login_info(result)


def check_login_info_cache():
    path = create_path(login_file)
    if exists_file(path):
        contents = path.read_text()
        info = json.loads(contents)
        print(info)
        print(type(info))
        return True
    return False


def do_input():
    name = input("name: ")
    pwd = input("pwd: ")
    result = {
        'name': name,
        'pwd': pwd,
        'success': True
    }
    return result


def save_login_info(info):
    path = create_path(login_file)
    contents = json.dumps(info)
    writen_count = path.write_text(contents)
    print(writen_count)


login()

