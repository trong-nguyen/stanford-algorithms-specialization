def max_weight_set(weights):
	accumulated_weight = [0] * len(weights)
	accumulated_weight[0] = weights[0]
	accumulated_weight[1] = max(accumulated_weight[0], weights[1])
	for i in range(2, len(accumulated_weight)):
		accumulated_weight[i] = max(weights[i] + accumulated_weight[i-2], accumulated_weight[i-1])

	return accumulated_weight

def retrieve_set(accumulated_weight):
	selected = [0] * len(accumulated_weight)

	i = len(accumulated_weight) - 1
	while i >= 1:
		if accumulated_weight[i] == accumulated_weight[i-1]:
			selected[i] = 0
			i -= 1
		else:
			selected[i] = 1
			i -= 2

	selected[0] = int(not selected[1])

	return selected


def test_basic():
	weights = [0, 1, 6, 5, 98, 4, 5, 4, 3, 99] 

	accu_weight = max_weight_set(weights)
	expected = [1, 0, 1, 0, 1, 0, 1, 0, 0, 1]
	res = retrieve_set(accu_weight)
	assert res == expected, 'Failed, expected {}, result {}'.format(expected, res)
	print 'Passed basic tests\n';


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
	weights = read_weights('problems/mwis.txt')

	accu_weight = max_weight_set(weights)
	max_set = retrieve_set(accu_weight)

	sample = [i-1 for i in [1, 2, 3, 4, 17, 117, 517, 997]] #base 0
	print '8bits sample test selection is {}'.format(''.join([str(max_set[i]) for i in sample]))
	print 'Passed assignment tests\n';

test_basic()
test_assignments()
