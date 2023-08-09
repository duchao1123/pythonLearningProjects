import csv
from pathlib import Path


def read_csv(src):
    path = Path(src)
    lines = path.read_text().splitlines()

    # 创建CSV读取器
    reader = csv.reader(lines)

    for var in reader:
        print(var)


if __name__ == "__main__":
    # read_csv("../data/weather_08_2023.csv")
    path = Path("../data/weather_08_2023.csv")
    lines = path.read_text().splitlines()

    # 创建CSV读取器
    reader = csv.reader(lines)

    # 读标题
    title_row = next(reader)

    # 获取要读的列索引
    time_index = title_row.index('DATE')

    for var in reader:
        time = var[time_index]
        print(time)










