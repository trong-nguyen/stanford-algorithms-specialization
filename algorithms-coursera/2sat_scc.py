from kosaraju import kosaraju

def make_implcation_graph(instance_2sat):
	graph = {}
	for i, j in instance_2sat:
		graph[-i] = graph.get(-i, []) + [j]
		graph[-j] = graph.get(-j, []) + [i]
	return graph

def is_2sat(instance):
	vertices = set([abs(j) for i in instance for j in i])

	graph = make_implcation_graph(instance)
	scc = kosaraju(graph)

	def has_duplicates(component):
		a = map(abs, component)
		return len(set(a)) < len(a)

	for _, component in scc:
		if has_duplicates(component):
			print '\t>>Detected contradictions in component', component
			return False

	return True


def test_basic():
	instance = [
		(1, 1),
		(-1, -2),
		(2, -1)
	]
	result = is_2sat(instance)
	assert result == False, 'Failed basic test'
	print 'Passed all basic tests'

	instance = [
		(1, 1),
		(-1, -2),
		# (2, -1)
	]
	result = is_2sat(instance)
	assert result == True, 'Failed basic test'
	print 'Passed all basic tests'

def read_instance(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	data.pop(0)
	data = filter(bool, data)
	return [map(int, d.split()) for d in data]

def test_assignment():
	for sat in [
		'2sat1',
		'2sat2',
		'2sat3',
		'2sat4',
		'2sat5',
		'2sat6',
	]:
		input_file = 'problems/{}.txt'.format(sat)
		instance = read_instance(input_file)
		result = is_2sat(instance)

		print "Instance {}'s satisfibility: {}".format(sat, result)



if __name__ == '__main__':
	test_basic()
	test_assignment()