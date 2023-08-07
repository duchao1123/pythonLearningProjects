"""
================== 课后作业 ==================
"""
'''
## 题目1 [加强训练]

### 题干
有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表
```python
list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
```

### 训练目标
让学员知道列表的循环和值的获取，以及列表的操作方法

### 训练提示
1.  如何找到列表中的每一个元素?
2.  如何判断列表中的元素以什么字符结尾?

### 参考方案
1.  使用循环遍历的方式获取列表中的每一个元素?
2.  列表中的元素为字符串,所以可以使用下标[-1] 来获取最后一个字符的值,然后判断.

### 操作步骤
1.  遍历列表中的每一个元素
2.  if 判断 最后一个字符是否是`s`或者`e`
3.  如果是,使用 append() 方法,将数据追加到新的列表中.
'''
list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
result = []
for s in list:
    if s.endswith("s") or s.endswith("e"):
        result.append(s)
print(result)


'''
## 题目2 [加强训练]

### 题干
给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且把最后一个元素复制一份，放在joke的后边

```python
my_list = ["spring", "look", "strange", "curious", "black", "hope"]
```

### 训练目标
列表的相关操作

### 训练提示
1. 通过for循环遍历列表，获取到每一个元素
2. 通过列表的操作方法对列表进行修改

### 参考方案
1. 通过for循环获取每一个元素
2. 通过remove删除列表中的元素
3. 通过insert函数在指定位置插入元素

### 操作步骤
1. 通过for循环获取每一个元素，判断是否以`s`开头
2. 如果条件成立，则通过remove删除选中的元素
3. 获取到最后一个元素，通过replace将元素放在指定的位置上
'''
my_list = ["spring", "look", "strange", "curious", "black", "hope"]
for s in my_list[:]:
    if s.startswith("s"):
        my_list.remove(s)  # 居然直接删除不引起：遍历时数据变动移除
my_list.insert(0, "joke")
my_list.insert(1, my_list[len(my_list) - 1])
print(my_list)


'''
## 题目3 [加强训练]

### 题干
将下列两个列表合并，将合并后的列表去重，之后降序并输出
```python
list1 = [11,  4, 45, 34, 51, 90]
list2 = [4, 16, 23, 51, 0]
```

### 训练目标
列表操作方法的使用

### 训练提示
1.  如何合并两个列表?
2.  如何进行列表去重?
3.  如何排序并降序输出?

### 参考方案
1.  合并列表可以使用 extend()方法或者两个列表相加。
2.  列表去重有两种方案
  1.  自己实现方法实现，借助一个新的列表，循环遍历原列表，判断元素是否在新的列表中，如果在，遍历下一个元素，如果不在，添加到新的列表中。
  2.  使用 set() 集合去重
3.  sort 函数可以实现排序，参数reverse=True对列表进行倒序排序

### 操作步骤
1，使用 +  对列表进行拼接(或者使用 extend)
2，列表去重
3，使用sort函数，参数reverse=True对列表进行倒序排序
'''

list1 = [11,  4, 45, 34, 51, 90]
list2 = [4, 16, 23, 51, 0]
sum_list = list1 + list2
new_list = [value for value in set(sum_list)]
new_list.sort(reverse=True)
print(new_list)
