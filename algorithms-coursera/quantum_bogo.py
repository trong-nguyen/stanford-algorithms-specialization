"""
Silly sorting algorithm by randomly choosing a shuffled version of
the sorting array
"""

import random
import math

def not_sorted(array):
	return any([ai > aj for ai, aj in zip(array[:-1], array[1:])])
def bogus_sort(array):
	a = array
	count = 1
	while not_sorted(a):
		a = list(a)
		random.shuffle(a)
		count += 1
	print 'Array size {}, sorting takes O({:.0f}^n)'.format(len(array), math.e**(math.log(count)/len(array)))
	print 'Array {}, sorted array {}'.format(array, a)

def test():
	for i in range(10):
		n = 7
		array = random.sample(range(n*10), n)
		bogus_sort(array)

test()

