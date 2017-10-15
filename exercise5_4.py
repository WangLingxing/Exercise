#!/usr/bin/env python
year = int(raw_input("Please enter year:"))
if year % 4 == 0 and year % 100 != 0:
	print "%d is a leap year" % year
elif year % 400 == 0:
	print "%d is a leap year" % year
else:
	print "%d is not a leap year" % year
