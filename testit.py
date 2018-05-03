#!/usr/bin/env python

def testit(func, *nkwargs, **kwargs):
	try:
		retval = func(*nkwargs, **kwargs)
		result = (True, retval)
	except Exception, diag:
		result = (False, str(diag))
	return result

def test():
	funcs = (int, long, float)
	vals = (1234, 12.34, '1234', '12.34')

	for eachfunc in funcs:
		print '-' * 20
		for eachval in vals:
			result = testit(eachfunc, eachval)
			if result[0]:
				print '%s(%s) =' % (eachfunc.__name__, eachval),result[1]
			else:
				print '%s(%s) =' % (eachfunc.__name__, eachval),result[1]

if __name__ == '__main__':
	test()
