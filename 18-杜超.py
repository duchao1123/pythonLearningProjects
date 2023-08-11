"""
18、定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果
例如：列表[1,2,3]，字典{‘a’: 4,‘b’: 5, ‘c’: 6},定义一个函数fun，输出它们的累积结果（1+2+3+4+5+6）
"""


def fun(*args):
    l_p, d_p = args
    sum_list_values = sum(l_p)
    sum_dict_values = sum(list(d_p.values()))
    return sum_list_values + sum_dict_values


if __name__ == "__main__":
    list_param = [1, 2, 3]
    dict_param = {'a': 4, 'b': 5, 'c': 6}
    print(f'result = {fun(list_param, dict_param)}')












