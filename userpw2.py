#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
from datetime import datetime
import re
import base64,hashlib
import pickle

def Initialization(file_name):
	'''程序初始化，创建user.ini和time.ini文件'''
	dict_test = {"admin":"db69fc039dcbd2962cb4d28f5891aae1"}   #超级管理员,密码admin(已加密)
	f = file(file_name, 'a+')
	if len(f.readlines()) == 0:  #判断程序是否为空，只在第一次运行的时候初始化
		if file_name == "user.ini":
			pickle.dump(dict_test, f, True)
		else:
			pickle.dump({}, f, True)
	f.close()

def encodepwd(passwd):
	'''采用base64和md5双层加密'''
	md5 = hashlib.md5()
	pwd = base64.b64encode(passwd)
	md5.update(pwd)
	return md5.hexdigest()


def time_order(user):
	'''记录用户登陆时间，结果保存在time.ini文件中''' 
	ft = file('time.ini', 'r')
	dbt = pickle.load(ft)
	if user not in dbt:
		dbt.setdefault(user, datetime.now())
	else:
		history_time = dbt[user]
		t = (datetime.now() - history_time).seconds
		#print t

		if t/3600.0 <= 4:
			print 'You already logged in at:',history_time
		dbt[user] = datetime.now()

	ft = file('time.ini', 'w')
	pickle.dump(dbt, ft, True)
	ft.close()

def newuser(db):
	'''用户创建程序，由olduser调用'''
	while True:
		name = raw_input("Please enter your user name: ")
		if re.match(r'^\w*$', name):     #采用正则表达式检测用户名是否合法
			pass
		else:
			print 'Username should be made of A~Z、a~z、0~9、_'
			continue

		for n in db.keys():
			if name.lower() == n.lower():
				print 'User name had been taken, please try again!'
				break
		else:
			break
	password = raw_input("Please enter your password: ")
	db[name] = encodepwd(password)

def olduser(db):
	'''用户登陆程序'''
	name = raw_input("Login: ")
	if name in db.keys():
		pwd = raw_input("Password: ")
		password = db[name]
		if password == encodepwd(pwd):
			print 'Welcome back ',name
			time_order(name)
		else:
			print 'Wrong password!'
	else:
		newUser = raw_input('Do you want to instead a new user? Yes or No:')
		if newUser.lower() == 'yes':
			newuser(db)
	print '\n'

def deluser(db):
	'''删除一个用户，但必须以管理员的身份'''
	print 'Please login as admin'   #管理员的身份才能删除用户
	name = raw_input('Login:')
	password = raw_input('Password:')
	if db[name] == encodepwd(password) and name == 'admin':
		user = raw_input("Please input a user name: ")
		if user != 'admin':
			if db.pop(user):
				print 'Delete Current!'
		else:
			print 'Can not delete admin!'
	else:
		print 'Wrong loginName/password!'

def checkuser(db):
	'''查看所有用户，但必须以管理员的身份'''
	print 'Please login as admin'    #管理员的身份才能删除用户
	name = raw_input('Login:')
	password = raw_input('Password:')
	pwd = db.get(name)
	if pwd == encodepwd(password) and name == 'admin':
		for i in db.keys():
			print 'username: %10s ====> password: %10s' % (i,db[i]) 
	else:
		print 'Wrong loginName/password!'

def resetuser(db):
	'''修改密码，但必须正确的输入老密码'''
	name = raw_input("Input user name:")
	password = raw_input("Input old password:")
	if db[name] == encodepwd(password):
		newpwd = raw_input("Input new password:")
		db[name] = encodepwd(newpwd)
	else:
		print 'Wrong loginName/password!'

def showmenu():  
    '''''程序运行的主函数'''  
    fu = file('user.ini','r')  
    db = pickle.load(fu)  
    prompt = '''''
                  (L)ogin Now 
                  (Q)uit 
                  (D)elet User 
                  (C)heck All User 
                  (R)eset Password 
                  Enter choice:'''
    done = False
    while not done:
    	chosen = False
    	while not chosen:
    		try:
    			choice = raw_input(prompt).strip()[0].lower()
    		except(EOFError,KeyboardInterrupt,IndexError):
    			choice = 'q'
    		print '\nYou picked:[%s]' % choice
    		if choice not in 'lqdcr':
    			print 'Invalid option, try again'
    		else:
    			chosen = True

    	if choice == 'q':done = True
    	if choice == 'l':olduser(db)
    	if choice == 'd':deluser(db)
    	if choice == 'c':checkuser(db)
    	if choice == 'r':resetuser(db)
    fu = file('user.ini', 'w')
    pickle.dump(db, fu, True)
    fu.close()

if __name__ == '__main__':
	'''系统有一个用户名为admin 密码为admin的超级用户,请立即修改密码！'''
	print 'Welcome to User Information Management System!'
	Initialization('user.ini')
	Initialization('time.ini')
	showmenu()  








