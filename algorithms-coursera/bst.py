# BUILD OPTIMAL BINARY SEARCH TREE FOR SEARCHING WITH STATISTICS

def bst(p):
	n = len(p)
	A = [[0]*n for i in range(n)]
	for s in range(n):
		for i in range(n):
			j = i+s
			if j >= n:
				continue
			# print 'j={}'.format(j)
			m = 1e6
			for r in range(i, j+1):
				v = sum(p[i:j+1])
				if i <= r-1:
					v += A[i][r-1]
				if r+1 <= j:
					try:
						v += A[r+1][j]
					except IndexError:
						print 'r+1={}, i={}, j={}, n={}'.format(r+1, i, j, n)
						raise

				m = min(m, v)
			A[i][j] = m

	return A

def print_bst(A):
	n = len(A)
	for i in range(n-1, -1, -1):
		print ''.join( ['{:2}\t\t'.format(i)] + ['{:4}  '.format(A[j][i]) for j in range(n)])

	print '\n'
	print '{:2}\t\t'.format('j/i') + ''.join(['{:4}  '.format(j) for j in range(n)])

def test_basic():
	p = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
	A = bst(p)
	print_bst(A)

test_basic()