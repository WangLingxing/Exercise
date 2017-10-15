#!/usr/bin/env python
# coding:utf-8

"""
为练习 5-13 写一个姊妹函数, 接受分钟数, 返回小时数和分钟数. 
总时间不 变,并且要求小时数尽可能大
"""
def changeTime(minutes):
	M = int(minutes)
	h,m = divmod(M,60)
	return [h,m]


inp = raw_input("Input minutes:\n")
list1 = changeTime(inp)
print "%d:%d" %(list1[0],list1[1])
