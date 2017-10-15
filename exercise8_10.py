#!/usr/bin/env python
#-*-coding:utf-8-*-

def countString(mystring):
	YY = 0
	FY = 0
	key = 0  
	for i in mystring:  
		if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':  
			YY += 1  
		elif i!=' ':  
			FY += 1  
	key = len(mystring.split())  
	return [YY,FY,key]  

if __name__ == '__main__':
	string = raw_input("Input a strings:")
	print "yuanyin:%d, fuyin:%d, danci:%d" % (countString(string)[0], countString(string)[1],countString(string)[2])