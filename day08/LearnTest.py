"""
需求：用户输入当前目录下任意文件名，完成对该文件的备份功能(test.txt => 备份文件名为xx[备份]后缀，例如：(test[备份].txt)。

实现思路：
① 接收用户输入的文件名    input()
② 规划备份文件名        规划一下新文件名称 => test.txt => test[备份].txt
③ 备份文件写入数据      把原来的文件内容写入到新文件中
"""

'''
初级版本
'''
# file_name = input("请输入文件路径：")
# # 获取'.'的索引
# index = file_name.rfind('.')
#
# pre_name = file_name[:index]
# pro_name = file_name[index + 1:]
# new_file_name = ''.join([pre_name, '[备份]', '.', pro_name])
#
# # 复制文件内容
# f = open(file_name, 'rb')
# contents = f.read()
# fn = open(new_file_name, 'wb')
# fn.write(contents)
# fn.close()
# f.close()

'''
增强版
健壮性补充：
1、判断输入书否符合文件格式
2、如果文件不存在，提示错误
3、io操作保证安全，进行限制每次读写大小，分段读写
4、文件名拼接方式改进
'''
from pathlib import Path


def find_file():
    while True:
        file_name = input("请输入文件路径：")
        if '.' in file_name and file_name.count('.') == 1:
            path = Path(file_name)
            if path.exists() and path.is_file():  # 判断文件书否存在，不希望使用r模式，拦截抛的异常方式，引入path
                return path
        print("文件名称不合法或文件不存在！")

# # api test
# path = Path('HomeWork.py')
# print(f'stem = {path.stem}', f'name = {path.name}', f'suffix = {path.suffix}', f'suffixes = {path.suffixes}',
#       f'drive = {path.drive}', f'parts = {path.parts}', f'root = {path.root}', f'anchor = {path.anchor}', sep='\n')
# '''
# stem = HomeWork
# name = HomeWork.py
# suffix = .py
# suffixes = ['.py']
# drive =
# parts = ('HomeWork.py',)
# root =
# anchor =
# '''


def copy_file():
    path = find_file()
    old_file = path.name
    new_file = ''.join([path.stem, '[备份]', path.suffix])
    of = open(old_file, 'rb')
    nf = open(new_file, 'wb')

    while True:
        contents = of.read(1024)
        if len(contents) == 0:
            break
        nf.write(contents)

    of.close()
    nf.close()
    print("文件拷贝完成")


copy_file()

