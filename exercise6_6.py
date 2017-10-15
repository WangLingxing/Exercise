#!/usr/bin/env python
# coding:utf-8
"""
创建一个 string.strip()的替代函数:接受一个字符串,去掉它前面和后面的空格
(如果使用 string.*strip()函数那本练习就没有意义了)
"""
inp = raw_input("Please input a string:")
print len(inp)
if inp[0] == ' ':
	if inp[-1] == ' ':
		inp = inp[1:-1]
	else:
		inp = inp[1:]
elif inp[-1] == ' ':
	inp = inp[:-1]
print inp,len(inp)
