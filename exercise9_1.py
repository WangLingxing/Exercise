#!/usr/bin/env python
# -*-coding:utf-8-*-

f = open("test.txt", 'r')
for eachline in f:
	if eachline.startswith('#'):
		continue
	elif '#' in eachline:
		index = eachline.find('#')
		print eachline[:index],
		continue
	print eachline,


