aDict = {'host':'eather'}
aDict['port'] = 80
for key in aDict:
	print key, aDict[key]

foo = 'abc'
for i, ch in enumerate(foo):
	print ch, '(%d)' %i

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEvens:
	print i
try:
	fileName = raw_input('Enter file name:')
	fobj = open(fileName,'r')
	for eachLine in fobj:
		print eachLine,fobj.close()
except IOError, e:
	print 'file open error:',e
