#!/usr/bin/env python
# -*-coding:utf-8-*-

def lines(filename):
	f = open(filename, 'r')
	line = f.readlines()
	f.close()
	print len(line)

if __name__ == '__main__':
	lines("test.txt")