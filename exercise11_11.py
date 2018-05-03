#!/usr/bin/env python
#!-*-coding:utf-8-*-
'''
写一个使用文件名以及通过除去每行中所有排头和最尾的空白来“清洁“文件。
在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。
给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析'''
import os
def stripFile(filename):
	print 'C: Create a new clean file'
	print 'O: Overwrite the orginal file'
	choose = raw_input('Please input your choice:\n')
	if choose.lower() == 'c':
		nfilename = raw_input('Please input a new file name:')
		f = open(filename,'r')
		nf = open(nfilename,'w')
		lines = map(lambda line:line.strip(), f)
		# 列表解析
		# lines = [line.strip() for line in f]
		for line in lines:
			nf.write(line)
			nf.write(os.linesep)
		f.close()
		nf.close()
	elif choose.lower() == 'o':
		fr = open(filename,'r')
		lines = map(lambda line:line.strip(), fr)
		# 列表解析
		# lines = [line.strip() for line in f]
		fr.close()
		fw = open(filename, 'w')
		for line in lines:
			fw.write(line)
			fw.write(os.linesep)
		fw.close()
stripFile('test.txt')
