"""
Matplotlib 库
"""

import matplotlib.pyplot as plt
import numpy as np


def draw_fold_line():
    """
    绘制折线
    :return:
    """
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]

    # 设置样式 (代码位置有要求)
    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    # 设置线宽度
    ax.plot(input_values, squares, linewidth=3)

    # 设置标题
    ax.set_title("Title", fontsize=24)
    # 设置x轴标签，和字体大小
    ax.set_xlabel("xlabel", fontsize=14)
    # 设置y轴标签，和字体大小
    ax.set_ylabel("ylabel", fontsize=20)

    # 设置刻度样式
    ax.tick_params(labelsize=14)

    plt.show()


def draw_line():
    """
    绘制曲线
    :return:
    """
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    fog, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


def print_style():
    print(plt.style.available)


def draw_scatter():
    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    # 绘制点（x, y）s可能是半径？
    ax.scatter(2, 4, s=200)

    ax.set_title('point', fontsize=24)  # encode='utf-8' AttributeError: Text.set() got an unexpected keyword argument 'encode'
    ax.set_xlabel('time', fontsize=14)
    ax.set_xlabel('income', fontsize=14)
    ax.tick_params(labelsize=14)

    plt.show()


def draw_scatters():
    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    # 绘制点（x, y）s可能是半径？
    ax.scatter(x_values, y_values, s=100)

    ax.set_title('point', fontsize=24)  # encode='utf-8' AttributeError: Text.set() got an unexpected keyword argument 'encode'
    ax.set_xlabel('time', fontsize=14)
    ax.set_xlabel('income', fontsize=14)
    ax.tick_params(labelsize=14)

    plt.show()


def draw_scatters_auto():
    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    x_values = range(1000)
    y_values = [value ** 2 for value in x_values]
    # 绘制点（x, y）s可能是半径？
    # color指定固定颜色
    # ax.scatter(x_values, y_values, color=(0, 1, 0), s=10)
    # c颜色渐变依据， cmap=plt.cm.Blues颜色映射值
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

    ax.set_title('point', fontsize=24)  # encode='utf-8' AttributeError: Text.set() got an unexpected keyword argument 'encode'
    ax.set_xlabel('time', fontsize=14)
    ax.set_xlabel('income', fontsize=14)
    ax.tick_params(labelsize=14)

    # 定义刻度格式
    ax.ticklabel_format(style='plain')

    # 设置坐标取值范围
    ax.axis([0, 1100, 0, 1_100_000])

    # plt.show()
    # show 和 save互斥？
    plt.savefig('draw_scatters_auto.png')


"""
练习
1、绘制立方值
2、绘制立方图
"""


def draw_cube():
    # 前五位数
    x_value = range(1, 5001)
    y_value = [value ** 3 for value in x_value]

    plt.style.use('seaborn')
    fog, ax = plt.subplots()
    ax.set_title('cube', fontsize=24, color='red')
    ax.set_xlabel('value', fontsize=14, color='green')
    ax.set_ylabel('value^3', fontsize=14, color='blue')
    ax.ticklabel_format(style='plain')
    ax.tick_params(labelsize=14)

    ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=100)

    plt.savefig("../data/draw_cube", bbox_inches='tight')


draw_cube()






