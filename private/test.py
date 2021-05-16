a = [1, 2]
import copy

b = copy.copy(a)
print(b)
print(id(a), id(b))
