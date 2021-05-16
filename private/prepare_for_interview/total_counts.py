
my_str = "abcebdirideawsleee"


def func(my_str):
	# 使用my_str的每一个字符串作为dict的key
	# 遍历my_str，计算每个字符出现的次数
	# return type dict
	res = {}
	for key in my_str:
		if key not in res:
			res[key] = 1
		else:
			res[key] += 1
	return res


print(func(my_str))




















def counts(str1):
	counts_dict = dict()
	for key in str1:
		counts_dict[key] = counts_dict[key] + 1 if key in counts_dict else 1
	return counts_dict

print(counts(my_str))

