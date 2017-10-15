#!/usr/bin/env python
#-*-coding:utf-8-*-

# 颠倒字典中的键和值。
# 用一个字典做输入，输出另一个字典，用前者的键做值，前者的 值做键。
def dictValueToKey(dict1):
	dict2 = {}
	for key,value in dict1.items():
		dict2.update({value:key})
	print dict1,'=>',dict2
	return dict2 

if __name__ == '__main__':
	dict1 = {1:"x",2:"y",3:"z"}
	dictValueToKey(dict1)
