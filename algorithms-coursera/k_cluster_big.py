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
	vertices = read_graph('problems/k_clustering_big.txt')

	# R = 0
	vertices = set(vertices)

	# R = 1
	clusters = UnionFind(vertices)
	for v in vertices:



	print vertices[:20]

test()


