#!/usr/bin/env python
# -*-coding:utf-8-*-

f = open('/etc/services', 'r')
dict1 = {}
for eachline in f:
	if eachline.startswith('#'):
		continue
	elif '#' in eachline:
		index = eachline.find('#')
		eachline = eachline[:index]
	listline = eachline.split()
	if len(listline) == 2:
		dict1.setdefault(listline[0], listline[1])

for i in dict1:
	print 'Key:%s, Value:%s' %(i, dict1[i])


