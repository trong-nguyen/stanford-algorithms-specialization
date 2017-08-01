import os
import sys
from copy import deepcopy
from dijkstra import dijkstra
from bellman_ford import bellman_ford

def johnson(graph):
	"""
	All pair shortest path algorithm with complexity O(nmlogn) for graph with negative edges
	- Create a new graph with a grounded node which has oneway connections to all other nodes
	- First use bellman_ford to reweight c_uv' = c_uv + p(v) - p(u) AND to detect negative cost cycles if present
	- Then apply Dijkstra on the reweighted graph to find shortest path
	- Then transformed shortest path values back to the unweighted values c_uv = c_uv' + p(u) - p(v)
	"""
	
	V = list(set([k for v in graph.values() for k in v] + graph.keys()))
	grounded_graph = deepcopy(graph)
	grounded_graph['ground'] = {v: 0 for v in V}

	weights = bellman_ford(grounded_graph, 'ground')
	if not weights:
		# ncc detected
		return None

	reweighted_graph = {u: {v: c + weights[u] - weights[v]
		for v, c in d.iteritems()} for u, d in graph.iteritems()}

	# dijkstra n times
	apsp = {v:dijkstra(reweighted_graph, v) for v in V}

	# unweight
	apsp = {u: {v: c - weights[u] + weights[v]
		for v, c in d.iteritems()} for u, d in apsp.iteritems()}

	return apsp

def test_basic():
	graph = {
		0: {1: -1, 2: 1},
		1: {2: 1},
		2: {3: 2},
		3: {0: 1}
	}

	apsp = johnson(graph)
	assert apsp == {
		0: {0: 0, 1: -1, 2: 0, 3: 2},
		1: {0: 4, 1: 0, 2: 1, 3: 3},
		2: {0: 3, 1: 2, 2: 0, 3: 2},
		3: {0: 1, 1: 0, 2: 1, 3: 0},
	}, 'failed test basic, result {}'.format(apsp)

	print 'Passed all basic tests!'

def read_graph(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	nodes, _ = map(int, data.pop(0).split()) # nodes
	data = filter(bool, data)
	edges = [map(int, e.split()) for e in data]
	graph = {}
	for u, v, c in edges:
		graph[u] = graph.get(u, {})
		graph[u][v] = min(graph[u].get(v, sys.maxint), c) # PREPROCESSOR, GET THE MIN COST

	return graph

def read_output(f):
	data = open(f, 'r').read()
	return data.strip()

def test():
	folder = 'tests/course4/assignment1AllPairsShortestPath'
	test_cases = os.listdir(folder)
	test_cases = filter(lambda f: 'input_' in f, test_cases)
	for tc in test_cases:
		input_file = os.path.join(folder, tc)
		output_file = input_file.replace('input_', 'output_')
		expected = read_output(output_file)
		graph = read_graph(input_file)

		apsp = johnson(graph)
		try:
			if apsp == None:
				assert 'NULL' == expected, 'expected {}'.format(expected)
			else:
				shortest = min([min(d.values()) for d in apsp.values()])
				assert str(shortest) == expected, 'expected {}, result {}'.format(expected, shortest)
		except AssertionError as e:
			print 'Failed test case {}'.format(tc), e.message
			raise
		else:
			print 'Passed test case', tc

def test_assignment():
	test_cases = ['problems/apsp_g1.txt', 'problems/apsp_g2.txt', 'problems/apsp_g3.txt']
	results = []
	for tc in test_cases:
		input_file = tc
		graph = read_graph(input_file)

		apsp = johnson(graph)
		if apsp == None:
			results.append('NULL')
		else:
			shortest = min([min(d.values()) for d in apsp.values()])
			results.append(shortest)
			print shortest
	print results


if __name__ == '__main__':
	test_basic()
	test()
	# test_assignment()