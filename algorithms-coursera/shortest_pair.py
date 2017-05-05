def compute_distance(p1, p2):
	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]
	return float(dx * dx + dy * dy)

def make_pairs(points):
	pairs = []
	for i, p in enumerate(points):
		pairs += [(p, pi) for pi in points[i+1:]]

	return pairs

def get_shortest_pair(pairs):
	pd = [(compute_distance(*pair), pair) for pair in pairs]
	return min(pd)[1]

def find_split_shortest_pair(stride, delta):
	# stride is sorted by y coordinate
	k = 7 # number of following points need to check in the rectangle [-delta, +delta] by [delta]
	shortest_pair = None
	for i, p in enumerate(stride[:-1]): # -1 to allow atleast 1 pair in the final iteration
		pairs = [(p, pi) for pi in stride[i+1:i+1+k+1]] # the next 7 points from i+1
		current_shortest = get_shortest_pair(pairs)
		current_shortest_distance = compute_distance(*current_shortest)
		if current_shortest_distance < delta:
			shortest_pair = current_shortest
			delta = current_shortest_distance
	return shortest_pair

def find_shortest_pair_by_bruteforce(points):
	return get_shortest_pair(make_pairs(points))

def find_shortest_pair(points):
	sorted_by_x = sorted(points, key=lambda p: p[0])
	sorted_by_y = sorted(points, key=lambda p: p[1])
	return _find_shortest_pair(sorted_by_x, sorted_by_y)

import sys
def _find_shortest_pair(px, py):
	n = len(px)

	if n == 3: # constant 3 could be tuned to represent a switch from bruteforce to SMART
		return find_shortest_pair_by_bruteforce(px)
	elif n == 2:
		return px
	elif n < 2:
		return None

	# divide
	x_bar = px[n/2][0]

	# Note: this partition strategy based on coordinates doesnot work if duplicates exist
	# filter(lambda x: x[0] <= x_bar, px)
	# filter(lambda x: x[0] > x_bar, px)

	# However: this works, funny that px and py in this partition neednot contain the same set of points! 
	# WHAT?!! Yeah, it still works!
	left_px = px[:n/2 + 1] 
	right_px = px[n/2 + 1:] 

	left_py = filter(lambda x: x[0] <= x_bar, py)
	right_py = filter(lambda x: x[0] > x_bar, py)
	# conquer
	left_pair = _find_shortest_pair(left_px, left_py)
	right_pair = _find_shortest_pair(right_px, right_py)

	# This check is crucial to make the algorithm work
	if not left_pair:
		return right_pair
	elif not right_pair:
		return left_pair

	shortest_pair = get_shortest_pair([left_pair, right_pair])
	delta = compute_distance(*shortest_pair)
	stride = filter(lambda p: abs(p[0] - x_bar) <= delta, py) # ta-da, recipe here

	split_pair = find_split_shortest_pair(stride, delta)

	# combine
	return split_pair if split_pair else shortest_pair

def test():
	points = [(0,0), (0,1), (1,0), (1,1), (1.5, 1.5)]
	print find_shortest_pair(points)

	points = [(0,0), (0,1), (1,0), (1,1), (1.5, 1.5), (1.6, 1.6)]
	print find_shortest_pair(points)

	points = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (2,2), (1,2)]
	print find_shortest_pair(points)

	# two uniform grids, coarser on the left, finer on the right, smallest at boundary
	points = [(0,2), (0,3), (1,2), (1,3), (1.1,0), (3.1,0), (1.1,3), (3.1,3)]
	print find_shortest_pair(points)

	# extreme - degenerated to 1d in x
	points = [(0,0), (0,1), (0,2), (0,4), (0,3), (0,9)]
	print find_shortest_pair(points)

	# extreme - degenerated to 1d in y
	points = [(0,0), (1,0), (2,0), (4,0), (3,0), (9,0)]
	print find_shortest_pair(points)


test()