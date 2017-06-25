NIDX = 1 # node index in the queue
WIDX = 0 # weight index in the queue
CIDX = 0 # code index in the queue

def get_smallest(q1, q2):
	if not q1:
		return q2.pop()
	elif not q2:
		return q1.pop()
	else:
		return q1.pop() if q1[-1] <= q2[-1] else q2.pop()

def merge(u, v, new_name):
	return (u[WIDX] + v[WIDX], new_name)

def encode_symbols(weights):
	q1 = sorted([(w, i) for i, w in enumerate(weights)], reverse=True)
	q2 = []
	longest = q1[-1][NIDX]
	shortest = q1[0] # default, likely to be changed
	merge_map = {}
	idx = len(q1) # name counter of the new nodes
	while len(q1) + len(q2) > 1:
		if len(q1) in [1,2]:
			shortest = q1[0][NIDX]

		u = get_smallest(q1, q2)
		v = get_smallest(q1, q2)
		u_node = u[NIDX]
		v_node = v[NIDX]

		# the final merge
		if not q1 and not q2:
			merge_map[u_node] = ('0', 'root')
			merge_map[v_node] = ('1', 'root')
			break

		# business as usual
		idx += 1
		w = merge(u, v, idx)
		w_node = w[NIDX]
		merge_map[u_node] = ('0', w_node)
		merge_map[v_node] = ('1', w_node)
		q2.insert(0, w)

	return {
		'map': merge_map,
		'shortest': shortest,
		'longest': longest
	}

def encode(symbol, merge_map):
	parent = merge_map[symbol]
	code = parent[CIDX]
	while parent[NIDX] != 'root':
		parent = merge_map[parent[NIDX]]
		code = parent[CIDX] + code
	return code

def test_basic():
	weights = [5, 10, 25, 27, 33]
	res = encode_symbols(weights)

	print 'merge_map', res['map']
	shortest_code = encode(res['shortest'], res['map'])
	longest_code = encode(res['longest'], res['map'])
	print 'shortest symbol: {}, code {}'.format(res['shortest'], shortest_code)
	print 'longest symbol: {}, code {}'.format(res['longest'], longest_code)

	for symbol in res['map']:
		if symbol < len(weights): # actual nodes
			print 'encoded {}: {}'.format(symbol, encode(symbol, res['map']))

	assert len(shortest_code) == 2, 'expected shortest code: {} bits'.format(2)
	assert len(longest_code) == 3, 'expected longest code: {} bits'.format(3)

def read_weights(f):
	weights = open(f, 'r').read()
	weights = map(int, weights.split())
	weights = filter(bool, weights)
	weights.pop(0)

	return weights

def read_output(f):
	res = open(f, 'r').read()
	res = map(int, res.split())
	res = filter(bool, res)

	return res[0], res[1]

def test_assignments():
	weights = read_weights('problems/huffman.txt')

	res = encode_symbols(weights)

	# print 'merge_map', res['map']
	shortest_code = encode(res['shortest'], res['map'])
	longest_code = encode(res['longest'], res['map'])
	print 'shortest symbol: {}, length {}, code {}'.format(res['shortest'], len(shortest_code), shortest_code)
	print 'longest symbol: {}, length {}, code {}'.format(res['longest'], len(longest_code), longest_code)

def test():
	for tc in [1, 2, 3]:
		f = 'problems/huffman_input_testcase_' + str(tc) + '.txt'
		output = f.replace('_input_', '_output_')
		weights = read_weights(f)
		res = encode_symbols(weights)

		# print 'merge_map', res['map']
		shortest_code = encode(res['shortest'], res['map'])
		longest_code = encode(res['longest'], res['map'])

		expected_shortest, expected_longest = read_output(output)

		assert len(shortest_code) == expected_shortest, 'Failed testcase {}, expected {} bits, result {}'.format(tc, expected_shortest, len(shortest_code))
		assert len(longest_code) == expected_longest, 'Failed testcase {}, expected {} bits, result {}'.format(tc, expected_longest, len(longest_code))

		print '... passed testcase {}: {}-{}'.format(tc, expected_shortest, expected_longest)

	print 'Passed all testcases!'



test_basic()
test_assignments()
test()

