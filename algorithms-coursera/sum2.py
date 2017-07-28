from bisect import bisect_left, bisect_right
import numpy as np
import itertools

def find_le(a, x):
    'Find rightmost index whose value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    return None

def find_ge(a, x):
    'Find leftmost index whose value greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return i
    return None

def find_range(a, lo, hi):
	'Return array a that lo <= a[0], a[-1] <= hi'
	i, j = find_ge(a, lo), find_le(a, hi)
	if i == None or j == None:
		return []
	return a[i:j+1]

def find_valid_sums(a, ran):
	def admissible(x):
		y = [i for i in find_range(a, ran[0]-x, ran[1]-x) if i != x]
		return y + x

	a = np.array(a)
	a.sort() # neccesary for correct bisect operations
	valid = map(admissible, a) # map from x to y to t=x+y
	valid = filter(lambda x: x.size, valid) # filter empty
	valid = list(itertools.chain.from_iterable(valid)) # concatenate into a single list
	return set(valid)


def read_array(f):
	data = open(f, 'r').read()
	data = filter(bool, data.split())
	return map(int, data)

def test_basic():
	array = [1, 1, -1, 0, 3, 2, 4, 5]
	ran = (-3, 3) #inclusive

	distinct_sums = find_valid_sums(array, ran)
	sd = sorted(distinct_sums)
	assert sd == [-1, 0, 1, 2, 3], sd
	result = len(distinct_sums)
	print 'Number of summable values {}'.format(result)


def test_assignment():
	'''
	There are 427 summable values in range (-10000, 10000)
	There are 4274 summable values in range (-100000, 100000)
	There are 42760 summable values in range (-1000000, 1000000)
	There are 427657 summable values in range (-10000000, 10000000)
	'''
	
	array = read_array('problems/2sum.txt')
	#inclusive
	rans = [
		(-10000, 10000),
		(-100000, 100000),
		(-1000000, 1000000),
		(-10000000, 10000000),
	]
	for ran in rans:
		distinct_sums = find_valid_sums(array, ran)
		result = len(distinct_sums)
		print 'There are {} summable values in range {}'.format(result, ran)



test_basic()
test_assignment()