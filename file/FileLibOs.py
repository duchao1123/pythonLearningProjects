"""
====================   文件操作库os  ====================
"""
import os

# 2、创建一个images文件夹
# os.mkdir('images')
# os.mkdir('images/avatar')
#
# # 3、获取当前工作路径（我在哪？）
# print(os.getcwd())
#
# # 4、切换到指定目录
# os.chdir('images/avatar')
# print(os.getcwd())
# # 5、跳出到newProject文件夹（需要从当前路径向上跳2级）
# os.chdir('../../')
# print(os.getcwd())
#
#
# # 6、打印当前目录下的所有文件信息（以列表形式返回）
# print(os.listdir())
#
#
# # 7、删除images目录下的avatar文件夹
# os.rmdir('images/avatar')
# os.rmdir('images')
# print(os.listdir())


# 使用rmtree方法强制删除images文件夹
print(os.getcwd())
# mkdir 不能创建带层级目录
# mkdir 如果存在不能重复创建
if not os.path.exists('images'):
    os.mkdir('images')
if not os.path.exists('images/a'):
    os.mkdir('images/a')
if not os.path.exists('images/a/b'):
    os.mkdir('images/a/b')

# 非空文件不能删除
# OSError: [Errno 66] Directory not empty: 'images'
# os.rmdir('images')

# 按层级删除成功
# os.rmdir('images/a/b')
# os.rmdir('images/a')
# os.rmdir('images')

'''
强制删除 不在乎层级
效果 = rm -rf dir
'''
# import shutil
# shutil.rmtree('images')

# os.chdir('./testfilelocation/images/avatar')
# print(os.listdir())
#
# os.rmdir('images')


'''
删除文件
'''
with open('images/a/b/test.txt', 'w') as f:
    f.write("hahahahha")

# remove
# os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出 OSError
# PermissionError: [Errno 1] Operation not permitted: 'images/a/b'
os.remove('images/a/b/test.txt')

