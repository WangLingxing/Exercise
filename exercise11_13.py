#!/usr/bin/env python
#!-*-coding:utf-8-*-
import time
def timeit(func, *nkwargs, **kwargs):
	try:
		start = time.time()
		retval = func(*nkwargs, **kwargs)
		end = time.time()
		result = (True, retval, end-start)
	except Exception, diag:
		result = (False, str(diag))
	return result

def mult(x, y):
	return x * y
def multB(n):
	return reduce(mult, range(1,n+1))
def myreduce(n):
	return reduce(lambda x,y:x*y, range(1,n+1))
def myiter(n):
	iterval = 1
	if n == 0 or n ==1:
		return 1
	else:
		for i in range(1,n+1):
			iterval *= i
	return iterval
def myfactor(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*myfactor(n-1)

def test():
	funcs = (myreduce, myfactor, myiter)
	vals = (4, 5, 6, 7,'9')
	for func in funcs:
		print '-'*20
		for val in vals:
			result = timeit(func, val)
			if result[0]:
				print '%s(%s) =' % (func.__name__, val),result[1]
				print 'Cost %f seconds.' % result[2]
			else:
				print '%s(%s)=FAILED:' % (func.__name__, val),result[1]


if __name__ == '__main__':
	test()

# print mult(3, 4)
# print multB(4)
# print myreduce(4)
# print myiter(4)
# print myfactor(4)