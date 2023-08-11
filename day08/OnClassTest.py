"""
==================  ==================
"""
print((lambda *args: sum(args))(1, 2, 3))

var1 = lambda a, b: a if a > b else b
print(var1(3, 4))

list3 = [8, 4, 3, 6, 5, 7, 9]
list3.sort(key=lambda x: x % 4)
print(list3)


print((lambda *args: [value ** 2 for value in args])(1, 2, 3, 4, 5))


