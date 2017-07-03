def knap(values_weights, W):
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

def print_cache(A):
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




def test_basic():
	for tc, (vw, W, expected) in enumerate([
		([(3,4), (2,3), (4,2), (4,3)], 6, [(4,2), (4,3)]),
		([(3,4), (2,3), (4,2), (4,3), (3,9), (4,2), (4,1), (5,6), (9,4)], 9, None),
	]):
		print 'Test', tc + 1
		A = knap(vw, W)
		items = sack(vw, A)
		print_cache(A)
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

test_basic()
test_variation()
