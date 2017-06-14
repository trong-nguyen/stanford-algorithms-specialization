import operator

def read_data(f):
	data = open(f, 'r').read().split('\n')
	data.pop(0)
	data = filter(bool, [map(int, d.split()) for d in data])

	return data

def schedule_by_diff(jobs):
	return sorted(jobs, key=lambda x: (x[0]-x[1], x[0]), reverse=True)

def schedule_by_fraction(jobs):
	# remember to convert weights to floats
	return sorted(jobs, key=lambda x: float(x[0])/x[1], reverse=True)

def calculate(sequence):
	if not sequence:
		return [0]

	completion_times = [0]
	for i, (weight, length) in enumerate(sequence):
		completion_times.append(completion_times[i]+length)

	return [w*c for (w,l),c in zip(sequence, completion_times[1:])]

def test_assignment():
	jobs = read_data('problems/jobs.txt')

	sequence = schedule_by_diff(jobs)
	costs = calculate(sequence)

	print 'Cost resulted from (w-d) scheduling:', sum(costs)

	sequence = schedule_by_fraction(jobs)
	costs = calculate(sequence)

	print 'Cost resulted from (w/d) scheduling:', sum(costs)

def test():
	for tc in range(1, 2+1):
		f = 'problems/jobs_input_1.txt'.replace('input_1.txt', 'input_' + str(tc) + '.txt')
		jobs = read_data(f)
		outputs = map(int, open(f.replace('input', 'output'), 'r').read().split())

		sequence = schedule_by_diff(jobs)
		costs = calculate(sequence)

		assert sum(costs) == outputs[0], 'Failed diff method, result [{}], expected [{}]'.format(sum(costs), outputs[0])

		sequence = schedule_by_fraction(jobs)
		costs = calculate(sequence)

		assert sum(costs) == outputs[1], 'Failed ratio method, result [{}], expected [{}]'.format(sum(costs), outputs[1])

		print 'Passed test case {}!'.format(tc)


test_assignment()
test()

