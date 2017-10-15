#!/usr/bin/env python
#-*-coding:utf-8-*-

def factorial(num):
	result = 1
	for i in range(1,num+1):
		result *= i
	return result

if __name__ == '__main__':
	number = int(raw_input("Input a number:"))
 	print factorial(number) 