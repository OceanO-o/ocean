ll = [8, 3, 1, 2, 5, 4, 6, 9, 0, 7]


def bubble_sort(array):
	for i in range(len(array)):
		for j in range(len(array) -i -1):
			if array[j] > array[j + 1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array


# print(bubble_sort(ll))


def quick_sort(array, i, j):
	if i >= j:
		return array
	base = array[i]
	low = i
	high = j
	while i < j:
		while i < j and array[j] >= base:
			j -= 1
		array[i] = array[j]

		while i < j and array[i] <= base:
			i += 1
		array[j] = array[i]
	array[j] = base

	quick_sort(array, low, i - 1)
	quick_sort(array, i + 1, high)
	return array


ls =[30,24,5,58,18,36,12,42,39]
# print(quick_sort(ls, 0, len(ls) - 1))




def quick_sort1(array, left, right):
	if left >= right:
		return array

	base = array[left]
	low = left
	high = right

	while low < high:

		while low < high and array[high] >= base:
			high -= 1
		array[low] = array[high]

		while low < high and array[low] <= base:
			low += 1
		array[high] = array[low]

	array[high] = base

	quick_sort(array, left, low-1)
	quick_sort(array, low+1, right)
	return array

final = quick_sort1(ls, 0, len(ls)-1)
print(final)