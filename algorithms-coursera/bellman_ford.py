import sys

def bellman_ford(graph, source):
	"""
	Implementing the bellmand-ford for SSSP - single source shortest path
	init source value 0, other inf
	iterate through available budget i from 1 to n-1 inclusive
	shortest path values propagate from source to the entire domain
	at iter i-th:
		loop over w nodes in the wave_front - the updated vertices at i-1 th
			loop over v nodes neighbor of w:
				update A[i, v] = min(A[i-1, v], A[i-1, w] + length(w,v))
				push v to the wave_front
	"""
	V = list(set([k for v in graph.values() for k in v] + graph.keys()))
	n = len(V)
	A0 = {v: sys.maxint for v in V}
	A0[source] = 0

	A = [dict(A0) for i in range(2)] # optimized version, we only need A[i-1] and A[i]

	wave_front = {source}
	for i in range(1,n):
		if not wave_front:
			break

		new_wf = set()
		for w in wave_front:
			for v, c in graph[w].items():
				A[1][v] = min(A[0][v], A[0][w] + c)
				if v in graph and A[1][v] < A[0][v]: # make sure there is outgoing edges from v
					new_wf.add(v)

		A[0] = dict(A[1]) # update
		wave_front = new_wf
	return A[1]



def test_basic():
	graph = {
		0: {1: -1, 2: 1},
		1: {2: 1},
		2: {3: 2},
	}

	sp = bellman_ford(graph, 0)
	assert sp == {0: 0, 1: -1, 2: 0, 3: 2}, 'failed test basic, result {}'.format(sp)
	print 'Passed basic tests!'


test_basic()