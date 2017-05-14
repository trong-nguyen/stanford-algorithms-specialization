import random
def min_cut(graph):
	edge_graph = make_edge_graph(graph)
	vertex_graph = copy.deepcopy(graph)
	vertex_graph['A'] = {}
	vertex_graph['B'] = {}
	while len(vertex_graph) > 2:
		vi, vj = edge_graph.pop(random.randrange(len(edge_graph)))
		nb = vertex_graph[vi].keys() + vertex_graph[vj].keys()
		nb = filter(lambda x: x not in (vi, vj), nb)
		del vertex_graph[vi]
		del vertex_graph[vj]
		super_node = 'B' if 'B' in nb else 'A'
		for nb in vertex_graph[vi]:
			pass
		# else


	return len(g), a, b

class EdgeGraph(object):
	"""docstring for EdgeGraph"""
	def __init__(self, adjacencies):
		super(EdgeGraph, self).__init__()

		def make_edge_graph(data):
			graph = []
			explored = {}
			for adj in data:
				v0 = adj[0]
				nodes = adj[1:]
				# graph += [(adj[0], adj_i) for adj_i in nodes]
				for vi in nodes:
					if not(v0 in explored and vi in explored[v0]):
						graph.append((v0, vi))
						explored[vi] = explored.get(vi, {})
						explored[vi][v0] = True
			return graph

		def make_vertex_graph(data):
			for adj in data:
				v0 = adj[0]
				nodes = adj[1:]
				graph[v0] = graph.get(v0, {})
				for vi in nodes:
					graph[vi] = graph.get(vi, {})
					graph[v0][vi] = 1
					graph[vi][v0] = 1

			return graph





	def remove_edge(self, vertices):
		pass

	def contract(self, vi, vj):
		pass
		

def _min_cut(edge_graph):
	# edge_graph = make_edge_graph(graph)
	while True:
		# choose random
		# vi, vj = edge_graph.pop(random.randrange(len(edge_graph)))
		vi, vj = edge_graph[random.randrange(len(edge_graph))]
		new_edge_graph = filter(lambda e: e not in [[vi, vj], [vj, vi]], edge_graph)
		stat = 'picking [{}] and [{}], edges {}'.format(vi, vj, len(edge_graph))
		# print edge_graph
		if len(new_edge_graph) < 2:
			# print len(edge_graph), edge_graph
			# print 'stopped when', stat
			return len(edge_graph), edge_graph[0]
		else:
			pass
			# print stat

		edge_graph = new_edge_graph

		# make name
		# new_node = ','.join([vi, vj])
		new_node = vi

		# filter either vertices of the edge
		edge_graph = [[new_node if v in (vi, vj) else v for v in edge] for edge in edge_graph]
		# remove self-loop
		# edge_graph = filter(lambda e: e != [new_node, new_node], edge_graph)

import copy
def min_cut(edge_graph):
	m = len(edge_graph)

	mc = (m, None)
	for i in range(m):
		g = copy.deepcopy(edge_graph)
		new_cut = _min_cut(g)
		mc = min(mc, new_cut)
		print 'Attemp No. {}:'.format(i), mc, new_cut
	return mc

def read_adjacencies(f):
	data = open(f, 'r').read()
	data = filter(bool, data.split('\n'))
	# data = [map(int, a.split()) for a in data]
	data = [a.split() for a in data]
	return data

def make_edge_graph(data):
	graph = []
	explored = {}
	for adj in data:
		v0 = adj[0]
		nodes = adj[1:]
		# graph += [(adj[0], adj_i) for adj_i in nodes]
		for vi in nodes:
			if not(v0 in explored and vi in explored[v0]):
				graph.append((v0, vi))
				explored[vi] = explored.get(vi, {})
				explored[vi][v0] = True
	return graph

def make_vertex_graph(data):
	for adj in data:
		v0 = adj[0]
		nodes = adj[1:]
		graph[v0] = graph.get(v0, {})
		for vi in nodes:
			graph[vi] = graph.get(vi, {})
			graph[v0][vi] = 1
			graph[vi][v0] = 1

	return graph

def test():
	# graph = read_graph('kargerMinCut.txt')
	edge_graph = [
		('1', '2'),
		('1', '3'),
		('2', '3'),
		('2', '4'),
		('3', '4'),
	]
	print 'Min cut for {} is {}'.format(edge_graph, min_cut(edge_graph))

def test_big():
	input_file = 'tests/course1/assignment4MinCut/input_random_40_200.txt'
	output_file = input_file.replace('input', 'output')
	adjacencies = read_adjacencies(input_file)
	edge_graph = make_edge_graph(adjacencies)
	cuts, _ = min_cut(edge_graph)
	expected_cuts = int(open(output_file, 'r').read())
	assert cuts == expected_cuts, 'RCut {}, expected {}'.format(cuts, expected_cuts)

def test_assignment():
	input_file = 'kargerMinCut.txt'
	adjacencies = read_adjacencies(input_file)
	edge_graph = make_edge_graph(adjacencies)
	min_cut(edge_graph)

# test()
# test_big()
test_assignment()