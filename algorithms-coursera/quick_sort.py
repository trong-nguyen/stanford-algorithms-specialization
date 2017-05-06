def pick_pivot(start, end):
	return start

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

def partition(array, pivot, start, end):
	ap = array[pivot]
	i = start
	j = start + 1
	while j < end:
		if array[j] < ap:
			i += 1
			swap(array, i, j)
		j += 1
	swap(array, pivot, i) # swap pivot to its rightful place
	return i

def quick_sort(array, start, end):
	if start >= end:
		return
	# divide
	pivot = pick_pivot(start, end)
	i = partition(array, pivot, start, end)

	quick_sort(array, start, i)
	quick_sort(array, i+1, end)

	# combine
	return

def test():
	array = [3,2,8,5,1,4,7,6]
	quick_sort(array, 0, len(array))
	assert array == [1, 2, 3, 4, 5, 6, 7, 8], array

	array = [1,1,1,2,1,3,1,4,4,1]
	quick_sort(array, 0, len(array))
	assert array == [1, 1, 1, 1, 1, 1, 2, 3, 4, 4], array



test()
