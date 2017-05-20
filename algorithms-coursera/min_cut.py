import random
import copy

class EdgeGraph(object):
	"""docstring for EdgeGraph"""
	def __init__(self, adjacencies):
		super(EdgeGraph, self).__init__()

		# these explored discovery tactics are 1 dimensional from v0 to v1
		def not_explored(v0, v1, explored):
			return not(v0 in explored and v1 in explored[v0])

		def mark_explored(v0, v1, explored):
			explored[v1] = explored.get(v1, {})
			explored[v1][v0] = True

		explored = {}
		vertex_edges = {} # to keep track of which edges are associated with which vertex

		for v0, vs in adjacencies.iteritems():
			# arrange connections in buckets
			ds = {}
			for vi in vs:
				ds[vi] = ds.get(vi, 0) + 1

			for vi, counts in ds.iteritems():
				if not_explored(v0, vi, explored):
					vertex_edges[vi] = vertex_edges.get(vi, []) + [(v0, counts)]
					vertex_edges[v0] = vertex_edges.get(v0, []) + [(vi, counts)]

					mark_explored(v0, vi, explored)

		self.vertex_edges = vertex_edges
		self.edges = []

	def pick_random_edge(self):
		def shuffle(ve):
			items = [(v0, v1) for v0, tp in ve.iteritems() for v1, count in tp for i in range(count)]
			random.shuffle(items)
			return items

		# correct only with reused vertices after contraction
		# the idea is to pre-generate a random sample of all edges
		# resupply if running out
		while self.vertex_edges:
			if not self.edges:
				self.edges = shuffle(self.vertex_edges)

			edge = self.edges.pop()
			v0, v1 = edge
			if v0 in self.vertex_edges and v1 in self.vertex_edges:
				return edge

	def new_node(self, v0, v1):
		# return '{},{}'.format(v0, v1)
		return v0

	def contract(self, edge):
		v0, v1 = edge
		new_vertex = self.new_node(v0, v1)
		v0_vertices = self.remap(v0, v1, new_vertex)
		v1_vertices = self.remap(v1, v0, new_vertex)

		del self.vertex_edges[v0]
		del self.vertex_edges[v1]
		self.vertex_edges[new_vertex] = self.shorten(v0_vertices + v1_vertices)

	def shorten(self, tuples):
		d = {}
		for k, count in tuples:
			d[k] = d.get(k, 0) + count
		return [(k,v) for k,v in d.iteritems()]

	def remap(self, v0, v1, new_vertex):
		vs = self.vertex_edges[v0]
		vs = [vi for vi in vs if vi[0] != v1]
		for vi, count in vs:
			tp = map(lambda x: (new_vertex, x[1]) if x[0] == v0 else x, self.vertex_edges[vi])
			self.vertex_edges[vi] = self.shorten(tp)
		return vs

	def size(self):
		return len(self.vertex_edges)

	def get_connectivities(self):
		ve = self.vertex_edges
		return sum([sum([c for _,c in x]) for x in ve.values()])
		

def min_cut2(adjacencies):
	def _min_cut(graph):
		while True:
			# choose random
			size = graph.size()
			edges = None

			edge = graph.pick_random_edge()

			graph.contract(edge)

			if graph.size() <= 2:
				return graph.get_connectivities() / 2, graph.vertex_edges

	mc = (10e6, None)
	n = len(adjacencies)
	count = 1
	# empirical choice based on previous success ratio (2%) of total runs regardless of m and n
	for i in range(500):
		eg = EdgeGraph(copy.deepcopy(adjacencies))
		new_cut = _min_cut(eg)

		if new_cut[0] == mc[0]:
			count += 1
		if new_cut[0] < mc[0]:
			count = 1 # reset
		mc = min(mc, new_cut)

		print 'Attemp No. {} (success {:.01f}%):'.format(i, 100.*count/(i+1)), mc, new_cut
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
		
		for vi in nodes:
			if not(v0 in explored and vi in explored[v0]):
				graph.append((v0, vi))
				explored[vi] = explored.get(vi, {})
				explored[vi][v0] = True
	return graph

def make_adjacency_graph(data):
	return {adj[0]: adj[1:] for adj in data}

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
	input_file = 'tests/course1/assignment4MinCut/input_random_39_200.txt'
	output_file = input_file.replace('input', 'output')
	adjacencies = read_adjacencies(input_file)

	graph = make_adjacency_graph(adjacencies)
	cuts, _ = min_cut2(graph)
	expected_cuts = int(open(output_file, 'r').read())
	assert cuts == expected_cuts, 'RCut {}, expected {}'.format(cuts, expected_cuts)

def test_assignment():
	input_file = 'kargerMinCut.txt'
	adjacencies = read_adjacencies(input_file)
	
	# edge_graph = make_edge_graph(adjacencies)
	# min_cut(edge_graph)

	graph = make_adjacency_graph(adjacencies)
	min_cut2(graph)

test()
# test_assignment()