#!/usr/bin/env python
# coding:utf-8

"""
给出一个整数值,返回代表该值的英文，比如输入 89 返回"eight-nine"。
附加题: 能够返回符合英文语法规则的形式，比如输入“89”返回“eighty-nine”。
本练习中的值限定在家 0 到 1,000"""

units = ['zero','one','two','three','four','five','six','seven',
'eight','nine','ten','eleven','twelve','thirteen','forteen','fifteen',
'sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifth','sixty','seventy','eighty','ninety']
hundreds = ['hundreds']

str1 = raw_input("Input your numbers between 0 to 200:\n")
num = int(str1)

if num <= 19:
	print units[num]
elif num <=99:
	tens_units = int(str1[0])-2
	units_units = int(str1[1])
	if units_units == 0:
		print tens[tens_units]
	else:
		print tens[tens_units] + '-' + units[units_units]
elif num <=119:
	hundreds_units = int(str1[0])
	units_units = int(str1[1:])
	print units[hundreds_units] + ' hundred and ' + units[units_units]
else:
	hundreds_units = int(str1[0])
	tens_units = int(str1[1]) - 2
	units_units = int(str1[2])
	if units_units == 0:
		print units[hundreds_units] + ' hundred and ' + tens[tens_units]
	else:
		print units[hundreds_units] + ' hundred and ' + tens[tens_units] + '-' + units[units_units]

