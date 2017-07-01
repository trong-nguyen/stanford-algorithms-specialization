GAP_PENALTY = 1
MATCH_PENALTY = 0

def preprocess(x, y):
	# this algorithm considers a zero-matching possibility
	return '_' + x, '_' + y

def sequence(x, y):
	x, y = preprocess(x, y)

	m = len(x)
	n = len(y)
	A = [[0]*n for i in range(m)]
	for i in range(n):
		A[0][i] = i * GAP_PENALTY
	for i in range(m):
		A[i][0] = i * GAP_PENALTY

	p = [GAP_PENALTY, MATCH_PENALTY]
	for i in range(1, m):
		for j in range(1, n):
			c1 = p[x[i] == y[j]] + A[i-1][j-1]
			c2 = GAP_PENALTY + A[i-1][j]
			c3 = GAP_PENALTY + A[i][j-1]
			A[i][j] = min([c1, c2, c3])

	return A

def print_cache(A, sx, sy):
	sx, sy = preprocess(sx, sy)
	legible_A = [[sx[i], ''] + ai for i, ai in enumerate(A)]
	legible_A.insert(0, ['', 'y'] + [c for c in sy])
	legible_A.insert(1, ['x'] + [''] * (len(legible_A[0])-1))

	n = len(legible_A)
	W = len(legible_A[0])
	for x in range(0, W):
		print ''.join(['{:>4}'.format(legible_A[i][x]) for i in range(n)])

def retrieve(x, y, A):
	# retrieve the knap-ed items
	x, y = preprocess(x, y)
	i = len(x) - 1
	j = len(y) - 1

	penalty = A[i][j]
	p = [GAP_PENALTY, MATCH_PENALTY]
	mx = ''
	my = ''
	penalty = A[i][j]
	while i > 0 or j > 0:
		v = A[i][j]

		route_1 = p[x[i] == y[j]] + A[i-1][j-1]
		route_2 = GAP_PENALTY + A[i-1][j]
		route_3 = GAP_PENALTY + A[i][j-1]

		if v == route_1:
			# both matched / unmatched case
			cx, cy = x[i], y[j]
			i -= 1
			j -= 1
		elif v == route_2:
			cx = x[i]
			cy = '_'
			i -= 1
		elif v == route_3:
			cx = '_'
			cy = y[j]
			j -= 1

		if cx != cy:
			cx = '({})'.format(cx)
			cy = '({})'.format(cy)
		mx = cx + mx
		my = cy + my

	# visual processing
	mx = mx.replace(')(', '')
	my = my.replace(')(', '')

	return mx, my, penalty

def test_basic():
	for tc, (x, y, expected_penalty) in enumerate([
		('abcde', 'cce', 3),
		('abcde', 'ace', 2),
		('xyzwvu', 'xyzwvu', 0),
		('abcd', 'ace', -1),
		('lksajdhf902uklajsdfpoiwer', 'abcde;laksdf902734h', -1),
		(';lkasdfoiu2098374kjhsdlfkup29834hsakfdjh9823', 'kalshjfdpoiuer987123hfskdjlhfliuasyf98234', -1),
	]):

		print '\n---------------------\nTEST NUMBER', tc+1

		A = sequence(x, y)

		if len(A[0])<30:
			# prevent printing excessively big A
			print_cache(A, x, y)

		mx, my, pe = retrieve(x, y, A)

		print 'Matching pattern costs [{}/{}] penalty, () and _ mean mismatched and gap insertion, respectively:\n\t{}\n\t{}'.format(pe, max(len(x), len(y)), mx, my)
		if expected_penalty >= 0:
			assert pe == expected_penalty, 'Failed, expected penalty {}, result'.format(expected_penalty, pe)

	print '\nPassed all basic tests!'
test_basic()
