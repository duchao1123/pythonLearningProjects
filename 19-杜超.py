"""
19、定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。 [上传文件题]
"""
import random
code_length = 4


def gen_verification_code(full_str: str):
    result = ''
    for i in range(code_length):
        index = random.randint(0, len(full_str))
        char_index = full_str[index]
        result = ''.join([result, char_index])
    return result


if __name__ == "__main__":
    str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = gen_verification_code(str1)
    print(f"验证码：{code}")










