'''
Experiments for max lateness problem, which is a scheduling problem.
Given project time and deadlines (p,d) find the greedy algorithm that minimize the maximum lateness (li). li measured by the difference of deadlines and completion times (di - ci)
'''

def max_lateness(pd):
	end = [0]
	for i, (p, d) in enumerate(pd):
		end.append(p + end[i])

	lateness = [d-e for (p,d), e in zip(pd, end[1:])]
	# print '\t', end

	return min(lateness + [0])

import random
def test():
	# pd = [
	# 	(3,1),
	# 	(4,3),
	# 	(2,6),
	# 	(7,4),
	# ]

	pd = [(random.randrange(10,100), random.randrange(10,100)) for i in range(100)]

	results = [
		(max_lateness(sorted(pd, key=lambda x: x[1])), 'd',),
		(max_lateness(sorted(pd, key=lambda x: x[0])), 'p',),
		(max_lateness(sorted(pd, key=lambda x: x[1]*x[0])), 'p x d',),
		(max_lateness(sorted(pd, key=lambda x: x[1]-x[0])), 'p - d',),
		(max_lateness(sorted(pd, key=lambda x: x[1]+x[0])), 'p + d',),
	]

	results = sorted(results, reverse=True)

	optimal = results.pop(0)

	print 'Optimal results is by: ***{}***, lateness {}'.format(optimal[1].upper(), optimal[0])
	print 'Others:'
	print results

test()