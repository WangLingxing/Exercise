#!/usr/bin/env python
#-*-coding:utf-8-*-

def nametrack(times):
	result = []
	count = 0
	for i in range(times):
		print "Please enter name %d" % i
		name = raw_input()
		if ',' in name:
			result.append(name)
		else:
			count += 1
			print "Wrong format... should be Last, First."
			print "You have done this %d time(s) already. Fixing input... " % count
			name = name.split()
			result.append(name[0] + ',' + name[1])
	return sorted(result)

if __name__ == '__main__':
	num = input('Enter total number of names:') 
	names = nametrack(num)
	for i in names:
		print i


