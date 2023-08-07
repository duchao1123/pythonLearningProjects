"""
====================   简化重复打印 *   ====================
"""
# price = input('price: ')
#
# print(f'total price = {price * 2}')  # price: 5; total price = 55
#
# print(f'total price = {int(price) * 2}')  # price: 5; total price = 10

# 怀疑 字符串 * n 是打印n个字符串
strValue = 'a'
intValue = 5
print(f'{strValue * 10}')  # aaaaaaaaaa
print(f'{intValue * 10}')  # 50

# 区分{}内外, 低级错误
print(f'{strValue} * 10')  # a * 10

"""
====================   打印其他占位符   ==================== 
"""

'''
1、%c，格式化字符及其ASCII码

2、%s，格式化字符串

3、%d，格式化整数

4、%.xf，float

5、%o，格式化无符号八进制数
'''
print('str = %s' % '你好')
# print('str = %c' % '你好')  # TypeError: %c requires int or char
print('str = %s, ASCII code = %c' % (64, 64))  # str = 64, ASCII code = @

'''
10进制    8进制
0        0
1        1
8        10
9        11
10       12
'''
print('str = %o' % 10)  # str = 12

"""
====================   f-string   ==================== 
"""
# f可以大写可以小写
int_value = 5
print(f'value = {intValue:03d}')
print(F'value = {intValue:03d}')
# 限定{}内输出格式时，:号后面紧跟限制， ' '空格也会占位
'''
value = 005
value = 005
value =  05
'''
print(F'value = {intValue: 03d}')

float_value = 3.1415
print(f'value = {float_value}')
print(f'value = {float_value:.2f}')
print(f'value = {float_value:.3f}')
'''
value = 3.1415
value = 3.14
value = 3.142 自动四舍五入
'''
