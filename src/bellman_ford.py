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

	return:
		- A[n-1, v] if no negative cost cycles present
		- None otherwise
	"""
	V = list(set([k for v in graph.values() for k in v] + graph.keys()))
	n = len(V)
	A0 = {v: sys.maxint for v in V}
	A0[source] = 0

	A = [dict(A0) for i in range(2)] # optimized version, we only need A[i-1] and A[i]

	wave = {source}
	for i in range(n): # n+1 -th iteration is for negative cycle detecting
		new_wave = set(wave)
		converged = True
		for w in wave:
			for v, c in graph[w].items():
				A[1][v] = min([A[1][v], A[0][w] + c])
				if v in graph and A[1][v] < A[0][v]: # make sure there is outgoing edges from v
					new_wave.add(v)
					converged = False
		
		# test for negative cost cycles
		if i == n-1 and any([A[1][v] < A[0][v] for v in V]):
			return None

		if converged:
			# print '---Stopped early at iter {} / {} (total)'.format(i+1, n)
			break

		A[0] = dict(A[1]) # update
		wave = new_wave

	return A[1]



def test_basic():
	graph = {
		0: {1: -1, 2: 1},
		1: {2: 1},
		2: {3: 2},
	}

	sp = bellman_ford(graph, 0)
	assert sp == {0: 0, 1: -1, 2: 0, 3: 2}, 'failed test basic, result {}'.format(sp)

	# add negative cost cycles
	graph[3] = {0: -3}
	sp = bellman_ford(graph, 0)
	assert sp == None, 'failed test basic, result {}'.format(sp)

	print 'Passed basic tests!'

if __name__ == '__main__':
	test_basic()