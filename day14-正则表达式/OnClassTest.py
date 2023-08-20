import re


def api_test(*, p, src_str, fs) -> str or None:

    '''
    生成一个（定义好规则的）正则对象
    def compile(pattern: Pattern[AnyStr],
            flags: Union[int, RegexFlag] = ...) -> Pattern[AnyStr]

    compile(pattern: Pattern[AnyStr], flags: Union[int, RegexFlag]=...)
    compile(pattern: AnyStr, flags: Union[int, RegexFlag]=...)
    '''
    p_o = re.compile(pattern=p, flags=fs)
    print(type(p_o))  # <class 're.Pattern'>
    print(p_o)  # re.compile('o')

    '''
    匹配Pattern，执行正则
    def sub(self,
        repl: AnyStr,
        string: AnyStr,
        count: int = ...) -> AnyStr
    repl： 替换为字符串
    string: 原字符串
    count: 替换数量
    '''
    result_str = p_o.sub(repl='@', string=src_str, count=2)
    print(result_str)  # hell@_pyth@n_iou

    '''
    查询到所有匹配到字符串
    def findall(self,
            string: AnyStr,
            pos: int = ...,
            endpos: int = ...) -> list
    string： 原字符串
    pos： 起始索引
    endpos： 结束索引(不包含)
    '''
    match_list = p_o.findall(string=src_str, pos=1, endpos=10)
    print(match_list)  # ['o']
    # 验证不包含end索引
    substring = src_str[1:10]
    substring_match_list = p_o.findall(string=substring)
    print(substring_match_list)  # ['o']

    '''
    def search(self,
           string: AnyStr,
           pos: int = ...,
           endpos: int = ...) -> Optional[Match[AnyStr]]
    string: 原字符串
    pos、endpos： 起始索引
    '''
    aa = p_o.search(string=src_str)
    print(aa)  # <re.Match object; span=(4, 5), match='o'>
    match_result = aa
    '''
    获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回，0代表整个匹配串
    返回 match 的一个或多个子组。
    如果只有唯的一参数，返回单一的子符串；如果有多个参数，结果是对应每一个参数的元素组成的 tuple 。
    如果没有参数， group 的默认值为 0 （返回整个匹配的字符串）
    def group(self, __group: Union[str, int] = ...) -> AnyStr
    Possible types:
    • (self: Match, __group: Union[str, int]) -> AnyStr
    • (self: Match, __group1: Union[str, int], __group2: Union[str, int], groups: Tuple[Union[str, int], ...]) -> Tuple[AnyStr, ...]
    '''
    any_str = match_result.group()
    print(any_str)  # o
    '''
    以元组形式返回全部分组截获的字符串，相当于调用group((1,2,…n))
    def groups(self, default: AnyStr = ...) -> Sequence[AnyStr]
    '''
    seq_any = match_result.groups()
    print(seq_any)  # ()

    '''
    返回以有别名的组的别名为键、以该组截获的子串为值的字典
    def groupdict(self, default: AnyStr = ...) -> Dict[str, AnyStr]
    '''
    dict_any = match_result.groupdict()
    print(dict_any)  # {}

    '''
    group传参对应正则（）分组
    def match(self,
          string: AnyStr,
          pos: int = ...,
          endpos: int = ...) -> Optional[Match[AnyStr]]
    '''
    match_result = p_o.match(string=src_str, pos=0, endpos=10)
    result_str = match_result.group()
    print(result_str)




if __name__ == '__main__':
    api_test(p="o", src_str="hello_python_iou", fs=0)



