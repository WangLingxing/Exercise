#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数。
"""

a = int(raw_input("Input number a:\n"))
b = int(raw_input("Input number b:\n"))
tmp = 0
product = a * b

if a < b:
	tmp = a
	a = b
	b = tmp


while True:
	c = a % b
	if c == 0:
		print "Greatest common divisor is %d" % b
		break
	else:
		a = b
		b = c

print "Least common multiple is %d" %(product/b)