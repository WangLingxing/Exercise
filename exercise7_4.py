#!/usr/bin/env python
#-*-coding:utf-8-*-

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

#1
d1 = {}
for i in range(len(a)):
	d1[a[i]] = b[i]
print d1

#2
d2 = {}
for i,x in enumerate(a):
	d2[x] = b[i]
print d2

#3
d3 = dict(map(None, a, b))
print d3

#4
d4 = dict(zip(a, b))
print d4