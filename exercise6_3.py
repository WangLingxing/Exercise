#!/usr/bin/env python
#! -*-coding:utf-8-*-
"""
(a) 输入一串数字,从大到小排列之.
(b) 跟 a 一样,不过要用字典序从大到小排列之.
"""

inp = raw_input("Input a string of numbers: ")
list1 = []
list2 = []

for i in inp:
	list1.append(int(i))
list2=sorted(list1,reverse=True)
print list2


key_store = []
list3 = []
while True:
	inp1 = raw_input("Input numbers,and end with # :")
	if inp1 != '#':
		key_store.append(int(inp1))
	else:
		break
list3 = sorted(key_store,reverse=True)			
print list3
