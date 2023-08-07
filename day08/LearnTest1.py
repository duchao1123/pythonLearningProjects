"""
案例：把当前项目目录下的python.txt文件，更名为linux.txt，
休眠20s，刷新后，查看效果，然后对这个文件进行删除操作。

目标：
pathlib是3.x后面添加的库，正式运行环境不一定兼容版本
os是低版本兼容的file操作
"""

from pathlib import Path
import os
import time

current_name = 'python.txt'
target_name = 'linux.txt'

# 文件不存在， 报错； 所以第一步需要判断文件是否存在
# FileNotFoundError: [Errno 2] No such file or directory: 'python.txt' -> 'linux.txt'
# os.rename(current_name, target_name)


'''
判断文件是否存在
'''
# os方式: 看起来Path(current_name)锁定了固定的文件，而os可以判定任何文件
is_exists = os.path.exists(current_name)
print(f'{current_name}文件{"存在" if is_exists else "不存在"}')

if not is_exists:
    print("创建文件，写入内容")
    with open(current_name, 'w') as f:
        f.writelines("""
            白日依山尽，
            黄河入海流，
            欲穷千里目，
            更上一层楼。
        """)

'''
重命名
'''
print("写入内容完成，重命名...")
os.rename(current_name, target_name)

time.sleep(10)

path = Path(target_name)
is_exists_by_path = path.exists()
print(f"{current_name} 改名为 {target_name} {'成功' if is_exists_by_path else '失败'}")

if is_exists_by_path:
    time.sleep(10)
    os.remove(target_name)
    print(f'{target_name}文件，删除成功')



