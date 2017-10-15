#!/usr/bin/env python
#-*-coding:utf-8-*-
# 人力资源。创建一个简单的雇员姓名和编号的程序。
# 让用户输入一组雇员姓名和编号。 
# 你的程序可以 供按照姓名排序输出的功能，雇员姓名显示在前面，后面是对应的雇员编号。
# 附加:添加一项功能，按照雇员编号的顺序输出数据
import sys
HR_DATA = {}
def newEmployee():
	try:
		name = raw_input("Input name(enter q to quit): ")
		number = raw_input("Input number(enter q to quit): ")
	except (EOFError,KeyboardInterrupt):
		name == 'q'
		number == 'q'
	if name == 'q' or number == 'q':
		sys.exit()
	else:
		HR_DATA.update({name:number})
		print 'Data had been update'

def listData(nameList = False):
	if nameList:
		keys = sorted(HR_DATA.keys())
		for i in keys:
			print "%s:%s" %(i,HR_DATA[i])
	else:
		for key1,value1 in sorted(HR_DATA.items(), key=lambda d:d[1],reverse=False):
			print "%s:%s" %(key1,value1)


while True:  
    print '''''Please enter the choice: 
[N]:enter the new data! 
[D]:display the updated data(sorted by number) 
[R]:display the updated data(sorted by name) 
[Q]:Quit!'''  
    try:  
        choice=raw_input(':').strip()[0].lower()  
    except (EOFError,KeyboardInterrupt):  
        choice='q'  
    if choice not in 'ndrq':  
        print 'Invalid option,try again!'  
    else:  
        if choice=='q':print 'Exit!!';break;  
        if choice=='d':listData();continue;  
        if choice=='r':listData(True);continue;  
        if choice=='n':newEmployee();continue; 


