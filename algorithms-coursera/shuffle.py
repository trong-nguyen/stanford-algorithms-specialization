import random

random.seed()
m = 10
counts = [{} for i in range(m)]
for i in range(100000):
    a = range(m)
    random.shuffle(a)
    for j in range(m):
        count = counts[j]
        idx = a[j]
        count[idx] = count.get(idx, 0) + 1

import json
for d in counts:
    median = sorted(d.values())[(m-1)/2]
    print {k:'{:.0f}%'.format(100.*v/median) for k, v in d.iteritems()}