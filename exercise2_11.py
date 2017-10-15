#!/usr/bin/env python
# -*-coding:utf-8 -*-
flag = True
sum1 = 0

aver = 0

while flag:
	print "-" * 18
	print "(1)取五个数的和"
	print "(2)取五个数的平均值"
	print "(0)退出"
	print "------------------"
	choose = int(raw_input("请选择:"))
	if choose == 1:
		for i in range(5):
			a = int(raw_input("请输入数字:"))
			sum1 += a
		print "五个数之和为：%d" %sum1
		print "\n\n"
	elif choose == 2:
		for j in range(5):
			b = int(raw_input("请输入数字:"))
			sum1 += b
			aver = float(sum1)/5
		print "五个数的平均值为:",aver
		print "\n\n"
	elif choose == 0:
		flag = False
	else:
		print "输入错误，请重新输入"
