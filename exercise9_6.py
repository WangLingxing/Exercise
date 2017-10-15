#!/usr/bin/env python
# -*-coding:utf-8-*-

def compareFile(file1, file2):
	f1 = open(file1, 'r')
	lines1 = f1.readlines()
	f1.close()
	f2 = open(file2, 'r')
	lines2 = f2.readlines()
	f2.close()
	len1 = len(lines1)
	len2 = len(lines2)
	minlen = len1 if len1 <= len2 else len2
	for i in range(minlen):
		if cmp(lines1[i], lines2[i]) != 0:
			print 'row is %d ' %(i+1)
			len3 = len(lines1[i])
			len4 = len(lines2[i])
			minstr = len3 if len3 <= len4 else len4
			for j in range(minstr):
				if cmp(lines1[i][j], line2[i][j]) != 0:
					print 'column is %d ' %(j+1)
					break
			break
	else:
		print 'Two Files Same!'

