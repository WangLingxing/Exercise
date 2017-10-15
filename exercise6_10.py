#!/usr/bin/env python
# coding:utf-8

"""
写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转. 
比如,输入"Mr.Ed",应该返回"mR.eD"作为输出.
"""
#可以用isupper和islower逐字判断,使用string.upper()和string.lower()转换大小写
inp = raw_input("Input a string:\n")
inp = inp.swapcase()
print inp