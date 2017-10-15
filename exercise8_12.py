#!/usr/bin/env python
#-*-coding:utf-8-*-

def output(start, end):
	if (start >= 33 and start <= 126) or (end <=126 and end >= 33):
		print '%-10s%-10s%-10s%-10s%-10s' % ('DEC','BIN','OCT','HEX','ASCII')
		print '---------------------------------------------'
	else:
		print '%-10s%-10s%-10s%-10s' % ('DEC','BIN','OCT','HEX')
		print '-------------------------------------'

	for i in range(start, end+1):
		if (start >= 33 and start <= 126) or (end <=126 and end >= 33):
			print '%-10s%-10s%-10s%-10s' % (i, bin(i), oct(i), hex(i)),
			if i >= 33 and i <= 126:
				print '%-10s' % chr(i)
			else:
				print '%-10s' % ' '
		else:
			print '%-10s%-10s%-10s%-10s' % (i, bin(i), oct(i), hex(i))

if __name__ == '__main__':
	start = int(raw_input("Input start:"))
	end = int(raw_input("Input end:"))
	output(start, end)




