#!/usr/bin/env python
#-*-coding:utf-8-*-

m = raw_input("Input python module:")
module = __import__(m)
arg = dir(module)

for i in arg:
	print 'name:',i,
	print 'Type:',str(type(getattr(module,i))),
	print 'Value:',getattr(module,i)
	print  