# BUILD OPTIMAL BINARY SEARCH TREE FOR SEARCHING WITH STATISTICS

def bst(p):
	# naive_root_evals = 0
	# knuth_root_evals = 0
	n = len(p)

	A = [[0]*n for i in range(n)] # search cost matrix, A[i][k] corresponding to optimal search cost of problem size [i:j] inclusive
	R = [[0]*n for i in range(n)] # optimal root node matrix, R[i][j]  corresponding to optimal root of problem size [i:j] inclusive
	for s in range(n):
		for i in range(n):
			j = i+s
			if j >= n:
				continue
			# print 'j={}'.format(j)
			m = float('inf')
			optimal_root = None
			# Knuth's optimization
			if i == j:
				root_range = range(i, j+1)
			else:
				root_range = range(R[i][j-1], R[i+1][j] + 1)

			# if i != j:
			# 	r0 = (i, j)
			# 	r1 = (R[i][j-1], R[i+1][j])
			# 	naive_root_evals += r0[1] - r0[0] 
			# 	knuth_root_evals += r1[1] - r1[0]
			# 	print 'Saved {} root evals, range [{}] vs [{}]'.format(r0[1] - r0[0] - (r1[1] - r1[0]), r1, r0)

			for r in root_range:
				v = sum(p[i:j+1])
				if i <= r-1:
					v += A[i][r-1]
				if r+1 <= j:
					v += A[r+1][j]
				if v < m:
					m = v
					optimal_root = r
			A[i][j] = m
			R[i][j] = optimal_root

	# print 'Saved total {}%, n2={}'.format((naive_root_evals - knuth_root_evals) * 100 / naive_root_evals, n**2)
	return A, R

def render_tree(R, bound, current_depth=0):
	# compute the coordinates x, y of the tree from the optimal root matrix R
	# whereas x = indent, y = depth
	# for ASCII printing
	def size(bound):
		return bound[1] - bound[0]

	i, j = bound
	j -= 1 # 0-based index

	root = R[i][j]
	indent = root

	T1 = [i, root]
	T2 = [root+1, j+1]
	
	res = []
	# left branch
	if size(T1) > 0:
		res += render_tree(R, T1, current_depth+1)

	# root
	res += [(indent, current_depth, root)]

	# right branch
	if size(T2) > 0:
		res += render_tree(R, T2, current_depth+1)

	return res

def draw_tree(nodes):
	n = len(nodes)

	space = [['']*n for i in range(n)]
	max_chars = max([len(str(x[-1])) for x in nodes])
	str_format = '{{:^{}}} '.format(max_chars)

	for i, j, label in nodes:
		space[i][j] = label

	for j in range(n):
		print ''.join([str_format.format(space[i][j]) for i in range(n)])


def print_2d_array(A):
	n = len(A)
	for i in range(n-1, -1, -1):
		print ''.join( ['{:2}\t\t'.format(i)] + ['{:4}  '.format(A[j][i]) for j in range(n)])

	print '\n'
	print '{:2}\t\t'.format('j/i') + ''.join(['{:4}  '.format(j) for j in range(n)])

def test_basic():
	p = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
	# p = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23, 0.3, 0.4, 0.6, 0.09, 0.75, 0.24]
	# p = range(100)
	A, R = bst(p)

	tree_nodes = render_tree(R, (0, len(R)))
	draw_tree(tree_nodes)

	if len(A) < 30:
		print_2d_array(A)
		print '\n\n'
		print_2d_array(R)

	if p == [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]:
		assert abs(A[0][len(A)-1] - 2.18) < 1e-3, 'Expected 2.18 +- 1e-3'

test_basic()