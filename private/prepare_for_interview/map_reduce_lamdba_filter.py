


print(list(map(lambda x: x * x, [1, 2, 3])))
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3]))
print(list(filter(lambda x: x%2 == 0, [1, 2, 3])))
# # [x for item in sequence if condition] x可以是一个表达式，比如 x+2
print([x+2 for x in [1, 2, 3]])

# map
# print(list(map(lambda x : x +1, [1, 2, 3])))
# from functools import reduce
# print(reduce(lambda x, y: x * y, [1, 2, 3]))
# print(list(filter(lambda x: x %2 == 0, [1, 2, 3])))
# print([x+2 for x in [1, 2, 3]])
