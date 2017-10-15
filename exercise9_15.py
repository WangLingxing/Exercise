#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

file1 = raw_input('Input copied file name:')
file2 = raw_input('Input copy file name:')

f1 = open(file1, 'r')
f2 = open(file2, 'a+')

f2.write(os.linesep)

for line in f1:
	f2.write(line)

f1.close()
f2.close()