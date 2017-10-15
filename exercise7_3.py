#!/usr/bin/env python
#-*-coding:utf-8-*-

#创建一个字典，并把这个字典中的键按照字母顺序显示出来
a = {"z":1,"d":4,"y":5,"k":9,"a":2}

#sorted(a.keys())
key = a.keys()
key.sort()
print key

#(b) 现在根据已按照字母顺序排序好的键，显示出这个字典中的键和值。
for i in key:
	print "%s:%d" %(i,a[i]),
print

value = a.values()
value.sort()

print value

for key1,value1 in sorted(a.items(), key=lambda d:d[1],reverse=False):
	print key1,value1 ,

