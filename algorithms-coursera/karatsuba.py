def split_at(x, idx):
	shift = 10**idx
	a = x / shift
	if a > 0:
		b = x - a * shift
	else:
		b = x
	return a, b

def karatsuba(x, y):
	if x < 10 or y < 10:
		return x * y

	nx = len(str(x))
	ny = len(str(y))

	n = max(nx, ny)
	m = (n+1)/2

	a, b = split_at(x, m)
	c, d = split_at(y, m)

	ac = karatsuba(a, c)
	bd = karatsuba(b, d)
	abcd = karatsuba(a+b, c+d)
	adbc = abcd - ac - bd

	res = 10**(2*m) * ac + 10**(m) * adbc + bd

	# print 'Computing {}*{}'.format(x, y)
	# print 'split {} into a=[{}] and b=[{}], m={}'.format(x, a, b, m)
	# print 'split {} into c=[{}] and d=[{}], m={}'.format(y, c, d, m)
	# print '\tac={}, bd={}, adbc={}'.format(ac, bd, adbc)
	# print '\tRESULT', res

	return res

def test():
	for x, y in [
		(1319, 9415),
		(3141592653589793238462643383279502884197169399375105820974944592, 
			2718281828459045235360287471352662497757247093699959574966967627),
	]:
		res = karatsuba(x, y)
		stat = 'result {}, expected {}'.format(res, x*y)
		try:
			assert res == x * y
			print stat
		except:
			print stat
			raise
test()