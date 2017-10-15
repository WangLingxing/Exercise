#/usr/bin/env python
#-*-coding:utf-8-*-
"""写一对函数来进行华氏度到摄氏度的转换。
转换公式为 C = (F - 32) * (5 / 9) 应该在这个练习中使用真正的除法"""

from __future__ import division

F = int(raw_input("Input Fahrenheit:\n"))

C = (F - 32) * (5 / 9)

print "%.2f F Fahrenheit change to degree is %.2f C" %(F, C)

