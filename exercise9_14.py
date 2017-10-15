#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os

if sys.argv[1] == 'print':
	if os.path.exists('recordOparte.txt'):
		f = open('recordOparte.txt', 'r')
		for line in f:
			print line
		f.close()
		f1 = open('recordOparte.txt','w')
		f1.write('')
		f1.close()
	else:
		print 'No such file'
		f = open('recordOparte.txt', 'w')
		f.close()
else:
	print sys.argv[1], sys.argv[2], sys.argv[3]
	a,b = sys.argv[1], sys.argv[3]
	operation = sys.argv[2]
	expression = sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + os.linesep
	f = open('recordOparte.txt', 'a+')
	f.write(expression)

	if operation == '+':
		print float(a) + float(b)
		result = str(float(a) + float(b)) + os.linesep +os.linesep
		f.write(result)
	elif operation == '-':
		print float(a) - float(b)
		result = str(float(a) - float(b)) + os.linesep +os.linesep
		f.write(result)
	elif operation == '*':
		print float(a) * float(b)
		result = str(float(a) * float(b)) + os.linesep +os.linesep
		f.write(result)
	elif operation == '/':
		print float(a) / float(b)
		result = str(float(a) / float(b)) + os.linesep +os.linesep
		f.write(result)
	elif operation == '**':
		print float(a) ** float(b)
		result = str(float(a) ** float(b)) + os.linesep +os.linesep
		f.write(result)
	elif operation == '%':
		print float(a) % float(b)
		result = str(float(a) % float(b)) + os.linesep +os.linesep
		f.write(result)
	f.close()
