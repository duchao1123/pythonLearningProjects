"""
====================   异常  ====================
"""
'''
捕获异常
try:
    可能出错的代码
except Exception as e:
    捕获异常类型
else:
    表示的是如果没有异常要执行的代码
finally:
    表示的是无论是否异常都要执行的代码，例如关闭文件、关闭数据库连接
'''

try:
    # ZeroDivisionError: division by zero
    result = 100 / 0
except ZeroDivisionError:
    print('是不是傻')

# 与java不同
# else

try:
    print("我没事，你没事吧")
except:
    print('可能有事')
else:
    print('没事去吃溜溜梅吧')
finally:
    print('都闭嘴')

"""
====================   自定义异常  ====================
使用 `raise 异常类对象` 抛出自定义异常
raise Exception('xxxx')   同java throw
"""

try:
    raise Exception('闲来无事抛异常')
except Exception:
    print('呆子找打')


"""
====================   断言  ====================
assert  固定抛出AssertionError
如果断言正确，正常执行。如果断言错误，抛出AssertionError
"""

assert 1 == 2
