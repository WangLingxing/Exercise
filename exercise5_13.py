#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间。
"""
def changeTime(h, m):
	t = 60 * h + m
	return "Total % d minutes" %t

if __name__ == "__main__":
	t = raw_input("Enter HH:mm:\n")
	time = t.split(':')
	H = int(time[0])
	M = int(time[1])
	print changeTime(H, M)