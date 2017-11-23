import operator
from union_find import UnionFind

def read_graph(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	data.pop(0)
	data = [map(int, d.split()) for d in data]
	data = filter(bool, data)

	return data

def k_cluster(graph, k):
	graph = sorted(graph, key=operator.itemgetter(2), reverse=True)
	vertices = list(set([i for ec in graph for i in ec[:2]]))
	ufc = UnionFind(vertices)
	min_spacing = graph[-1][-1]
	clusters = ufc.get()
	while len(ufc) >= k and graph:
		u, v, min_spacing = graph.pop()
		ufc.union(u, v)

		# keep the iteration going even the number of clusters already reaches k
		# due to the fact that we want to eliminate cyclic edges after the last union
		# to find the correct min spacing
		if len(ufc) == k:
			clusters = ufc.get()

	# in case of a single cluster, theoretically min_spacing should be infinite
	if len(ufc) == 1:
		min_spacing = float('inf')

	return min_spacing, clusters

def standardize_clusters(clusters):
	return sorted([sorted(c) for c in clusters]) # for convenient assertions

def test_basic():
	graph = [
		(1, 2, 4),
		(1, 4, 5),
		(1, 3, 6),
		(2, 4, 1),
		(3, 4, 3)
	]
	for (res_spacing, res_clusters), (expected_spacing, expected_clusters) in [
		(k_cluster(graph, 4), (1, [[1], [2], [3], [4]])),
		(k_cluster(graph, 3), (3, [[1], [3], [2, 4]])),
		(k_cluster(graph, 2), (4, [[1], [2, 3, 4]])),
		(k_cluster(graph, 1), (float('inf'), [[1, 2, 3, 4]])),
	]:
		res_clusters = standardize_clusters(res_clusters)
		expected_clusters = standardize_clusters(expected_clusters)
		assert res_clusters == expected_clusters, 'Failed test basic 0: result [{}], expected_clusters [{}]'.format(res_clusters, expected_clusters)


	for tc in [1]:
		k = 4
		f = 'problems/k_cluster_input_1.txt'.replace('_1.txt', '_' + str(tc) + '.txt')
		graph = read_graph(f)
		expected_spacing, expected_clusters = read_expected(f.replace('_input', '_output'))

		res_spacing, res_clusters = k_cluster(graph, k)

		res_clusters = standardize_clusters(res_clusters)
		expected_clusters = standardize_clusters(expected_clusters)
		assert res_spacing == expected_spacing and res_clusters == expected_clusters, 'Failed test basic {}, resultant spacing {}, expected spacing {}'.format(tc, res_spacing, expected_spacing)

		print 'Passed test case', tc

	print 'Passed all basic tests!'

def read_expected(f):
	data = open(f).read()
	data = data.split('\n')

	spacing = int(data.pop(0)) # note, could be a float
	clusters = [map(int, d.split()) for d in data]
	clusters = filter(bool, clusters)

	return spacing, clusters


def test():
	import os
	test_cases = os.listdir('tests/course3/assignment2Clustering/question1/')
	test_cases = filter(lambda f: f.find('input') != -1, test_cases)
	test_cases = map(lambda f: f.replace('input_completeRandom_', '').replace('.txt', ''), test_cases)

	for tc in test_cases:
		k = 4
		f = 'tests/course3/assignment2Clustering/question1/input_completeRandom_10_32.txt'.replace('_10_32', '_' + tc)
		graph = read_graph(f)
		expected_spacing, expected_clusters = read_expected(f.replace('input_', 'output_'))

		res_spacing, res_clusters = k_cluster(graph, k)

		# res_clusters = standardize_clusters(res_clusters)
		# expected_clusters = standardize_clusters(expected_clusters)
		assert res_spacing == expected_spacing, 'Failed test case {}, resultant spacing {}, expected spacing {}'.format(tc, res_spacing, expected_spacing)

		print 'Passed test case', tc


def test_assignment():
	# Question 1
	f = 'problems/k_clustering.txt'
	k = 4
	graph = read_graph(f)
	res_spacing, res_clusters = k_cluster(graph, k)

	print 'Minimum spacing for Question 1', res_spacing

test_basic()
test()
test_assignment()