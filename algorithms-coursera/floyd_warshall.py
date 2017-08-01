import sys

def unit_init(a, graph):
	for ak in a:
		for i in range(len(ak)):
			ak[i] = [0] * len(ak[i])

	for t, d in graph.items():
		for h, v in d.items(): 
			a[0][t][h] = v

def unit_relax(A, i, j, k):
	return A[k-1][i][j] + A[k-1][i][k-1] * A[k-1][k-1][j]

def standard_init(a, graph):
	for ak in a:
		for i in range(len(ak)):
			ak[i] = [sys.maxint] * len(ak[i])

	for t, d in graph.items():
		for h, v in d.items(): 
			a[0][t][h] = v
		a[0][t][t] = 0

def standard_relax(A, i, j, k):
	return min(A[k-1][i][j], A[k-1][i][k-1] + A[k-1][k-1][j])


def floy_warshall(graph, init=standard_init, relax=standard_relax):

	n = len(graph)
	A = [[[sys.maxint for j in range(n)] for i in range(n)] for k in range(n+1)]
	init(A, graph)

	print '\nk=0'
	print_a(A[0])
	for k in range(1, n+1):
		for i in range(n):
			for j in range(n):
				A[k][i][j] = relax(A, i, j, k)

		print '\nk=',k
		print_a(A[k])

	return A

def print_a(a):
	for ai in a:
		print ''.join(map('{:7d}'.format, ai))

def test_basic():
	graph = {
		0: {2: -2},
		1: {0: 4, 2: 3},
		2: {3: 2},
		3: {1: -1}
	}

	A = floy_warshall(graph)

	print '\nk=n'
	print_a(A[-1])

	assert A[-1] == [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
	print 'Passed all basic tests!'

def test_unit_graph():
	graph = {
		0: {1: 1},
		1: {2: 1},
		2: {0: 1}
	}
	A = floy_warshall(graph, unit_init, unit_relax)

	print '\nk=n'
	print_a(A[-1])

def test_strongly_connected_graph():
	graph = {
		0: {1: -1, 2:-1, 3: -1, 4: -1},
		1: {2: -1, 0:-1, 3: -1, 4: -1},
		2: {0: -1, 1:-1, 3: -1, 4: -1},
		3: {0: -1, 1: -1, 2:-1, 4: -1},
		4: {0: -1, 1: -1, 2:-1, 3: -1},
	}
	# graph = {
	# 	0: {1: -1},
	# 	1: {2: -1},
	# 	2: {3: -1},
	# 	3: {4: -1},
	# 	4: {0: -1},
	# }


	A = floy_warshall(graph, standard_init, standard_relax)

	print '\nk=n'
	print_a(A[-1])

if __name__ == '__main__':
	test_basic()
	# test_unit_graph()
	# test_strongly_connected_graph()