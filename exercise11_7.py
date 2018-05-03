#!/usr/bin/env python
#-*-coding:utf-8-*-

def combine(list1, list2):
	if len(list1) != len(list2):
		print "Length of lists must be equal!"
	else:
		print map(None, list1, list2)
		print zip(list1,list2)

combine([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
