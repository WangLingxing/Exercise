#!/usr/bin/env python
# -*-coding:utf-8-*-
import os

def display25(filename):
	f = open(filename, 'r')
	n = 0
	for i in f:
		print i,
		n += 1
		if n == 25:
			n = 0
			pause = raw_input("按任意键继续.")
	f.close()

if __name__ == '__main__':
	display25("userpw2.py")




