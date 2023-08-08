import matplotlib.pyplot as plt


def draw_line00():
    squares = [1, 4, 9, 16, 25]
    fig, ax = plt.subplots()
    ax.plot(squares)
    # plt.show()
    plt.savefig('../data/draw_line00.png', bbox_inches='tight')


def draw_line01():
    squares = [1, 4, 9, 16, 25]
    fig, ax = plt.subplots()
    ax.plot(squares, linewidth=3)
    ax.set_title("squares of value", fontsize=24)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squares", fontsize=14)
    ax.tick_params(labelsize=14)
    # plt.show()
    plt.savefig('../data/draw_line01.png', bbox_inches='tight')


def draw_line02():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)
    ax.set_title("squares of value", fontsize=24)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squares", fontsize=14)
    ax.tick_params(labelsize=14)
    # plt.show()
    plt.savefig('../data/draw_line02.png', bbox_inches='tight')


def draw_line03():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)
    ax.set_title("squares of value", fontsize=24)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squares", fontsize=14)
    ax.tick_params(labelsize=14)
    # plt.show()
    plt.savefig('../data/draw_line03.png', bbox_inches='tight')


def draw_point00():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(2, 4)
    # plt.show()
    plt.savefig('../data/draw_point00.png', bbox_inches='tight')


def draw_point01():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(2, 4, s=200)
    ax.set_title("squares of value", fontsize=24)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squares", fontsize=14)
    ax.tick_params(labelsize=14)
    # plt.show()
    plt.savefig('../data/draw_point01.png', bbox_inches='tight')


def draw_point02():
    x_values = [value for value in range(1, 6)]
    y_values = [value ** 2 for value in range(1, 6)]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, s=100)
    ax.set_title("squares of value", fontsize=24)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squares", fontsize=14)
    ax.tick_params(labelsize=14)
    # plt.show()
    plt.savefig('../data/draw_point02.png', bbox_inches='tight')


def draw_point03():
    x_values = range(1, 1001)
    y_values = [value ** 2 for value in x_values]
    print(y_values[:10])

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    # ax.scatter(x_values, y_values, color='red', s=10)
    # ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
    ax.set_title("squares of value", fontsize=24)
    ax.set_xlabel("value", fontsize=14)
    ax.set_ylabel("squares", fontsize=14)
    ax.tick_params(labelsize=14)

    ax.axis([0, 1100, 0, 1_100_000])
    ax.ticklabel_format(style='plain')

    # plt.show()
    plt.savefig('../data/draw_point03.png', bbox_inches='tight')


draw_line00()
draw_line01()
draw_line02()
draw_line03()
draw_point00()
draw_point01()
draw_point02()
draw_point03()

