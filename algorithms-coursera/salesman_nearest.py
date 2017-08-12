import itertools
import math
from math import sqrt
import numpy as np

def compute_distance(u, v):
	return sqrt((v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2)

def compute_distance2(u, v):
	return (v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2

def compute_path_length(path, points):
	return sum([compute_distance(points[i], points[j]) for i, j in zip(path[:-1], path[1:])])

class Lookup(object):
	"""Lookup class using window clusters to search for nearest points"""
	def __init__(self, points):
		self.points = points

		xs = [p[0] for p in points]
		ys = [p[1] for p in points]
		xlim = (min(xs), max(xs))
		ylim = (min(ys), max(ys))

		xlen = xlim[1] - xlim[0]
		ylen = ylim[1] - ylim[0]

		self.ds = ds = int(max(xlen, ylen) / math.sqrt(len(points))) * 8

		self.x0 = xlim[0] - 0.5*ds
		self.y0 = ylim[0] - 0.5*ds

		lookup = {}
		for i, p in enumerate(points):
			idx = self.to_index(p)
			lookup[idx] = lookup.get(idx, []) + [i]

		self.lookup = lookup

		self.popped = []


	def to_index(self, point):
		return (int((point[0] - self.x0) / self.ds), int((point[1] - self.y0) / self.ds))

	def remove_id(self, i):
		u, v = self.to_index(self.points[i])
		self.lookup[(u,v)].remove(i)
		self.popped.append(i)

	def pop_nearest(self, idx):
		p = self.points[idx]
		i, j = self.to_index(p)

		rmax = 50
		step = 1
		for r in range(1, rmax, step):
			ids = []
			for di in range(-r, r+1):
				for dj in range(-r, r+1):
					u, v = (i+di), (j+dj)
					slot = self.lookup.get((u,v), [])
					if slot:
						ids += [k for k in slot if k != idx]
			if ids:
				distances = map(lambda k: (compute_distance2(p, self.points[k]), k), ids)
				_, k = min(distances) # first by distance, then by k
				self.remove_id(k)
				return k

		print "Can't find a point within rmax={} for point with index {}, should raise it higher".format(rmax, idx)
		print 'Doing brute force with set size {}'.format(len(self.points) - len(self.popped))

		ids = set(range(len(self.points))).difference(self.popped)
		distances = [(compute_distance(p, self.points[k]), k) for k in ids if k != idx]
		_, k = min(distances) # first by distance, then by k
		self.remove_id(k)

		return k

class BruteLookup(object):
	"""Lookup class using brute force to search for nearest points"""
	def __init__(self, points):
		super(BruteLookup, self).__init__()
		self.points = points
		self.lookup = set(range(len(points)))

	def pop_nearest(self, idx):
		_, k = min([(compute_distance2(self.points[idx], self.points[i]), i) for i in self.lookup])
		self.remove_id(k)
		return k

	def remove_id(self, idx):
		self.lookup.remove(idx)

def salesman(points):
	lookup = Lookup(points)
	tour = [0]
	lookup.remove_id(0)

	while len(tour) != len(points):
		try:
			nearest = lookup.pop_nearest(tour[-1])
		except ValueError as e:
			print 'Error! Current tour length {} / total length {}'.format(len(tour), len(points))
			raise
		if nearest != 0:
			tour.append(nearest)

		if len(tour) % 1000 == 0:
			print 'Tour', len(tour)

	return tour + [0]

def test_basic():
	pass

def read_points(f, coord_idx=0):
	data = open(f, 'r').read()
	data = data.split('\n')
	data.pop(0)
	data = filter(bool, data)
	return [map(float, d.split()[coord_idx:]) for d in data] #remove first indices

def read_output(f):
	return float(open(f, 'r').read())

def test_assignment():
	points = read_points('problems/nearest_neighbor_tsp.txt', coord_idx=1) # coordinate starts after index

	tour = salesman(points)
	result = compute_path_length(tour, points)

	print 'Heuristic Salesman Problem by Nearest Neighbor: total distance {}'.format(result)

	# # visualize data points
	# data = 'x y\n' + '\n'.join([' '.join(map(str, points[i])) for i in tour])
	# with open('nn_salesman.txt', 'w') as f:
	# 	f.write(data)

def test():
	for tc in ['1', '2', '3']:
		fin = 'problems/tsp_input_test_{}.txt'.format(tc)
		fout = fin.replace('input_', 'output_')
		points = read_points(fin)
		expected = read_output(fout)
		
		tour = salesman(points)
		result = compute_path_length(tour, points)
		message = 'test {}, result {}, expected {}, tour {}'.format(tc, result, expected, tour)
		assert abs(result - expected) < 1e-2, result
		print 'Passed ' + message

if __name__ == '__main__':
	test()
	test_assignment()