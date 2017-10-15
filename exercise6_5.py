#!/usr/bin/env python
# coding:utf-8
"""
(a)更新你在练习 2-7 里面的方案,使之可以每次向前向后都显示一个字符串的一个字符. 
(b)通过扫 来判断两个字符串是否匹配(不能使用比较操作符或者 cmp()内建函数)。附加题:
在你的方案里加入大小写区分. 
(c)判断一个字符串是否重现(后面跟前面的一致).附加题:在处理除了严格的回文之外,加入对
例如控制符号和空格的支持。 
(d)接受一个字符,在其后面加一个反向的拷贝,构成一个回文字符串.
"""
#(a)
inp = raw_input("Please input a string:")

for i in inp:
	print i

print "----reverse----"
for j in inp[::-1]:
	print j

#(b)
inp1 = raw_input("Input string1:")
inp2 = raw_input("Input string2:")
if len(inp1) != len(inp2):
	print "string1 is not equal than string2!"
else:
	for i in range(len(inp1)):
		if inp1[i] != inp2[i]:
			print "string1 is not equal than string2!"
			break
	else:
		print "string1 is equal than string2!"

#(c)
inph = raw_input("Input string:")
if len(inph) % 2 != 0:
	print "String is not a huiwen"
i = len(inph) / 2
str1 = inph[:i]
str2 = inph[i:][::-1]
print str1,str2
for j in range(i):
	if str1[j] != str2[j]:
		print "String is not a huiwen"
		break
else:
	print "String is a huiwen"

#(d)
inpf = raw_input("Input a string:")
strf = inpf[::-1]
huiwen = inpf+strf
print huiwen