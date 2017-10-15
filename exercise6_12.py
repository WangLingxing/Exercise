#!/usr/bin/env python
# coding:utf-8

"""
(a)创建一个名字为 findchr()的函数,函数声明如下:
     def findchr(string, char)
findchr()要在字符串 string 中查找字符 char,
找到就返回该值的索引,否则返回-1.
不能用 string.*find()或者 string.*index()函数和方法

(b)创建另一个叫 rfindchr()的函数,查找字符 char 最后一次出现的位置.
它跟 findchr()工作 类似,不过它是从字符串的最后开始向前查找的.
(c)创建第三个函数,名字叫 subchr(),
声明如下: def subchr(string, origchar, newchar)
subchr()跟 findchr()类似,不同的是,如果找到匹配的字符就用新的字符替换原先字符.
返回 修改后的字符串.
"""

def findchr(string, char):
	for i in range (len(string)):
		if string[i] == char:
			return i	 
	else:
		return "-1"

def rfindchr(string, char):
	for i in range (len(string))[::-1]:
		if string[i] == char:
			return i	 
	else:
		return "-1"
def subchr(string,origchar,newchar):
	string = list(string)
	for i in range (len(string)):
		if string[i] == origchar:

			string[i] = newchar

			return ''.join(string)
	else:
		return "-1"	

str1 = raw_input("Input a string\n")
char = raw_input("Which character do you want to find?\n")
print findchr(str1,char)
print rfindchr(str1,char)

replace = raw_input("Which character do you want to replace the find character?\n")
print subchr(str1,char,replace)
