#!/usr/bin/env python
#-*-coding:utf-8-*-

"""(a) 使用循环和算术运算，求出 0-20 之间的所有偶数 
(b) 同上，不过这次输出所有的奇数
(c) 综合 (a) 和 (b)， 请问辨别奇数和偶数的最简单的方法是什么?
(d) 使用(c)的成果，写一个函数，检测一个整数能否被另一个整数整除。 
先要求用户输 入两个数，然后你的函数判断两者是否有整除关系，
根据判断结果分别返回 True 和 False;
"""
odd = []
even = []
for i in range(1,21):
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)
print "Odd number between 0-20 are " + str(odd)
print "Even number between 0-20 are " + str(even)

def exactDivision(n1,n2):
	if n1 % n2 == 0:
		print "Can be exact division!"
		return True
	else:
		print "Can't be exact division!"
		return False
if __name__ == '__main__':
    a = int(raw_input("Enter divisor:\n"))
    b = int(raw_input("Enter dividend:\n"))
    exactDivision(a,b)