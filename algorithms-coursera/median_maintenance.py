import heapq

def maintenance(stream):
	if len(stream) < 2:
		return stream

	def max_low(h):
		# peek value of the low heep
		return -h[0]
	def min_high(h):
		return h[0]
	def insert_low(h, i):
		heapq.heappush(h, -i) # max heap
	def insert_high(h, i):
		heapq.heappush(h, i)

	def balance(low, high):
		if len(low) > len(high) + 1:
			insert_high(high, -heapq.heappop(low))
		elif len(high) > len(low):
			insert_low(low, heapq.heappop(high))

	# init phase
	ab = sorted(stream[:2])
	low_heap = [-ab[0]]
	high_heap = [ab[1]]
	medians = [stream[0], ab[0]] # so crucial

	for i, e in enumerate(stream[2:]):
		if e < min_high(high_heap):
			insert_low(low_heap, e)
		else:
			insert_high(high_heap, e)

		# balancing
		balance(low_heap, high_heap)

		# thanks to balance and convention (low size >= high size)
		# the current median is always the max of low heap
		medians.append(max_low(low_heap))
		# print 'medians \n\t{}'.format(medians)
		# print 'stream\n\t{}'.format(sorted(stream[:i+3]))
		# print '\t{} {}\n'.format(low_heap, high_heap)

	return medians


def test_basic():
	stream = [1, 2, 3, 9, 0, 5]
	expected = [1, 1, 2, 2, 2, 2]

	result = maintenance(stream)
	assert result == expected, 'Failed basic test!, result {}, expected {}'.format(result, expected)

def read_stream(f):
	data = open(f, 'r').read()
	return map(int, data.split())

def read_output(f):
	return int(open(f, 'r').read())

def test_assignment():
	file = 'problems/median.txt'
	stream = read_stream(file)

	result = maintenance(stream)
	print result[:20]
	print 'Answer is {}'.format(sum(result) % 10000)

def test():
	import os
	folder = 'tests/course2/assignment3Median'
	test_cases = os.listdir(folder)
	test_cases = filter(lambda f: 'input_' in f, test_cases)
	for tc in test_cases:
	# for tc in ['input_random_4_10.txt']:
		input_file = os.path.join(folder, tc)
		output_file = input_file.replace('input_', 'output_')
		expected = read_output(output_file)
		stream = read_stream(input_file)

		result = maintenance(stream)
		modulo = sum(result) % 10000
		message = 'Failed test case {}, result {} expected {}'.format(tc,modulo, expected)
		try:
			assert expected == modulo, message
			print 'Passed test case {}'.format(tc)
		except AssertionError:
			print message

test_basic()
test_assignment()
test()