#!/usr/bin/env python
#-*-coding:utf-8-*-

from exercise8_5 import getfactors

def isperfect(num):
	result = 0
	l = getfactors(num)
	for i in l[:-1]:
		result += i
	if result == num:
		return True
	else:
		return False

if __name__ == '__main__':
	number = int(raw_input("Input a number:"))
	print "Is perfect number?",isperfect(number)
