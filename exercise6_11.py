#!/usr/bin/env python
# coding:utf-8

"""
(a)创建一个从整数到 IP 地址的转换程序,如下格式: WWW.XXX.YYY.ZZZ. 
(b)更新你的程序,使之可以逆转换."""

def transferToIP(numbers):
	ipAdress = []
	if len(numbers) != 12:
		print "Not a vaild IP!"
	else:
		for i in range(4):
			ipNum,numbers = numbers[:3],numbers[3:]
			ipAdress.append(ipNum)
		return '.'.join(ipAdress)
def transferIPToNum(ipAdress):
	ipAdress = list(ipAdress)
	if len(ipAdress) !=15:
		print "Not a vaild IP!"
	else:
		for i in ipAdress:
			if i == '.':
				ipAdress.remove(i)
		return ''.join(ipAdress)

inp = raw_input("Input a number which can transfer to IP adress:\n")
print transferToIP(inp)

inp = raw_input("Input a number which IP can transfer to number adress:\n")
print transferIPToNum(inp)

