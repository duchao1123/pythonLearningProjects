"""
正则基础
"""
import re

'''
字符组[]
'''
# 请你使用字符组匹配Java和 java
def strg():
    for s in ['Java8.0', 'java8.0']:
        result = re.match(pattern='[Jj]ava', string=s)
        print(result.group())
    print('-'*20)

'''
区间
要匹配任意数字可以使用[0-9]；
如果想要匹配所有小写字母，可以写成[a-z]；
想要匹配所有大写字母可以写成[A-Z]

匹配字母
'''
# 匹配数据所有的数字、小写字母和大写字母
def match_all():
    for s in ['abcdefg', '012345678', '987654321', 'ABCDEFG']:
        result = re.match(pattern='[a-zA-Z0-9]+', string=s)
        print(result.group())
    print('-' * 20)

'''
匹配特殊字符
使用 \ 就可以进行对特殊符号进行转义
'''
# 匹配下列符号
def match_spa_f():
    for s in ['[]', '-----', '--', '()']:
        result = re.match(pattern='[\\[\\]\\-+\\(\\)]+', string=s)
        print(result.group())
    print('-' * 20)

'''
取反
开头使用 ^ 字符实现取反
'''
# 匹配爱后面不包含你的数据
def get_fa():
    for s in ['爱吗', '爱你', '爱我自己', '不爱你', '我爱我', '爱你一万年']:
        result = re.match(pattern='.*爱[^你].*', string=s)
        if result:
            print(result.group())
    print('-' * 20)


'''
快捷匹配数字和字母
\\w	与任意单词字符匹配，任意单词字符表示 [A-Z]、 [a-z]、[0-9]、_
\\d	与任意数字匹配
'''
# 使用快捷方式匹配下面的单词。
def match_words():
    for s in [
        'master',
        'code',
        '=-',
        '/*-',
        '987654321',
        '0123',
        '$#$%',
        'JIAONANG',
        '<>()',
        'python'
    ]:
        result = re.match(pattern='[\\w]+', string=s)
        if result:
            print(result.group())
    print('-' * 20)

'''
匹配空白
\\s快捷方式可以匹配空白字符，比如空格，tab、换行
'''
# 匹配空白分隔的单词
def match_space():
    for s in [
        'code',
        'code jiaonang',
        'code www',
        'CODEINFO',
        'codeasd/',
        'codejiaonangA$',
        'CO DEJIAONANG'
    ]:
        result = re.match(pattern='code\\s.*', string=s)
        if result:
            print(result.group())
    print('-' * 20)


'''
单词边界
\\b 匹配的是单词的边界
'''
# 快捷方式匹配下列数据
def word_side():
    for s in [
        'code',
        'code jiaonang',
        'code.jiaonang',
        'www.code',
        'code-jiaonang',
        'CODEINFO',
        'codeasd/',
        'codejiaonangA$',
        'JIAONANG-MASTER',
        'CODEJIAONANG!'
    ]:
        result = re.match(pattern='\\bcode\\b', string=s)
        print(result.group())
    print('-' * 20)

'''
快捷取反
\\W
\\D
\\S
'''
# 匹配下列开头不以字母开头的单词
def word_side():
    for s in [
        'master',
        '¥¥master',
        '$codejiaonang',
        'python',
        'code-jiaonang',
        '-java',
        'codeasd',
        'codejiaonangA$',
        '*ruby'
    ]:
        result = re.match(pattern='^[^\\w]+\\w+', string=s)
        if result:
            print(result.group())
    print('-' * 20)

'''
开始和结束
^指定的是一个字符串的开始，$指定的是一个字符串的结束
任意字符
.字符只有一个不能匹配的字符，也就是换行符（\n）
可选字符
使用 ? 符号指定一个字符、字符组或其他基本单元可选，这意味着正则表达式引擎将会期望该字符出现零次或一次
'''
# 匹配codejiaonang的不同写法
def match_code():
    for s in [
        'codejiaonang',
        'code.jiaonang',
        'code - jiaonang',
        '(code)jiaonang',
        'code(jiaonang)',
        'code jiaonang'
    ]:
        result = re.match(pattern='[\\W]?code[\\W]?jiaonang', string=s)
        if result:
            print(result.group())
    print('-' * 20)

'''
重复
在一个字符组后加上{N} 就可以表示在它之前的字符组出现N次
重复区间
{M,N}，M是下界而N是上界
开闭区间
{M,}
速写
*： 0～
+： 1～
'''
# 匹配以 http开头，以/结尾的所有数据。
def match_code():
    for s in [
        'https://code.com/',
        'http://codejn/',
        'http://google.com/',
        'https://codejn/',
        'https://google.com/'
    ]:
        result = re.match(pattern='^http.*/$', string=s)
        print(result.group())
    print('-' * 20)

'''
分组 ()
使用() 获得整个匹配。还能够在匹配中选择每一个分组。见回溯
'''
# 分组提取 hi
def test_group():
    str_v = '<div>hi</div>'
    p = '<div>(.*?)</div>'
    print(p)
    result = re.match(pattern=p, string=str_v)
    if result:
        print(result)
    print('-' * 20)



'''
分组或  ｜
可以在各个后缀名之间加上一个 | 符号
'''
# 视频文件的后缀名有 .mp4、.avi、.wmv、.rmvb
# 请编写正则表达式提取所有的视频文件的后缀
def test_group_or():
    src_list = [
        '1.avi',
        'abc.mp4',
        'chapter1.wmv',
        'chapter2.rmvb'
    ]
    result_list = []
    p = '.+(.avi|.mp4|.wmv|.rmvb)'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)
    print('-' * 20)


'''
非捕获分组
(?:表达式):  不捕获数据，还能使用分组的功能
'''
# 提取目标数据中的电话号码 75855
def test_group_nf():
    src_list = [
        '01-75855',
        '0731-75855',
        '12345-75855',
        'tel:75855'
    ]
    result_list = []
    p = '.+(\\d{5})'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)
    print('-' * 20)


'''
分组的回溯引用
https://codejiaonang.com/#/course/regex_chapter2/0/8

使用\\N可以引用编号为N的分组
'''
# 接下来请你编写代码匹配符合 ab ba 这种关系的单词
def test_group_hs():
    src_list = [
        'abccba',
        'allagmatic',
        'otto',
        'abba',
        'asffs',
        'maam',
        'warrandice',

        'aaruria',
        'bluted',
        'cffusive',
        'dusoid',
        'eesthophysiology',
        'fmphimictical',
        'ccritan'
    ]
    result_list = []
    p = '.*(.{1,})(.{1,})(\\2)(\\1).*'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)
    print('-' * 20)


'''
正向先行断言
https://codejiaonang.com/#/course/regex_chapter2/1/0

位置(?=表达式)：表示所在位置右侧必须能匹配表达式
'''
# 现在请你编写正则表达式进行密码强度的验证，规则如下：
# 至少一个大写字母
# 至少一个小写字母
# 至少一个数字
# 至少8个字符
def test_zxxxdy():
    src_list = [
        'Admin123456', 'pZUJLUpTL2','Tnut2eWPN1','wJxpVhVYi3','UySRo49ps','Ig7AHzZ0J','oYHMDdHCK9','yiyWKQnWo2','gTZEEkVrj1','8Ij12340as','wdfqe#wefDdf444','Codejiaonang123','CodeJiaonang@qq1','111111abc11ABc','CodeJiaonang123',
        'qwe','8848','123456','asd123','Adm123','Asd123','wjleif932','admin123','123admin','123asd123','ADMIN123()','编号89757','888888888info','masterxiao123','888888888A'
    ]
    result_list = []
    p = '(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\\d).{8,}'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)
    print('-' * 20)



'''
反向先行断言
https://codejiaonang.com/#/course/regex_chapter2/1/1

位置(?!表达式)：表示保证右边不能出现某字符
'''
# 编写正则表达式匹配不是qq邮箱的数据。
def test_fxxxdy():
    src_list = [
        'abc@sina.com',
        'qq@163.com',
        'a@google.com',
        'qq@123.com',

        'test@qq.com',
        'qq@qq.com',
        'gc@qq.com',
        '163@qq.com'
    ]
    result_list = []
    p = '.+@(?!qq.com).+'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)
    print('-' * 20)


'''
正向后行断言
https://codejiaonang.com/#/course/regex_chapter2/2/0

(?<=表达式)位置：表示所在位置左侧必须能匹配表达式
'''
# 使用正则表达式匹配匹配王姓同学的名字
def test_zxhxdy():
    src_list = [
        '王芳',
        '王芳芳',
        '芳芳 王菲',
        '菲菲 王菲菲',
        '王五',

        '张三',
        '李四 小王',
        '富贵',
        '二麻子',
        '大王'
    ]
    result_list = []
    p = '.*(?<=王).+'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)
    print('-' * 20)


'''
反向后行断言
https://codejiaonang.com/#/course/regex_chapter2/2/1

(?<!表达式)位置： 所在位置左侧不能匹配表达式
'''
# 匹配一个美元符号中的数据
def test_fxhxdy():
    src_list = [
        '$ a = a^2 $',
        '$123$',
        '$ A = a / b + b $',
        '$ a = a^2 $',
        '$123$',
        '$ A = a / b + b $',
        '$ a^{2}+ 3\\frac{2}{3} $',
        '$ a**N&123% $',

        'abc$asddadd$$',
        '$$$ a=b^2 $$',
        'abc$asddadd$$',
        'abc$ a=b^2 $$abc',
        'abc$$ a = a**2 $$',
        '$$ a=b^2 $$',
        'abc$asddadd$$',
        '$$$ a=b^2 $$$$'
    ]
    result_list = []
    p = '^\\$(?!=\\$).+(?<!\\$)\\$$'
    print(p)
    for s in src_list:
        result = re.match(pattern=p, string=s)
        if result:
            result_list.append(result.group())
    print(result_list)


if __name__ == '__main__':
    strg()
    match_all()
    match_spa_f()
    get_fa()
    match_words()
    match_space()
    word_side()
    match_code()
    test_group()
    test_group_or()
    test_group_nf()
    test_group_hs()
    test_zxxxdy()
    test_fxxxdy()
    test_zxhxdy()
    test_fxhxdy()





