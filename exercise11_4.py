#!/usr/bin/env python
#-*-coding:utf-8-*-
# 给你在 5-13 的解创建一个补充函数。
# 创建一个带以分为单位的总时间以及 返回一个以小时和分为单位的等价的总时间。

"""
写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间。
"""
# 5-13
def changeTime(h, m):
	t = 60 * h + m
	return "Total % d minutes" %t



# new
def changeTime2(t):
	h = t / 60
	m = t % 60
	return "Time is %s Hour, %s minutes." %(h,m)

if __name__ == "__main__":
	t = raw_input("Enter HH:mm:\n")
	time = t.split(':')
	H = int(time[0])
	M = int(time[1])
	print changeTime(H, M)
	t1 = int(raw_input("Enter minutes:\n"))
	print changeTime2(t1)

