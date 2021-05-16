# 给定一个包含n个数的排序数组，找出给定目标值target的其实和结束位。
# 如果目标值不在数组中，返回[-1, -1]
ll = [5, 7, 7, 8, 8, 10]    #  target=8   返回[3, 4]
def find_target(array, target):
	if target not in array:
		return [-1, -1]

	start = 0
	for index, key in enumerate(array):
		if not start:
			if target == key:
				start = index
		else:
			if target != key:
				return [start, index - 1]


print(find_target(ll, 8))

# 滑动窗口最大值
# [1, 2, 7, 7, 8] 滑动窗口k=3 返回 [7,7,8]

def _find_max(array):
	max_num = 0
	for key in array:
		if key > max_num:
			max_num = key
	return max_num

def find_max(array, k):
	if len(array) == k:
		return [_find_max(array)]
	result = list()
	index = k
	while k-1 < len(array):
		data = array[k-index:k]
		result.append(_find_max(data))
		k += 1
	return result


lll = [1, 9, 7, 7, 8]
print(find_max(lll, 3))

