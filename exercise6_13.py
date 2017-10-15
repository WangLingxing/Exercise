#!/usr/bin/env python
# coding:utf-8

"""
实现一个,atoc(),接受单个字符串做参 数输入,一个表示复数的字符串,
例如,'-1.23e+4-5.67j',返回相应的复数对象.
你不能用 eval()函 数,但可以使用 complex()函数,
而且你只能在如下的限制之下使用 complex():complex(real,imag)
的 real 和 imag 都必须是浮点值.
"""
import string

def atoc(string):
	if 'j' not in string:
		real = string
		print real
		return complex(real)
	else:
		for i in range(len(string))[::-1]:
			if string[i] in ['+','-']:
				real,imag = float(string[:i]),float(string[i+1:-1])
				print real,imag
				break
		return complex(real,imag)

inp = raw_input("Input a complex string:\n")
print atoc(inp)