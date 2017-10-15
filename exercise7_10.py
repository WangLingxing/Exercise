#!/usr/bin/env python
#-*-coding:utf-8-*-

db = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z',  
     'n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m',  
     'N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M',  
     'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z'}

def rot13(string):
	rot13string = ''
	for i in string:
		if i in db:
			rot13string += db[i]
		else:
			rot13string += i
	return rot13string

if __name__ == '__main__':
	inputString = raw_input("Enter string to rot13: This is a short sentence. Your string to en/decrypt was: \n")
	rot13string = rot13(inputString)
	print rot13string