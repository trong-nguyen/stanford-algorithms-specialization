def schedule_by_product(jobs):
	return sorted(jobs, key=lambda x: x[0]*x[1])

def schedule_by_deadline(jobs):
	return sorted(jobs, key=lambda x: x[1])

def schedule_by_processing_time(jobs):
	return sorted(jobs, key=lambda x: x[0])

def calculate_lateness_cost(sequence):
	if not sequence:
		return [0]

	completion_times = [0]
	for i, (p, d) in enumerate(sequence):
		completion_times.append(completion_times[i]+p)

	return [max(c-d,0) for (p,d),c in zip(sequence, completion_times[1:])]

def test():
	import random
	n = 1000
	jobs = [(random.randint(1, 100), i+random.randint(1, 50)) for i in range(n)]

	sequence = schedule_by_product(jobs)
	costs = calculate_lateness_cost(sequence)

	print 'Cost resulted from (pxd) scheduling:', sum(costs)

	sequence = schedule_by_deadline(jobs)
	costs = calculate_lateness_cost(sequence)

	print 'Cost resulted from deadline scheduling:', sum(costs)

	sequence = schedule_by_processing_time(jobs)
	costs = calculate_lateness_cost(sequence)

	print 'Cost resulted from processing time scheduling:', sum(costs)

test()

