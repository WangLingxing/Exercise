#!/usr/bin/env python
#!-*-coding:utf-8-*-
# (a) 写分别带两个元素返回一个较大和较小元素，
# 简单的 max2()核 min2()函数。他们应该可以用任意的 python 对象运作。
# 举例来说，max2(4,8)和 min2(4,8)会各自每次返回 8 和 4。
# (b) 创建使用了在 a 部分中的解来重构 max()和 min()的新函数 my_max()和 my_min().
# 这些函 数分别返回非空队列中一个最大和最小值。它们也能带一个参数集合作为输入。
# 用数字和字符串来 测试你的解。

max2 = lambda x,y:x if x>y else y
min2 = lambda x,y:x if x<y else y
print max2(4,8)
print min2(4,8)

def my_max(*args):
	retval = args[0]
	for i in args:
		retval=max2(retval, i)
	return retval

def my_min(*args):
	retval = args[0]
	for i in args:
		retval=min2(retval, i)
	return retval

print my_max(10,19,5)  
print my_max('a','b','c')  
print my_min(1,3,7)  
print my_min('a','b','c') 