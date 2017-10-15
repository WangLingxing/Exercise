#!/usr/bin/env python
#-*-coding:utf-8-*-
from exercise8_4 import isPrime
from exercise8_5 import getfactors


def fenjie(number):
	primelist = []
	result = []
	for i in getfactors(number):
		if isPrime(i):
			primelist.append(i)
	while number is not 1:
		for i in primelist[::-1]:
			if number % i == 0:
				number = number / i
				result.append(i)
				break
	return result

if __name__ == '__main__':
	num = int(raw_input("Input a number:"))
	print fenjie(num)


