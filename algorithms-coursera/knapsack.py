import resource, sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10000)


def knap(values_weights, W):
	'''
	The usual / naive bottom up approach
	Sequentially fill in the ful n x W 2D array
	'''
	n = len(values_weights) # number of items
	A = [[0] * (W+1) for i in range(n+1)]
	for i in range(1, n+1):
		v, w = values_weights[i-1]
		for x in range(W+1):
			A[i][x] = A[i-1][x]
			if x >= w:
				A[i][x] = max(A[i][x], A[i-1][x-w] + v)

			# print '\n v={} w={} A[i-1][x-w]={}, x-w={}'.format(v,w,A[i-1][x-w], x-w)
			# print_cache(A)

	return A

def knap_top(values_weights, i, W, cache):
	'''
	Top down approach using recursive
	Much better for problems with big w steps
	So that we don't need to browse through each and every unit step of weights
	'''
	if i < 0 or W < 0:
		return 0

	if (i, W) in cache:
		return cache[(i, W)]

	if i == 0 or W == 0:
		cache[(i, W)] = 0
		return cache[(i, W)]

	v, w = values_weights[i-1]

	ai_inherited = knap_top(values_weights, i-1, W, cache)
	ai_inclusive = (v + knap_top(values_weights, i-1, W-w, cache) if W >= w else 0)
	
	cache[(i, W)] = max(ai_inherited, ai_inclusive)

	return cache[(i, W)]



def print_cache(A):
	if isinstance(A, dict):
		print A
		return

	legible_A = [[i, ''] + ai[1:] for i, ai in enumerate(A)]
	legible_A.insert(0, ['', 'w'] + [i+1 for i in range(len(legible_A[0])-2)])
	legible_A.insert(1, ['i'] + [''] * (len(legible_A[0])-1))

	n = len(legible_A)
	W = len(legible_A[0])-1
	for x in range(W,-1,-1):
		print ''.join(['{:>4}'.format(legible_A[i][x]) for i in range(n)])

def sack(values_weights, A):
	# retrieve the knap-ed items
	n = len(A) - 1
	W = len(A[0])-1

	i = n
	x = W
	residue = A[i][x]

	items = []
	while residue > 0 and i > 0:
		v, w = values_weights[i-1]
		if A[i][x] > A[i-1][x]:
			items.insert(0, (v,w))
			x -= w
		i -= 1
		residue = A[i][x]
	return items

def sack_top(values_weights, W, A):
	# items to be retrieved using the hash table A from top-down approach
	n = len(values_weights)

	i = n
	x = W
	residue = A[(i, x)]
	items = []
	while residue > 0 and i > 0:
		v, w = values_weights[i-1]
		ai_inherited = A[(i-1, x)]
		if residue > ai_inherited:
			items.insert(0, (v,w))
			x -= w
		i -= 1
		if x < 0:
			break
		residue = A[(i, x)]
	return items



def test_basic():
	for tc, (vw, W, expected) in enumerate([
		([(3,4), (2,3), (4,2), (4,3)], 6, [(4,2), (4,3)]),
		([(3,4), (2,3), (4,2), (4,3), (3,9), (4,2), (4,1), (5,6), (9,4)], 9, None),
	]):
		print 'Test', tc + 1
		# A = knap(vw, W)
		# items = sack(vw, A)

		A = {}
		res = knap_top(vw, len(vw), W, A)
		items = sack_top(vw, W, A)

		print_cache(knap(vw, W))
		# print_cache(A)
		print '\nSacked items:', items
		if expected != None:
			assert items == expected, 'Test failed, knapped the wrong items, expected {} , result {}'.format(expected, items)


def test_variation():
	for tc, (vw, W, expected) in enumerate([
		# ([(3,4), (2,3), (4,2), (4,3), (4,2), (4,1), (9,4)], 6, None),
		# ([(3,4), (2,3),		   (4,3), (4,2), (4,1)		 ], 6, None),
		# ([(3,4), (2,3), (4,2), (4,3), (4,2), (4,1), (9,4)], 12, None),
		# ([(3,4), (2,3), (4,2), (4,3), (4,2), (4,1), (9,4)], 4, None),
		# ([(3,4), (2,3), (4,2), (4,3), (4,2), (4,1)		 ], 4, None),
		# ([(3,4), (2,3), (4,2), (4,3), (4,2), (4,1), (9,4)], 8, None),
		([(2,2), (3,2), (2,2), (1,2)], 3, None),
		([(2,2), 	  	(2,2), (1,2)], 5, None),
		([(2,2), (3,2), (2,2), (1,2)], 8, None),
	]):
		print 'Test', tc + 1
		A = knap(vw, W)
		items = sack(vw, A)
		print_cache(A)
		print '\nSacked items:', items
		if expected != None:
			assert items == expected, 'Test failed, knapped the wrong items, expected {} , result {}'.format(expected, items)

def read_inputs(f):
	data = open(f, 'r').read()
	data = data.split('\n')	
	data = filter(bool, data)
	data = [map(int, w.split()) for w in data]

	W,_ = data.pop(0)

	return W, data

def read_outputs(f):
	res = open(f, 'r').read()
	return int(res.strip())


def test():
	import os
	directory = 'tests/course3/assignment4Knapsack/'
	test_cases = os.listdir(directory)
	test_cases = filter(lambda f: f.find('input_random_') != -1, test_cases)
	# test_cases = map(lambda f: f.replace('input_completeRandom_', '').replace('.txt', ''), test_cases)

	for tc in test_cases:
		ip = os.path.join(directory, tc)
		op = ip.replace('input_', 'output_')
		W, vw = read_inputs(ip)
		expected = read_outputs(op)

		A = {}
		res = knap_top(vw, len(vw), W, A)

		print 'Optimized/Naive: {:.02f}%'.format(100. * len(A) / len(vw) / W)

		assert res == expected, 'Failed test case {}, expected {}, result {}'.format(tc, expected, res)

		print 'Passed test case', tc

def test_assignments():
	for tc in [
		'problems/knapsack1.txt',
		'problems/knapsack_big.txt'
	]:
		ip = tc
		W, vw = read_inputs(ip)

		# preprocess
		vw = sorted(vw, key=lambda x: x[1])

		# A = knap(vw, W)
		# res = A[-1][-1]

		A = {}
		res = knap_top(vw, len(vw), W, A)

		print 'Optimized/Naive: {:.02f}%'.format(100. * len(A) / len(vw) / W)

		print 'Knapped value {} for test case {}'.format(res, tc)

test_basic()
# test_variation()
# test()
# test_assignments()