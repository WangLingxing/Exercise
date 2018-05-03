#!/usr/bin/env python
#-*-coding:utf-8-*-
from random import randint as ri 
def leapyear(year):
	if year % 4 == 0 and year % 100 != 0:
		print "%d is a leap year" % year
		return year
	elif year % 400 == 0:
		print "%d is a leap year" % year
		return year
	else:
		print "%d is not a leap year" % year

years = []
for i in range(10):
	years.append(ri(1980, 2017))

print years
print filter(leapyear, years)

# 列表解析
print [n for n in [ri(1980, 2017) for i in range(10)] if ((n % 4 == 0 and n % 100 !=0) or (n % 400 == 0)) ]