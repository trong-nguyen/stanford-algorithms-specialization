import heapq
import copy

def prim(G):
	tree = {}
	v = G.keys()[0]
	heap = [(cost, (v, u)) for u, cost in G[v].iteritems()]
	heapq.heapify(heap)
	while len(tree) != len(G) and heap:
		ce = heapq.heappop(heap)
		cost, (u, v) = ce
		if u in tree and v in tree:
			continue

		node_in = v if v in tree else u
		node_out = u if v in tree else v

		tree[node_in] = tree.get(node_in, {})
		tree[node_in][node_out] = cost
		tree[node_out] = {node_in: cost}

		new_costs = [(cost, (node_out, nb)) for nb, cost in G[node_out].iteritems() if nb not in tree]
		for ce in new_costs:
			heapq.heappush(heap, ce)

	return tree

def test_basic():
	print 'Basic tests start ------'
	G = {
		'a': {'b': 1, 'c': 3, 'd':4},
		'b': {'a': 1, 'c': 5, 'e': 2},
		'c': {'a': 3, 'd': 7, 'b': 5, 'e': 4},
		'd': {'a': 4, 'c': 7},
		'e': {'b': 2, 'c': 4}
	}

	tree = prim(G)
	print adjacency_to_edge_list(tree)
	print 'MST cost:', charge(tree)
	print 'Basic tests end ------\n'

def test():
	for tc in [1, 2]:
		f = 'problems/prim_input_1.txt'.replace('_1.txt', '_' + str(tc) + '.txt')
		graph = read_graph(f)
		expected = int(open(f.replace('_input', '_output')).read())

		tree = prim(graph)
		res = charge(tree)
		assert res == expected, 'Test Case {} failed: result {}, expected {}'.format(tc, res, expected)

		print 'Passed test case', tc


def adjacency_to_edge_list(adj):
	adj = copy.deepcopy(adj)
	edges = []
	for u, a in adj.iteritems():
		for v, c in a.iteritems():
			edges.append((u, v, c))
			del adj[v][u]

	return edges

def charge(tree):
	costs = [sum(v.values()) for v in tree.values()]
	return sum(costs) / 2

def read_graph(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	data.pop(0)
	data = [map(int, d.split()) for d in data]
	data = filter(bool, data)

	graph = {}

	for u, v, cost in data:
		for x, y in zip((u, v), (v, u)):
			graph[x] = graph.get(x, {})
			graph[x][y] = cost

	return graph

def test_assignment():
	f = 'problems/prim_edges.txt'
	graph = read_graph(f)

	tree = prim(graph)
	res = charge(tree)

	print 'Prim MST cost', res

test_basic()
test()
test_assignment()
