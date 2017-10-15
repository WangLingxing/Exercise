#!/usr/bin/env python
# -*-coding:utf-8-*-

def display(num, filename):
	f = open(filename, 'r')
	lines = f.readlines(num)
	f.close()
	for eachline in range(num):
		print lines[eachline]

if __name__ == '__main__':
	display(1, "test.txt")
