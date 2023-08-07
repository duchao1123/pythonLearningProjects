"""
====================   文件基础操作  ====================
"""

'''
打开文件
open(filename, mode, encoding'):  filename: 相对路径 or 绝对路径； mode打开模式; 
r  只读 
rb 读二进制文件
w  先清除再写入
wb 二进制写
a  末尾拼接写入
a+ 可读写模式，末尾追加
w+ 可读写，先清理在写入
r+ 可读写，可以写到文件任意位置

操作文件
关闭文件: close()
上下文: with
'''

'''
打开文件
'''
# 以读的方式打开文件，如果文件不存在，会报错
# FileNotFoundError: [Errno 2] No such file or directory: 'xxxxx'
# open("./testfilelocation/basic_test.txt", 'r', encoding='utf-8')

# 以写的方式打开文件，如果文件不存在，会创建文件
# open("./testfilelocation/basic_test.txt", 'w', encoding='utf-8')
# open("./testfilelocation/basic_test.txt", 'w')  # 默认编码utf-8

f = open("./testfilelocation/basic_test.txt", 'w')
print(f'type = {type(f)}, name = {f.name}, mode = {f.mode}, encoding = {f.encoding}')
# type = <oopclass '_io.TextIOWrapper'>, name = ./testfilelocation/basic_test.txt, mode = w, encoding = UTF-8
print("=" * 40)

'''
写
'''
f.write("hello python!")
# 不会换行
f.write("hello python， hello ai!")
# 写入多行，也不会换行
f.writelines("i am dc")
# 换行使用\n
f.write("aaaaa\nbbbbbb\ncccccc")

# 不执行close不会进行保存
f.close()

# flush即时写入，不必等close
f = open("./testfilelocation/basic_test.txt", 'w')
f.write("嘎嘎嘎")
f.flush()

'''
读
'''
f = open("./testfilelocation/basic_test.txt", 'r')
content = f.read()
# type = <oopclass 'str'>, content = hello python!hello python， hello ai!iamdc
print(f'type = {type(content)}, content = {content}')
# 虽然读不存在不close，无法写入的问题，但是io操作，一定是闭环的
f.close()
print("=" * 40)


f = open("./testfilelocation/basic_test.txt", 'r')
# 读取文件一行，文件指针向下移动
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
# 读不到不会报错
print(f.readline())
f.close()

'''
设置文件指针
seek
'''

f = open("./testfilelocation/basic_test_1.txt", 'w')
f.writelines("01234567890\nabcdefghijk\n============")
f.close()

f = open('./testfilelocation/basic_test_1.txt', 'r')
print(f.readline())  # 01234567890\n
print(f.tell())  # 当前文件指针在索引12
print(f.seek(0))  # 充值文件指针
print(f.tell())  # 当前文件指针在0
print(f.readline())  # 再次打印，根据指针位置仍然打印第一行
# 主动移动文件指针到25，期望打印 '============'
f.seek(25)
print(f.readline())  # ===========

f.close()
















