#!/usr/bin/env python
#-*-coding:utf-8-*-

def tax(rate = 0.2):
	price=float(raw_input('please input a earn price: '))
	print 'your tax is %10.2f' %round(price*rate,2)
tax()