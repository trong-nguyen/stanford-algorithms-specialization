def swap_pivot_to_start(array, start, end, pivot_as):
	# pivot_index = (start + end - 1)/2
	# pivot_index = end - 1
	pivot_index = pivot_as(start, end, array)
	swap(array, pivot_index, start)

def select_first_as_pivot(start, end, array=None):
	return start

def select_last_as_pivot(start, end, array=None):
	return end - 1

def select_median_as_pivot(start, end, array):
	n = end - start
	if n == 1:
		return start
	elif n == 2:
		return start

	items = [(array[index], index) for index in (start, start+(n-1)/2, end-1)]
	return sorted(items)[1][1] # mid point, index

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

def partition_0(array, start, end):
	pivot = start
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


def _quick_sort(array, start, end, pivot_as):
	if start >= end:
		return
	# divide
	swap_pivot_to_start(array, start, end, pivot_as)
	i = partition_0(array, start, end)

	comparisons = 0
	try:
		# print array[start:i], [array[i]], array[i+1:end] , array
		if start < i:
			comparisons += i - start - 1
			comparisons += _quick_sort(array, start, i, pivot_as)
		if i+1 < end:
			comparisons += end - i - 1 - 1
			comparisons += _quick_sort(array, i+1, end, pivot_as)
	except RuntimeError:
		print array, start, i
		raise

	# combine
	return comparisons

import math
def quick_sort(array):
	cp = list(array)
	_quick_sort(cp, 0, len(cp), select_median_as_pivot)
	return cp

def comparisons_in_quick_sort(array, pivot_as):
	cp = list(array)
	comp = len(cp) - 1 + _quick_sort(cp, 0, len(cp), pivot_as)
	n = len(array)
	# print 'Total comparisons {}, ({:.0f}%) of array length {}'.format(comp, 100. * comp / n / int(math.log(n, 2)), n)
	return comp


def test():
	array = [0, 3, 1, 2, 6, 9, 3]
	assert select_median_as_pivot(0, len(array), array) == 3, select_median_as_pivot(0, len(array), array)

	array = [3,2,8,5,1,4,7,6]
	assert quick_sort(array) == [1, 2, 3, 4, 5, 6, 7, 8], array

	array = [1,1,1,2,1,3,1,4,4,1]
	assert quick_sort(array) == [1, 1, 1, 1, 1, 1, 2, 3, 4, 4], array


	array = [3, 6, 4, 1, 4, 3, 3, 3, 5, 6]
	assert quick_sort(array) == [1, 3, 3, 3, 3, 4, 4, 5, 6, 6], array


	array = [9, 3, 3, 0, 4, 2, 6, 1, 8, 0]
	assert quick_sort(array) == [0, 0, 1, 2, 3, 3, 4, 6, 8, 9], array

	

	import random
	for t in range(5):
		n = random.randrange(1000, 10001)
		array = [random.randrange(n) for i in range(n)]
		# print array, sorted(array)
		assert quick_sort(array) == sorted(array), array

def load_array(f):
	data = open(f, 'r').read()
	# array = map(bool, data.split())
	array = map(int, data.split())
	return array

def test_big():
	array = [8, 2, 4, 5, 7, 1]
	assert select_median_as_pivot(0, len(array), array) == 2, select_median_as_pivot(0, len(array), array)

	cases = [
		'01_5','02_5','03_5','04_5','05_5',
		'06_10','07_10','08_10','09_10','10_10', 
		'11_20', '12_20', '13_20', '14_20', '15_20',
		'16_100000',
	]
	for file in ['tests/course1/assignment3Quicksort/input_dgrcode_{}.txt'.format(c) 
		for c in cases]:

		array = load_array(file)
		output = [
			comparisons_in_quick_sort(array, select_first_as_pivot),
			comparisons_in_quick_sort(array, select_last_as_pivot),
			comparisons_in_quick_sort(array, select_median_as_pivot),
		]
		
		ofile = file.replace('input', 'output')
		expected = load_array(ofile)
		print output, expected
		if not output == expected:
			'Failed case {}'.format(file)

def test_assignment():
	array = load_array('QuickSort_Array.txt')
	print '{} comparisons with first item as pivot'.format(comparisons_in_quick_sort(array, select_first_as_pivot))
	print '{} comparisons with last item as pivot'.format(comparisons_in_quick_sort(array, select_last_as_pivot))
	print '{} comparisons with median item as pivot'.format(comparisons_in_quick_sort(array, select_median_as_pivot))


# test()
# test_big()
test_assignment()
