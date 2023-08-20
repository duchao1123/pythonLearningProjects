"""
胶囊测试
"""
import re


'''
请使用分组提取所有的电话号码：
'''
def test_02():
    src_list = [
        '2118673676',
        '(211)8673676',
        '211.867.3676',
        '(211)867-3676',
        '211-867-3676',

        '211 867 3676',
        '211 867 3676',
        '211 867 3676',
        '211 867 3676',
        '211 867 3676'
    ]
    result_list = []
    p = '\\(?(\\d{3})[-\\)\\.]?(\\d{3})[.-]?(\\d{4})'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            r_s1 = matched.group(1)
            r_s2 = matched.group(2)
            r_s3 = matched.group(3)
            ymd = f'{r_s1} {r_s2} {r_s3}'
            result_list.append(ymd)

    return result_list



'''
请编写正则表达式匹配下列有重复的数据：
'''
def test_01():
    src_list = [
        'mama',
        'baba',
        'froufrou',
        'barbar',
        'haha',
        'hehe',
        'ohhohh',

        'abcd',
        'abba',
        'gummage',
        'asdhweuir',
        'babb',
        'aa',
        'ccbbdd',
    ]
    result_list = []
    p = '(\\w{2,})\\1'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            result_list.append(matched.group())

    return result_list


'''
编写正则表达式匹配除<p>或</p>之外的所有标签。
'''
def test_0():
    src_list = [
        '<div></div>', '<h1></h1>', '<h2></h2>', '<h3></h3>', '<h4></h4>', '<h5></h5>', '<tr></tr>', '<td></td>',
        '<p></p>', '<p>code</p>', '<p></p><p></p>', '<p></p><p></p>', '<p></p><p></p>', '<p></p><p></p>', '<p></p><p></p>', '<p></p><p>'
    ]
    result_list = []
    p = '<((?!p).+)>.*</\\1>'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            result_list.append(matched.group())

    return result_list



'''
匹配所有XML标签
'''
def test_1():
    src_list = [
        '<city>hello</city>', '<info>haha</info>', '<div>code</div>', '<table>jn</table>',
        '<city>hello</cite>', '<info>haha</inf>', '<div>code</dia>', '<table>jn</tbble>'
    ]
    result_list = []
    p = '<(\\w+)>.+</\\1>'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            result_list.append(matched.group())

    return result_list


'''
实践：提取所有人的生日
'''
def test_2():
    src_list = [
        '张伟 1996.8.24', '王伟 1993年1月2日', '王芳 1997-7-24', '李伟 1996.3.21', '王英 1991.12.1', '李秀 1994-7-5', '李娜 1993年1月6日'
    ]
    result_list = []
    p = '.+\\s(\\d{4}).(\\d{1,2}).(\\d{1,2})'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            r_s1 = matched.group(1)
            r_s2 = matched.group(2)
            r_s3 = matched.group(3)
            ymd = f'{r_s1}-{r_s2}-{r_s3}'
            result_list.append(ymd)

    return result_list


'''
实践：匹配所有的小数
'''
def test_3():
    src_list = [
        '0.1', '3.5', '1.34', '2.56', '1.24', '0.123', '77.87', '192.158', '3.1415926',
        '1', '12', '123', '999', '123456', '12.12.12.', '.12', '.10', '1.1.1.1'
    ]
    result_list = []
    # 以大于1的若干数字开头，包含.，.右边不能有.，以大于1的若干数字结尾
    p = '^\\d+\\.(?!=\\.)\\d+$'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            result_list.append(matched.group())

    return result_list


'''
请使用正则表达式匹配所有两个$符号中的数据。
'''
def test_4():
    src_list = [
        '$$ a = a^2 $$', '$$123$$', '$$ A $$', '$$ a = a^2 $$', '$$123$$', '$$ A = a/$$', '$$ a^{2}+ 3\$$',
        '$$ 9999 $$', '$$ 0987 $$', '$$3\\frac{2}$$',
        'abc$asddadd$$', '$$$ a=b^2 $$', 'abc$asddadd$$', '$asddadd$', '$ b = a ^ 2$', 'abc$ a=b^2 $$abc',
        'abc$$$ a = a**2 $$', '$$$$ a=b^2 $$', 'abc$asddadd$$￥', '$$$a=b^2 $$$$'
    ]
    result_list = []
    # 以大于1的若干数字开头，包含.，.右边不能有.，以大于1的若干数字结尾
    p = '(?<!\\$)\\$\\$[^\\$]+\\$\\$(?!=\\$)'
    print(p)
    for s in src_list:
        matched = re.match(pattern=p, string=s)
        if matched:
            result_list.append(matched.group())

    return result_list


if __name__ == '__main__':
    # print(test_01())
    print(test_02())
    # print(test_0())
    # print(test_1())
    # print(test_2())
    # print(test_3())
    # print(test_4())











