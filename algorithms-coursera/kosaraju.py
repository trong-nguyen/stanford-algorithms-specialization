def first_pass(graph):
	def first_pass_callback(r, result):
		# first pass accumulates finishing times of all nodes
		result += r[1]

	return dfs_loop(graph, graph.keys(), first_pass_callback)

def second_pass(graph, finishing_time):
	def second_pass_callback(r, result):
		# second pass accumulates ith-component and its leader node
		result.append(r)

	return dfs_loop(graph, finishing_time, second_pass_callback)


def kosaraju(graph):
	graph_rev = reverse(graph)
	finishing_time = first_pass(graph_rev)
	scc = second_pass(graph, finishing_time)
	return scc

def reverse(graph):
	graph_rev = {}
	for i, nb in graph.iteritems():
		for j in nb:
			graph_rev[j] = graph_rev.get(j, []) + [i]

	return graph_rev


def dfs(g, i, explored):
	stack = [i]
	ft = []
	while stack:
		i = stack[-1]
		dead_end = True
		if i in g: # directed graph does not guarantee every node exists in adjacency list labels (i.e. natural dead-end nodes).
			for j in g[i]:
				if j not in explored:
					# print '..adding {} to stack {}, {}'.format(j, stack, explored)
					stack.append(j)
					dead_end = False
					explored.add(j)
					break
		if dead_end:
			ft.append(stack.pop())
		# print '\tDfs-ing, visiting {}, stack {}, ft {}, dead_end {}'.format(i, stack, ft, dead_end) 
	return ft

def dfs_loop(graph, sequence, callback):
	explored = set()
	result = []
	while sequence:
		i = sequence.pop()
		if i in explored:
			continue

		explored.add(i)

		res = dfs(graph, i, explored)
		callback((i, res), result)
		# print 'DFS({}), ft={}'.format(i, ft), explored

	return result

def test():
	graph = {
		1: [3],
		2: [1],
		3: [2, 4],
		4: [5],
		5: [6],
		6: [7],
		7: [8, 5],
	}

	graph_rev = {
		1: [2],
		2: [3],
		3: [1],
		4: [3],
		5: [4, 7],
		6: [5],
		7: [6],
		8: [7],
	}

	expected_finishing_time = [2, 1, 3, 4, 5, 6, 7, 8] # this is extremly particular to the above choice of graph, due to node naming

	assert reverse(graph) == graph_rev

	finishing_time = first_pass(graph_rev)
	assert finishing_time == expected_finishing_time, finishing_time

	expected_components = [(8, [8]), (7, [6, 5, 7]), (4, [4]), (3, [1, 2, 3])]

	components = second_pass(graph, finishing_time)
	assert components == expected_components, components

	expected_scc = expected_components
	scc = kosaraju(graph)
	assert scc == expected_scc, scc

test()

def test_assignment(graph_file='./scc.txt', dump_backup=False, do_assertion=True):
	def read_graph(f):
		import os
		import cPickle as pickle

		pickled_file = f.replace('.txt', '.pck')
		if os.path.exists(pickled_file):
			return pickle.load(open(pickled_file, 'rb'))

		data = open(f, 'r').read()
		data = filter(bool, data.split('\n'))
		data = [map(int, a.split()) for a in data]
		# data = [a.split() for a in data]

		graph = {}
		for tail, head in data:
			graph[tail] = graph.get(tail, []) + [head]

		if dump_backup:
			pickle.dump(graph, open(pickled_file, 'wb'))

		return graph

	graph = read_graph(graph_file)

	scc = kosaraju(graph)
	scc = [(s[0], len(s[1])) for s in scc]
	scc = sorted(scc, key=lambda tp: tp[1], reverse=True)
	# scc = sorted(scc, key=lambda tp: len(tp[1]), reverse=True)
	largest_5 = scc[:5]
	largest_5 = largest_5 if len(largest_5) == 5 else largest_5 + [(0,0)] * (5 - len(largest_5))
	largest_5_str = ','.join([str(s[1]) for s in largest_5])
	print '5 largest components:', largest_5_str
	print largest_5

	if do_assertion:
		assert_file = graph_file.replace('input', 'output')
		expected = open(assert_file, 'r').read().strip()
		expected = expected.split(',')
		expected = [i.strip() for i in expected] # just to be sure about output cases where we have spaces
		expected = ','.join(expected) 
		assert largest_5_str == expected, 'Failed test [{}], result {}, expected {}'.format(graph_file, largest_5_str, expected)
		
		print 'Passed test case [{}] with flying colors'.format(graph_file)

# test_assignment(graph_file='./scc.txt', dump_backup=True, do_assertion=False)
for tc in range(1, 6+1):
	test_assignment(graph_file='tests/course2/assignment1StronglyConnectedComponent/input_scc_{}.txt'.format(tc))
