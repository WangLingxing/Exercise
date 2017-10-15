#!/usr/bin/env python
#-*-coding:utf-8-*-

def getfactors(num):
	l = []
	for i in range(1,num+1):
		if num % i ==0:
			l.append(i)
	return l

if __name__ == '__main__':
	print getfactors(20)
