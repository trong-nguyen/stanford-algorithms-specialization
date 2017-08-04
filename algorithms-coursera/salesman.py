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


def compute_path_length(path, points):
	return sum([compute_distance(points[i], points[j]) for i, j in zip(path[:-1], path[1:])])

def all_pair_distances(points):
	return [[compute_distance(u, v) for v in points] for u in points]

def print_tour(tour, points):
	"""
	just a hack for easy copying to Excel columns
	"""
	print '\n'.join([str(points[i][0]) for i in tour])
	print '\n'
	print '\n'.join([str(points[i][1]) for i in tour])

def postprocess(points, A, D):
	n = len(points)
	S = list(range(n))
	tour = [0]
	while True:
		code = encode(S)
		j = np.argmin([A[code][k] + D[k][tour[0]] for k in range(len(A[code]))])
		tour.insert(0, j)
		if j == 0 or len(tour) > n:
			break
		S = bar(S, j)
	print tour
	print_tour(tour, points)

	tour_length = compute_path_length(tour, points)
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

	return postprocess(points, A, D)

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

def pertube(points, solution, pertubed_nodes):
	"""
	Approximate the TSP problem by greedy method
	solution is the solution to the reduced TSP problem
	pertubed_nodes is the dict that saves which nodes were excluded and to 
	which nodes they are related to (in the same cluster)
	"""
	def avoid_head(idx):
		return -1 if idx == 0 else idx
	
	new_solution = list(solution)
	for node, per_node in pertubed_nodes.items():
		idx = new_solution.index(node)

		insert_before_path = list(new_solution)
		insert_before_path.insert(avoid_head(idx), per_node)
		pre = compute_path_length(insert_before_path, points)

		insert_after_path = list(new_solution)
		insert_after_path.insert(idx+1, per_node)
		post = compute_path_length(insert_after_path, points)

		insert_position = avoid_head(idx if pre <= post else idx + 1)

		new_solution.insert(insert_position, per_node)

	return new_solution


def test_assignment():
	points = read_points('problems/tsp.txt')

	reduced_set = [1, 10, 24]
	reduced_neighbors = [0, 9, 23]
	points = [p for i,p in enumerate(points) if i not in reduced_set]
	tsp = salesman(points)

	# tsp = salesman(points)

	def tsp_with_pertubed_clusters():
		pertubed_nodes = {0: 1, 9: 10, 23: 24}
		solution = [0, 5, 9, 11, 14, 18, 17, 21, 22, 20, 16, 19, 23, 15, 13, 12, 8, 6, 2, 3, 7, 4, 0] # solved solution
		new_solution = pertube(points, solution, pertubed_nodes)
		print new_solution
		print 'Approximated path length of TSP problem: {}'.format(compute_path_length(new_solution, points))
		print_tour(new_solution, points)

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

if __name__ == '__main__':
	test()
	test_assignment()