def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

def select_pivot(array):
	n = len(array)
	if n in (1, 2):
		return 0

	items = [(array[index], index) for index in (0, (n-1)/2, len(array)-1)]
	return sorted(items)[1][1] # mid point, index

def swap_pivot_to_first(array):
	pivot = select_pivot(array)
	swap(array, pivot, 0)

def partition_0(array):
	ap = array[0]
	i = 0
	j = 1
	while j < len(array):
		if array[j] < ap:
			i += 1
			swap(array, i, j)
		j += 1
	swap(array, 0, i)
	return i

def _select(array, k):
	if len(array) == 1:
		assert k == 0, 'Serious logic error'
		return array[0]

	swap_pivot_to_first(array)
	p = partition_0(array)

	# print array[:p], array[p], array[p+1:], p
	if k == p:
		return array[p]
	elif k < p:
		return _select(array[:p], k)
	else:
		return _select(array[p+1:], k-p-1)

def select(array, k_base1):
	assert 0 < k_base1 <= len(array)
	k = k_base1 - 1
	return _select(array, k)

def test():
	array = [1, 2, 3, 4, 5]
	assert select(array, 3) == 3

	array = [9, 0, 3, 1, 2, 4, 6]	
	assert select(array, 6) == 6, select(array, 6)

def test_big():
	import random
	for t in range(5):
		n = random.randrange(10000, 100000)
		array = [random.randrange(n) for i in range(n)]
		i = random.randrange(1, len(array))
		res = select(array, i)
		expected = sorted(array)[i-1]
		stat = 'Select item {}-th: result {}, expected {}'.format(i, res, expected)
		assert res == expected, stat
		print stat

test()
test_big()


