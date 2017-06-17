from union_find import UnionFind

def read_graph(f):
	def make_label(s):
		# join binary strings and convert to decimal
		return int(s.replace(' ', ''), 2)

	data = open(f, 'r').read()
	data = filter(bool, data.split('\n'))
	data.pop(0)
	data = map(make_label, data)

	return data

def permute(label, level, bits):
	res = []
	if level == 1:
		# create bit 1 then shift it left to the i-index
		# equivalent to toggle bit i of label
		return [label ^ 1 << i for i in range(bits)]
	if level == 2:
		return [(label ^ 1 << j) ^ 1 << i for i in range(bits) for j in range(i+1,bits)]

	raise Exception('Level not supported')


def test():
	BITS = 24
	MIN_SPACING = 3
	vertices = read_graph('problems/k_clustering_big.txt')

	# R = 0
	vertices = set(vertices)

	# R = [1 ... MIN_SPACING)
	clusters = UnionFind(vertices)
	for v in vertices:
		candidates = [j for i in range(1, MIN_SPACING) for j in permute(v, i, BITS)] # permute(v, 1, BITS) + permute(v, 2, BITS)
		candidates = filter(lambda x: x in vertices and x != v, candidates)
		for candidate in candidates:
			clusters.union(v, candidate)


	print 'Question 2 K-Cluster'
	print 'Maximum k for min spacing to be {} is {}'.format(MIN_SPACING, len(clusters))

test()


