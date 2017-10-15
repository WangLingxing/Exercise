#!/usr/bin/env python
#-*-coding:utf-8-*-

def countBySteps():
	f = int(raw_input("Input the start number:"))
	t = int(raw_input("Input the end number:"))
	increment = int(raw_input("Input the step:"))
	count = f
	while count <= t:
		print count
		count += increment

if __name__ == '__main__':
	countBySteps()