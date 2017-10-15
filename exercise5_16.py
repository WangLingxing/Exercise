#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
家庭财务。
给定一个初始金额和月开销数，
使用循环，确定剩下的金额和当月的支出数，
包括最后的支出数。 
Payment() 函数会用到初始金额和月额度
"""

def Payment(paid, balance):
	count = 0
	print "Amount Remaining"
	print "Pymt#  Paid      Balance"
	print "-----  -----     --------"
	while (balance > paid):
		print "%-2d     %.2f      %.2f"%(count,paid,balance)
		balance = balance - paid
		count += 1
	count += 1
	print "%-2d     %.2f      %.2f"%(count,balance,0)

if __name__ == '__main__':
	balance = float(raw_input("Enter opening balance:"))
	paid = float(raw_input("Enter monthly payment:"))
	Payment(paid,balance)

