from src.die import Die
import plotly.express as px


if __name__ == "__main__":
    d1 = Die()
    d2 = Die()
    results = []

    for roll_num in range(1000):
        result = d1.roll() + d2.roll()
        results.append(result)

    print(results)

    frequencies = []
    max_result = d1.num_sides + d2.num_sides
    poss_results = range(2, max_result + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    print(frequencies)

    title = "掷骰子"
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    # 简易版
    # fig = px.bar(x=poss_results, y=frequencies)
    # 定制表头版
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    # x轴为每组数据设置label
    fig.update_layout(xaxis_dtick=1)
    # 展示结果表
    # fig.show()
    # 保持结果为html
    fig.write_html('../data/result.html')









