import pickle


def load_from_plk(src: str, load_times=1):
    """
    从plk二进制序列化文件中读取数据
    :param src: 文件
    :param load_times: load次数，取决于dump次数
    :return: 无指定数据类型数据元组，调用者进行强转
    """
    result = []
    with open(src, 'rb') as f:
        for i in range(load_times):
            result.append(pickle.load(f))
    return tuple(result)


def dump_2_plk(dst: str, *args, **kwargs):
    """
    将数据序列化写入文件
    :param dst: 目标文件
    :param args: 动态参数
    :param kwargs: 字典参数
    :return: 返回dump次数，用于读取
    """
    with open(dst, 'wb') as f:
        for arg in args:
            pickle.dump(arg, f)
        pickle.dump(kwargs, f)
    return len(args) + (1 if len(kwargs) > 0 else 0)


def loads_from_plk(src: str):
    """
    针对单个数据使用：从plk二进制序列化文件中读取数据
    :param src: 文件
    :return: 无指定数据类型数据元组
    """
    with open(src, 'rb') as f:
        content = f.read()
        return pickle.loads(content)


def dumps_2_plk(dst: str, obj):
    """
    将数据序列化写入文件
    :param obj:
    :param dst: 目标文件
    :return: 返回dump次数，用于读取
    """
    with open(dst, 'wb') as f:
        bytes_content = pickle.dumps(obj)
        f.write(bytes_content)


if __name__ == "__main__":
    f_n = '../data/students.plk'
    int_value = 10
    str_value = "学校"
    tuple_value = (1, 2, 3)
    dict_value = {"name": 'xiaoming', "age": 18, "no": "20230001"}
    times = dump_2_plk(f_n, int_value, str_value, tuple_value, dict_value)
    int_value, str_value, tuple_value, dict_value = load_from_plk(f_n, times)
    print(int_value)
    print(str_value)
    print(tuple_value)
    print(dict_value)

    f_n1 = '../data/students1.plk'
    dict_value = {"name": 'xiaoming', "age": 18, "no": "20230001"}
    dumps_2_plk(f_n1, dict_value)
    new_dict_value = loads_from_plk(f_n1)
    print(new_dict_value)










