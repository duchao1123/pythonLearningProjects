from random import choice
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, nums=5000):
        self.nums = nums

        self.x_data = [0]
        self.y_data = [0]

    def do_walk(self):
        while len(self.x_data) < self.nums:

            x_d = choice([-1, 1])
            x_value = choice(range(5))
            x_vector = x_d * x_value

            y_d = choice([-1, 1])
            y_value = choice(range(5))
            y_vector = y_d * y_value

            if x_vector == 0 and y_vector == 0:
                continue

            x = self.x_data[-1] + x_vector
            y = self.y_data[-1] + y_vector

            self.x_data.append(x)
            self.y_data.append(y)


index = 10
while True:
    rw = RandomWalk(int(input("nums = ? ")))
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    rw.do_walk()
    # 突出起始点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(x=rw.x_data, y=rw.y_data, c=range(rw.nums), cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.savefig(f"../data/random_walk-{index}")
    index += 1
    if input("继续 y or n ? ") == 'n':
        break












