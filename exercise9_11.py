#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import re

def checkurl(url):
	regex = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')

	if regex.match(url):
		return True
	else:
		return False


def geturl():
	name = raw_input('Please input url name:')
	while True:
		url = raw_input('Pleaes input url address:')
		if checkurl(url):
			break
		else:
			print 'Wrong url format,Please enter again!'
	mark = raw_input('Please input url mark:')
	folder = raw_input('Please input url folder:')
	return (name, url, mark, folder)

def load(filename):
	f = open(filename, 'a+')
	bmlist = f.readlines()
	f.close()
	return bmlist

def save(bmlist, filename):
	f = open(filename, 'w')
	for line in bmlist:
		if len(line) == 0:
			continue
		f.write(line)
	f.close()

def add(bmlist,name,url,mark,folder='default'):
	bookmark = ''
	bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
	if bookmark not in bmlist:
		bmlist.append(bookmark)

def modify(bmlist,index,name,url,mark,folder):
	bookmark = ''
	bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
	bmlist[index] = bookmark

def delbm(bmlist,index):
	bmlist.pop(index) 
	
def findbk(bmlist,fname,furl):
	for i, item in enumerate(bmlist):
		(name, url, mark, folder) = item.split(';')
		if (fname in name) and (furl in url):
			return i
		if fname and (fname in name):
			return i
		if furl and (furl in url):
			return i
	else:
		return -1

def output2html(bmlist):
	for i, item in enumerate(bmlist):
		(name, url, mark, folder) = item.split(';')
		if os.path.exists(folder.strip()):
			pass
		else:
			os.mkdir(folder.strip())
		filename = name.strip() + '.html'
		f = open(filename,'w+')
		fmt = '%d\t%s\t<a href=%s>%s</a>\t%s\t%s<br>'
		f.write('<html><head><title>bookmark</title></head><body>')
		content = fmt % (i+1, name, r'http:\\' + url, url, mark, folder)
		f.write(content)
		f.write('</body></html>')
		f.close()
		os.rename(filename,folder.strip()+os.sep+filename)


bmlist=load(r'url.txt')
print bmlist

while True:
	print '0. quit'
	print '1. add a url bookmark'
	print '2. modify a url bookmark'
	print '3. delete a url bookmark'
	print '4. find a url bookmark'
	print '5. output url bookmark as html'
	print '\n'

	userInput = int(raw_input('Please enter your choice:\n'))
	if(userInput == 0):
		save(bmlist, 'url.txt')
		break
	elif(userInput >5 or userInput <0):
		print 'Try agin(0-5). Enter 0 to quit\n'
	elif(userInput == 1):
		data = geturl()
		add(bmlist,*data)
		print bmlist
	elif(userInput == 2):
		modifyInput = int(raw_input('Please enter which Bookmark Index to modified:'))
		data = geturl()
		modify(bmlist, modifyInput, *data)
	elif(userInput ==3):
		popIndex = int(raw_input('Please enter which Bookmark Index to delete:'))
		delbm(bmlist, popIndex)
	elif(userInput == 4):
		name = raw_input('url name:')
		url = raw_input('url address:')
		index = findbk(bmlist, name, url)
		if index == -1:
			print 'Not found'
		else:
			print bmlist[index]
	elif(userInput == 5):
		output2html(bmlist)











