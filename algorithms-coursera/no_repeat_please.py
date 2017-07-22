from itertools import permutations
from math import factorial
import operator
import re

def brute_repeat(s):
	pm = map(''.join, list(permutations(s)))
	r = re.compile(r'(.)\1{1,}')
	repeats = filter(r.search, pm)
	return len(pm) - len(repeats)

def groupify(s):
	groups = {}
	for c in s:
		groups[c] = groups.get(c, 0) + 1

	return groups

def no_repeat(s):
	groups = groupify(s)
	repeat_groups = {k:v for k, v in groups.iteritems() if v >= 2}
	identical_groups = {k:v for k, v in groups.iteritems() if k not in repeat_groups}
	if len(repeat_groups) > 2:
		raise 'Not ready'

	n = len(s)
	if len(repeat_groups) == 1:
		na = repeat_groups.values()[0]

		total = 0
		for i in range(2, na+1):
			t = factorial(i) * factorial(n-na+1 + (na-i>0)) * (1 if na-i<0 else factorial(na-i))
			total += t
			print 't {}, [repeat] {}, [remain] {}, groups {}'.format(t, i, na-i, n-na+1 + (na-i>0))
		return factorial(n) - total


	if len(repeat_groups) == 2:
		na, nb = repeat_groups.values()



def test():
	for s in ['aa', 'aab', 'aaab', 'aaaabcd', 'abcdefa', 'aaabcdef', 'aaaacde', 'zzzzz']:
		print 'There are {} non-repeats of {}'.format(no_repeat(s), s)
		print '\t fact: {} non-repeats'.format(brute_repeat(s))
		print '---'

test()