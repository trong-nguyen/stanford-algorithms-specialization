import heapq

def dijkstra(graph, source):
	inf = 1000000
	S = {k: inf for k in graph}
	S[source] = 0

	def done(node):
		return S[node] < inf

	H = [(length, node) for node, length in graph[source].items()]
	heapq.heapify(H)

	count = 1 # count of shortest distances found, apparently it is the source initially
	while H and count <= len(graph):
		score, node = heapq.heappop(H)
		if done(node):
			continue

		S[node] = score
		count += 1
		for v in graph[node]:
			if not done(v):
				heapq.heappush(H, (score + graph[node][v], v))

	return S



def read_graph(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	graph = [d.split() for d in data]
	graph = filter(bool, graph)
	graph = {int(d[0]): map(lambda x: x.split(','), d[1:]) for d in graph}
	graph = {k:{int(node):int(length) for node, length in v} for k, v in graph.iteritems()}
	return graph


def test_basic():
	graph = {
		0: {1: 2, 2: 1},
		1: {0: 2, 2: 1, 3: 1},
		2: {0: 1, 1: 1, 3: 4},
		3: {1: 1, 2: 4}
	}

	distances = dijkstra(graph, 0)
	assert distances == {0: 0, 1: 2, 2: 1, 3: 3}, 'Failed basic tests!'

def test_assignments():
	graph = read_graph('problems/dijkstraData.txt')
	# print graph
	# print [(k, graph[k]) for k in graph.keys()[:20]]
	distances = dijkstra(graph, 1)

	interested = [7,37,59,82,99,115,133,165,188,197]
	# print distances
	print ','.join(map(str, [distances[i] for i in interested]))

test_basic()
test_assignments()