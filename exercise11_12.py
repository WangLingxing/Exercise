#!/usr/bin/env python
#!-*-coding:utf-8-*-
import time
def timeit(func, *nkwargs, **kwargs):
	try:
		time_start = time.time()
		retval = func(*nkwargs, **kwargs)
		time_end = time.time()
		result = (True, retval, time_end-time_start)
	except Exception, diag:
		result = (False, str(diag))
	return result

def test():
	funcs = (int, long, float)
	vals = (1234, 12.34, '1234', '12.34')

	for func in funcs:
		print '-' * 20
		for val in vals:
			result = timeit(func, val)
			if result[0]:
				print '%s(%s) =' % (func.__name__, val),result[1]
				print 'Cost %f seconds.' % result[2]
			else:
				print '%s(%s) =' % (func.__name__, val),result[1] 

if __name__ == '__main__':
	test()
