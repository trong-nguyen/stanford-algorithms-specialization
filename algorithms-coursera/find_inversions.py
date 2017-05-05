# find number of inversions in array
# complexity O(nlogn), same as merge sort

def count_merge_split_inversions(sorted_left, sorted_right):
	merged = []
	nl = len(sorted_left)
	nr = len(sorted_right)
	i = 0
	j = 0
	count = 0
	while i < nl or j < nr:
		if i < nl and j < nr:
			if sorted_left[i] <= sorted_right[j]:
				appendee = sorted_left[i]
				i += 1
			else:
				appendee = sorted_right[j]
				j += 1
				count += nl - i # piggyback
				# print 'found {}, i={}, j={} in left {}, right {}'.format(count, i, j, sorted_left, sorted_right)
			merged.append(appendee)
		else:
			if i < nl:
				merged.append(sorted_left[i])
				i += 1
			else:
				merged.append(sorted_right[j])
				j += 1
	return count, merged

def count_inversions(array):
	n = len(array)
	if n == 1:
		return 0, list(array)

	left_inv, sorted_left = count_inversions(array[:n/2])
	right_inv, sorted_right = count_inversions(array[n/2:])
	split_inv, merged = count_merge_split_inversions(sorted_left, sorted_right)

	inv = left_inv + right_inv + split_inv

	return inv, merged

def test():
	for i, (array, expected_inv) in enumerate([
		([1,3,5,2,4,6], 3),
		([1,5,3,2,4], 4),
		([5,4,3,2,1], 10),
		([1,6,3,2,4,5], 5),
		([9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0], 56),
		([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45], 590),
		([4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54], 2372),
	]):
		inv, _ = count_inversions(array)
		assert inv == expected_inv, 'Failed case {}, expected {}, counted {}'.format(i, expected_inv, inv)
		print 'Passed case', i

def test2():
	data = open('IntegerArray.txt', 'r').read()
	array = map(int, data.split())
	inv, _ = count_inversions(array)
	print 'There are {} inversions in the array'.format(inv)

	assert inv == 2407905288, 'Failed test'

# test2()

# test()