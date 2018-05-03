#!/usr/bin/env python
#-*-coding:utf-8-*-
def average(list1):
	return reduce(lambda x,y:x+y, list1)/len(list1) 

l = [1,2,3,4,5,6,7,8]
print average(l)