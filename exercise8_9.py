#!/usr/bin/env python
#-*-coding:utf-8-*-

def fibonacci(index):
	a1 = 1
	a2 = 1
	a3 = 2
	if index == 1 or index == 2:
		return 1
	else:
		for i in range(3, index):
			a1 = a2 + a3
			(a1, a3) = (a3, a1)
			(a2, a1) = (a1, a2)
		return a3

if __name__ == '__main__':
	number = int(raw_input("Input times:"))
	print fibonacci(number)