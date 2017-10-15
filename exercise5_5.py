#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""取一个任意小于 1 美元的金额，然后计算可以换成最少多少枚硬币。
硬币有 1 美分，5 美分，10 美分，25 美分四种。
1 美元等于 100 美分。举例来说，0.76 美元换算结果 应该是 3枚25美分，1枚1美分。
类似76枚1美分，2枚25美分+2枚10美分+1枚5美分+1
枚 1 美分这样的结果都是不符合要求的"""

cent = int(raw_input("Please enter amount between 0-99 cents："))

while cent > 0:
	if cent >= 25:
		print "need %d conts of 25 cents" %(cent/25),
		cent = cent % 25
	elif cent >= 10:
		print "need %d conts of 10 cents" %(cent/10),
		cent = cent % 10
	elif cent >= 5:
		print "need %d conts of 5 cents" %(cent/5),
		cent = cent % 5
	else:
		print "need %d conts of 1 cents" %cent,
		cent = 0