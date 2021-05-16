

my_str = [1, 2, 3, 4]


def reverse_string(str1):
	return str1[::-1]

print(reverse_string(my_str))

# 去重
print(list(set([1,2,3,3,2,1])))


tup = tuple(my_str)
print(tup)
print(list(tup))
