"""
==================  ==================
"""
import pandas




def func(a, b):
    def call_f(x):
        return a * x + b
    return call_f


if __name__ == '__main__':
    # y = ax + b
    f = func(2, 1)
    print(f(10))
    print(f(11))
    print(f(12))



