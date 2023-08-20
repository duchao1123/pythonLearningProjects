"""
================== 正则表达式 ==================

导包：import re
api:

re.match(pattern, string, flags=0)          从头开始匹配，返回匹配对象

re.search(pattern, string, flags = 0)       在字符串中找匹配的串，返回第一个匹配到的匹配对象
re.findall(pattern, string, flags=0)        search加强版，返回所有的匹配对象的list
re.finditer(pattern, string, flags=0)       返回一个迭代器，用户可以使用迭代器查看所有匹配对象

re.split(pattern, string, maxsplit=0, flags=0)     使用pattern分割字符串，返回一个结果list


re.compile(pattern, flags=0)                预编译一个正则表达式，返回一个表达式对象 <class 're.Pattern'>
re.purge()                                  清空正则表达式缓存

Pattern#
search(string[, pos[, endpos]])             从Pos处开始查找字符串，返回匹配对象
match(string[, pos[, endpos]])              从Pos处匹配字符串，返回匹配对象
split(string, maxsplit=0)                   同re.split
findall(string[, pos[, endpos]])            从Pos处查找所有匹配的字符串，返回所有匹配对象的list
finditer(string[, pos[, endpos]])           从Pos处查找所有的字符串，返回一个迭代器
sub(repl, string, count=0)                  同re.sub
subn(repl, string, count=0)                 同re.subn


re.sub(pattern, repl, string, count=0, flags=0)    使用repl替换string中pattern匹配到的部分； 这里repl可以是一个函数，参数是匹配对象，返回要替代的串
re.subn(pattern, repl, string, count=0, flags=0)   类似sub，返回元组(new_string, number_of_subs_made)
re.escape(string)                                  将所有的非字母数字字符前加"\"后返回

"""

