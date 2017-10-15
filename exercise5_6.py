#!/usr/bin/env python
#-*-coding:utf-8-*-
"""写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符:
N1 运算符 N2"""

equation = raw_input("Please enter equation like N1 operator N2:\n")
n = equation.split(" ")
if n[1] == '+':
    print (int(n[0]) + int(n[2]))
elif n[1] == '-':
	print (int(n[0]) - int(n[2]))
elif n[1] == '*':
	print (int(n[0]) * int(n[2]))
elif n[1] == '/':
	print (int(n[0]) / int(n[2]))
elif n[1] == '**':
	print (int(n[0]) ** int(n[2]))
