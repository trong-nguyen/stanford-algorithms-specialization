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

def compute_distance(u, v):
	return sqrt((v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2)

def all_pair_distances(points):
	return [[compute_distance(u, v) for v in points] for u in points]

def print_tour(tour, points):
	# tour = [0, 1, 5, 4, 3, 7, 6, 8, 12, 11, 2, 9, 10, 13, 16, 17, 19, 18, 15, 14]
	S23 = [0, 1, 5, 4, 3, 7, 6, 8, 12, 11, 2, 9, 10, 13, 16, 17, 18, 21, 22, 20, 19, 14, 15, 0]
	S22 = [0, 4, 3, 2, 6, 5, 7, 10, 9, 1, 8, 11, 14, 15, 16, 19, 20, 18, 17, 12, 13, 21, 0]
	print '\n'.join([str(points[i][0]) for i in tour])
	print '\n'
	print '\n'.join([str(points[i][1]) for i in tour])

def preprocess(points, A):
	n = len(points)
	S = list(range(n))
	tour = [0]
	while True:
		k = np.argmin(A[encode(S)]) # + D[k][0]
		tour.insert(0, k)
		if k == 0 or len(tour) > n:
			break
		S = bar(S, k)
	print tour
	print_tour(tour, points)

	tour_length = sum([compute_distance(points[i], points[j]) for i, j in zip(tour[:-1], tour[1:])])
	return tour_length

	

def salesman(points):
	D = all_pair_distances(points)
	n = len(points)
	FULL_S = list(range(n))
	A = {encode([0]): [0]}
	for m in range(1, n):
		print 'Going Round', m
		for B in itertools.combinations(range(1, n), m):
			S = (0,) + B
			A[encode(S)] = [float('inf')] * n
			for j in B:
				NS = bar(S, j)
				A[encode(S)][j] = min([A[encode(NS)][k] + D[k][j] for k in NS])


	return preprocess(points, A)

def test_basic():
	pass

def read_points(f):
	data = open(f, 'r').read()
	data = data.split('\n')
	data.pop(0)
	data = filter(bool, data)
	return [map(float, d.split()) for d in data]

def read_output(f):
	return float(open(f, 'r').read())

def test_assignment():
	points = read_points('problems/tsp.txt')
	# print_tour(points)

	reduced_set = [1, 10, 24]
	reduced_neighbors = [0, 9, 23]
	points = [p for i,p in enumerate(points) if i not in reduced_set]
	tsp = salesman(points)

def test():
	for tc in ['1', '2', '3']:
		fin = 'problems/tsp_input_test_{}.txt'.format(tc)
		fout = fin.replace('input_', 'output_')
		points = read_points(fin)
		expected = read_output(fout)
		
		result = salesman(points)
		message = 'test {}, result {}, expected {}'.format(tc, result, expected)
		assert abs(result - expected) < 1e-2, 'Failed ' + message
		print 'Passed ' + message


test_assignment()
# test()