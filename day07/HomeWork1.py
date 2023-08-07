"""
# 每日必会题
##
 书写学生管理系统中的界面展示部分
 书写学生管理系统中的添加学生信息接口add_new_info()并添加循环控制逻辑
 书写学生管理系统中的删除信息的接口del_info()并补充循环控制逻辑
 书写学生管理系统中的修改学生信息的接口modify_info(), 并在循环控制模块中添加器修改信息的接口
 书写学生管理系统中的查询学生信息的接口search_info(), 并在循环控制模块中添加查询信息的接口
 书写学生管理系统中的遍历学生信息的接口print_all_info(), 并在循环控制模块中添加遍历学生信息的接口及退出功能
"""
from pathlib import Path
import os

# 学生列表
students = []
# 自增学号
increment_no = 1


# 添加学生
def add_new_info():
    global students
    global increment_no
    student = {'name': input("请输入学生名字："),
               'age': int(input('请输入学生年纪：')),
               'no': str(increment_no).zfill(4)}
    students.append(student)
    increment_no += 1
    print('添加完成')


# 删除学生
def del_info():
    student_no = input('请输入学号学号：')
    global students
    for student in students:
        if student['no'] == student_no:
            students.remove(student)
            print('删除完成')
            break
    else:
        print('不存在此学生')


# 搜索学生信息
def search_info():
    student_no = input('请输入学号学号：')
    global students
    for student in students:
        if student['no'] == student_no:
            print('查询成功')
            print(student)
            break
    else:
        print('不存在此学生')


# 修改学生信息
def modify_info():
    student_no = input('请输入学号学号：')
    global students
    for student in students:
        if student['no'] == student_no:
            print(student)
            student['name'] = input('请输入学生名字：')
            student['age'] = input('请输入学生年纪：')
            print('修改成功')
            break
    else:
        print('不存在此学生')


# 打印全部学生信息
def print_all_info():
    global students
    if len(students) <= 0:
        print('没有学生数据')
        return None
    print('name'.center(12), 'age'.center(12), 'no'.center(12), sep='|')
    for student in students:
        print(f'{str(student["name"]).center(12)}',
              f'{str(student["age"]).center(12)}',
              f'{str(student["no"]).center(12)}', sep='|')


'''
需求增强：
1、需要把录入学生保存到本地
2、每次启动时导入到内存
3、添加清除的功能：清空内存和缓存
分析：序列化数据
'''
data_file = 'students.txt'


def save_2_disk():
    global students
    global students
    if len(students) > 0:
        with open(data_file, 'w') as f:  # 每次都是完整的students列表，所以是用'w'
            f.write(f'{str(students)};{increment_no}')


def load_from_disk():
    path = Path(data_file)
    if path.exists() and path.is_file():
        global students
        global increment_no
        with open(data_file, 'r') as f:
            contents = f.read()
            if len(contents) > 0:
                data = contents.split(';')
                increment_no = eval(data[1])
                students = eval(data[0])  # 读出的内容为字符串包裹的列表，直接eval


def clear():
    global students
    global increment_no
    students.clear()
    increment_no = 1
    if os.path.exists(data_file):
        os.remove(data_file)
    print('清除完成')


def startup():
    load_from_disk()
    while True:
        print("""
            支持操作如下：
        【0】：新增学生
        【1】：删除学生
        【2】：搜索学生
        【3】：编辑学生信息
        【4】：打印所有学生信息
        【8】：清除数据
        【9】：退出
        """)
        select_option = input("请选择操作：")
        if not select_option.isdigit():
            print("请正确选择！")
            continue
        option = int(select_option)
        if option == 9:
            # 关闭前，保存
            save_2_disk()
            print('谢谢使用')
            break
        elif option == 0:
            add_new_info()
        elif option == 1:
            del_info()
        elif option == 2:
            search_info()
        elif option == 3:
            modify_info()
        elif option == 4:
            print_all_info()
        elif option == 8:
            clear()
        else:
            print("请正确选择！")


# 启动程序
startup()




















