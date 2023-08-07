"""
================== 课后作业 ==================
"""
'''
## 题目1 [加强训练]
### 题干
使用文件操作，向`movie.txt`文件中写入一下内容：

```python
功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥
```
### 训练目标
* 文件的写操作

### 训练提示
* 如何往一个文件里面写入数据
* 写入的数据换行使用什么方法

### 参考方案
* 打开文件`open()`，打开方式为`"w"`
* 写入文件`write()`
* 换行使用`"\n"`
* 也可以使用`""" """`三个引号的形式，可以直接在代码里书写换行

### 操作步骤
* 打开文件，创建对象
* 写入信息
* 关闭文件
'''
# with open('movie.txt', 'w') as f:
#     f.write(
#         """功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥""")

'''
## 题目2 [加强训练]
### 题干
将第一题创建好的文件打开，并读取内容， 要求如下：
* 一次全部读取
* 每次读取一行

### 训练目标
* 文件的读操作

### 训练提示
* 如何读取文件内容？
* 读取全部内容的方法？
* 每次读取一行的方法？

### 参考方案
* 打开文件open，打开方式为“r”
* 读取文件read()
* 读取一行readline()
* 读取所有行readlines()

### 操作步骤
* 打开文件（使用r方式打开，如果不写那么默认是只读方式打开）
* 读取信息
* 关闭文件（每次操作完文件后要关闭文件）
'''
# with open('movie.txt', 'r') as f:
#     print(f.read())
    # print(f.readlines())
    # while True:
    #     content = f.readline()
    #     if len(content) <= 0:
    #         break
    #     print(content)

'''
## 题目3 [加强训练]
### 题干
- 使用os模块创建一个名为“黑马”的文件夹
- 获取黑马文件夹当前所在目录
- 获取当前的目录列表
- 改变文件的操作路径
- 将黑马文件夹删除

### 训练目标
* os模块的使用

### 训练提示
os模块基础命令的使用

### 参考方案
创建文件mkdir

当前所在目录getcwd
当前的目录列表listdir
改变文件的操作路径chdir
删除文件夹rmdir

### 操作步骤
'''
import os
# if not os.path.exists('heima'):
#     os.mkdir('heima')
# print(os.getcwd())
# print(os.listdir())
# os.chdir('heima')
# print(os.getcwd())
# os.chdir('../')
# os.rmdir('heima')

'''
## 题目4 [综合训练1]
### 题干
编写一段代码以完成两份文件之间的相互备份
* 提示用户输入文件名。例：gailun.txt
- 创建以用户输入的名字的文件
- 打开文件写入如下信息
  ​	功夫，周星驰
  ​	一出好戏，黄渤
  ​	我不是药神，徐峥
- 将输入的数据输出到终端上
- 在文件夹中创建gailun副本.txt文件
- 将gailun.txt文件中的数据写入gailun副本.txt文件中
- 打开文件，查看文件中内容

### 训练目标
* 文件的综合使用

### 训练提示
* 每次操作完文件需要关闭
* 在windows系统中注意编码格式问题
* 需要自己重新定义一个新的文件名

### 参考方案

### 操作步骤
* 操作步骤一
  * 提示用户输入文件名
  * 打开文件
  * 写入信息
  * 关闭文件
  * 打开文件
  * 读取文件中的信息
* 操作步骤二
  * 提取文件名的后缀
  * 组建新的文件名
* 操作步骤三
  * 打开新组建的文件名字的文件
  * 写入文步骤一中读取到的信息写入到新的文件中
  * 关闭文件
* 操作步骤四
  * 打开新的文件
  * 读取文件中的内容
  * 关闭文件
'''
# file_name = input("name: ")
# with open(file_name, 'w') as f:
#     f.write("""功夫，周星驰
# 一出好戏，黄渤
# 我不是药神，徐峥""")
#     f.close()
#
#
# from pathlib import Path
# path = Path(file_name)
# pro = path.suffix
# pre = path.stem
# new_name = ''.join([pre, '备份', '.', pro])
# old_file = open(file_name, 'r')
# new_file = open(new_name, 'w')
# while True:
#     content = old_file.read()
#     if len(content) <= 0:
#         break
#     new_file.write(content)
# old_file.close()
# new_file.close()
#
# with open(new_name, 'r') as f:
#     print(f.read())


'''
## 题目5 [综合训练2]

### 题干
- 创建一个新项目中新创建一个名字py文件夹
- 进入py文件夹中创建5个文件，文件名分别为python基础班-1.txt，python基础班-2.txt，python基础班-3.txt，python基础班-4.txt，python基础班-5.txt
- 然后将py文件夹中的所有文件都改名为[黑马]python基础班-1.txt，[黑马]python基础班-2.txt，[黑马]python基础班-3.txt，[黑马]python基础班-4.txt，[黑马]python基础班-5.txt

### 训练目标
* os模块的综合使用

### 训练提示
* 首先创建文件夹，创建文件
* 然后，获取当前文件夹下所有文件
* 最后进行重命名

### 参考方案
* 创建文件夹mkdir
* 进入文件夹中chdir
* 获取文件夹中所有的文件listdir
* 重命名rename

### 操作步骤
* 第一部分
  * 创建文件夹
  * 进入文件夹中
  * 循环遍历创建五个文件，每创建一个后关闭文件
* 第二部分
  * 获取文件夹中所有的文件
  * 遍历获取后的文件，并修改文件名称
'''
# test
# file_name = 'tmp.txt'
# print('='*50)
# print(os.path.abspath(file_name))  # /Users/duchao/PycharmProjects/LearnProject/day08/tmp.txt
# print(os.path.basename(file_name))  # tmp.txt
# print(os.path.dirname(file_name))  # 空
# print(os.path.expanduser(file_name))  # tmp.txt
# print(os.path.expandvars(file_name))  # tmp.txt
# print(os.path.normcase(file_name))  # tmp.txt
# print(os.path.normpath(file_name))  # tmp.txt
# print(os.path.commonpath(file_name))  # 空
# print(os.path.commonprefix(file_name))  # 空

# from pathlib import Path
# import shutil
#
# if os.path.exists('testfiles'):
#     shutil.rmtree('testfiles')
#
# if not os.path.exists('testfiles'):
#     os.mkdir('testfiles')
# os.chdir('testfiles')
# for i in range(5):
#     f = open(f'python-{i}.txt', 'w')
#     f.write(f'file{i}')
#     f.close()
#
# for index, p in enumerate(os.listdir()):
#     if os.path.isfile(p):
#         path = Path(p)
#         path.rename(f'咕咕嘎-{index}')
'''
# 企业面试题
**补充缺失的代码**

提示：
os.path.join() ：可以把两个或多个路径进行拼接，如os.path.join(父路径, 子路径) => 父路径/子目录
os.path.isdir() ：判断其是否为一个文件夹，是返回为True，反之返回为False
函数可能要使用递归操作

```python
def print_directory_contents(sPath):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
```

加深：定义一个函数，功能与print_directory_contents类似，但是要求给所有文件添加层级关系。
① 输入要打印的文件夹名称
② 把里面所有的文件进行遍历输出
+images
+css
+js
​-script.js
-file1.txt
-file2.txt
-file3.txt
> 提示：os.path.join()拼接路径/os.path.isdir()判断是否为文件夹/os.path.isfile()判断是否为文件，这个函数必须要有2个参数（要遍历的路径、默认缩进的空格）
'''
import os


def print_directory_contents(p_arg):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    '''
    思路伪代码：
    if p 是目录：
       获取内容列表，遍历内容列表
          递归调用函数自身 p = 内容路径
       *** 重要！当前目录递归查询完成后，需要返回上一层，才能递归同级其他目录
       返回上一层
    else p 是文件：
       打印路径
    '''
    if not os.path.exists(p_arg):
        return None
    if os.path.isdir(p_arg):
        os.chdir(p_arg)
        for p in os.listdir():
            print_directory_contents(p)
        os.chdir('../')
    else:
        print(os.path.abspath(p_arg))


print_directory_contents('images')




