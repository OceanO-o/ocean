# 书籍推荐 流畅的python 黑客与画家 程序员修炼之道 集体智慧编程 人月神话 代码大全2 重构 程序员基础练级攻略
print("a b c".split())                # ['a', 'b', 'c']
print("a,b,c".split(","))             # ['a', 'b', 'c']
#  rsplit 从后往前分隔， rsplit(分隔符, 分隔几次，默认全部)返回列表
print('a b c d'.rsplit(None, 2))      # ['a b', 'c', 'd']
print('a,b,c,d'.rsplit(",", 2))       # ['a b', 'c', 'd']


# 返回一个3元的元组，分隔符左边的子串，分隔符本身，分隔符右边的子串
print('/a/b/c'.partition('/'))        # ('', '/', 'a/b/c')
print('/a/b/c'.rpartition('/'))       # ('/a/b', '/', 'c')

# 不要循环去累加来拼接
print(', '.join(['a', 'b', 'c']))     # a, b, c

# 除法
print(10/5)                           # 2    py2  10/3 =3   整数
print(10/5)                           # 2.0  py3
# print(1.1 * 0.2)                    # 0.22000000000000003   py3
from decimal import Decimal
print(Decimal('1.1') * Decimal('0.2'))  # 使得无论是2还是3都能得到浮点数
# from __future__ import division  # 使用新的除法特性,保证2和3效果一样

import keyword
print(",".join(keyword.kwlist))


# 列表
list1 = [1, 2, 3, 4, 5]
print(list1[::-1])                     # 逆序列表
del list1[0]                           # 明确知道索引删除元素
l1 = sorted(list1)                     # sorted 方法返回的是一个新的 list
list1.sort(reverse=True)               # sort 方法返回的是对已经存在的列表进行操作，无返回值


# 元组
a = 10
b = 1
a, b = b, a                             # 交换时，两步。右边b, a组成一个元组，然后元组拆包分别赋值给a, b
# tuple1 = (1, 2, [3, 4])
# try:
#     tuple1[2] += [5,6]
# except Exception as e:
#     pass
# print(tuple1)           (1, 2, [3, 4, 4, 5])


# 字典
dict1 = {"a": 1}
print(dict1.get("a"))
print(dict1.get("b", 2))
dict1.update(b=2, c=3, d=1)
print(dict1)
del dict1['a']
from collections import OrderedDict
dict2 = OrderedDict(a=1)


print(list(set([1, 3, 2, 1])))
set1 = set()
set1.add(1)
set1.update([2, 3])
print(set1)


# while  break else     for break else
# 如果执行了循环中执行了break，就不执行else,否则执行else

pass        # 作用 创建空类，占位

# 函数
# 函数参数 依次是必选参数、默认参数、可变参数和关键字参数 def func(x, y, z=0, *args, **kwargs):  *() **{}, 打包，使用时解包
# 闭包指延伸了作用域的函数，其中包含函数定义体中引用，但是不在定义体中定义的非全局变量，它能访问定义体之外定义的非全局变量
zip1 = [1, 2, 3]
zip2 = [4, 5, 6]
print(list(zip(zip1, zip2)))                # [(1, 4), (2, 5), (3, 6)]
print(list(zip(*zip(zip1, zip2))))          # [(1, 2, 3), (4, 5, 6)]

print(sum([1, 2, 3], 10))                   # 16
print(sum([1, 2, 3]))                       # 6

# 列表推导式 [表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]
li = [1, 3, 5, 6, 7, 8, 9]
print([x**2 for x in li if x > 5])
# map filter reduce    (func, iter) 一个函数，一个迭代器
# lambda func = lambda x: x * x      lambda 参数：表达式







