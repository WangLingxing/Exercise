#!/usr/bin/env python
flag = True

while flag:
	number = int(raw_input("Input a number:"))
	if number <= 100 and number >= 1:
		flag = False
	elif number < 1 or number > 100:
		print "Try again! Now you can't exit the loop"
print "Success! Now you can exit the loop"