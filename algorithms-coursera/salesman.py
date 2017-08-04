import itertools
from math import sqrt
import numpy as np

def encode(S):
	"""
	encode S into an integer whose binary representations has
	bit indices in S set to 1

	ex: S = [1,3] -> need to set bits 1 and 3, should return 0b1010
	i = 1: x = 0, (1 << i) = 0b10
	i = 3: x = 0b10, (3 << i) = 0b1000 => x | 3 << i should be 0b1010
	"""
	return reduce(lambda x, y: x | 1 << y, S)

def encode_bar(S, j):
	"""
	get the full encoded S
	clear bit j if it was set in S
	1 << j is to set bit j to 1: ex 001000
	~(1 << j) then inverse: ex      110000
	then do an AND with the original, only when the bit in the original x was set should it be clear
	"""
	return encode(S) & ~(1 << j)

def bar(S, x):
	return [i for i in S if i != x]

def all_pair_distances(points):
	dist = lambda u, v: sqrt((v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2)
	return [[dist(u, v) for v in points] for u in points]


def salesman(points):
	D = all_pair_distances(points)
	n = len(points)
	FULL_S = list(range(n))
	A = {encode([0]): [0]}
	for m in range(1, n):
		for B in itertools.combinations(range(1, n), m):
			S = (0,) + B
			A[encode(S)] = [float('inf')] * n
			for j in B:
				NS = bar(S, j)
				A[encode(S)][j] = min([A[encode(NS)][k] + D[k][j] for k in NS])

	# print np.argmin(A[encode(FULL_S)])
	tour = []
	S = FULL_S
	while True:
		k = np.argmin(A[encode(S)])
		tour.insert(0, k)
		if k == 0 or len(tour) > n:
			break
		S = bar(S, k)
	print tour

def test_basic():
	pass

def read_points(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	data.pop(0)
	data = filter(bool, data)
	return [map(float, d.split()) for d in data]

def test_assignment():
	points = read_points('problems/tsp.txt')
	tsp = salesman(points[:20])

test_assignment()