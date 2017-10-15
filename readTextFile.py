#!/usr/bin/env python
'readTextFile.py -- read and display text file'

#get fileName
fname = raw_input('Enter fileName:')
print

#attempt to open file for reading
try:
	fobj = open(fname,'r')
except IOError, e:
	print "%s file open error:" % fname, e
else:
	#display contents to the screen
	for eachLine in fobj:
		print eachLine,
fobj.close()
