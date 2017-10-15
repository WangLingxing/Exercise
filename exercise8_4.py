#!/usr/bin/env python
#-*-coding:utf-8-*-

def isPrime(num):
	n = num/2
	for i in range(2,n+1):
		if num % n == 0:
			return False
	else:
		return True

if __name__ == '__main__':
	number = int(raw_input("Your input number is:"))
	print "Is prime?",isPrime(number)