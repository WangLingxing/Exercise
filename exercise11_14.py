#!/usr/bin/env python
#-*-coding:utf-8-*-

def fibonacci(n):
	flist = [0,0,1]
	if n == 1 or n == 0:
		return 1
	else:
		for i in range(2,n):
			flist.append(fibonacci(i)+fibonacci(i-1))
	return flist[n]

print fibonacci(6)
