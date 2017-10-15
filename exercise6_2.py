#!/usr/bin/env python
#!-*-coding-utf-8-*-
import string
import keyword

alphas = string.letters + '_'
nums = string.digits
kw = keyword.kwlist

print 'Welcome to the Identifier Checker v1.0'
inp = raw_input("Identifier to test?")

if len(inp) == 1:
	if inp[0] not in string.letters:
		print '''invalid: first symbol must be alphabetic'''
	else:
		print "okay as an one character identifier"
elif len(inp) > 1:
	if inp  in kw:
		print '''Invalid: it a python keyword'''
	elif inp[0] not in alphas:
		print '''invalid: first symbol must be alphabetic'''
	else:
		for otherChar in inp[1:]:
			if otherChar not in alphas:
				print '''invalid: first symbol must be alphabetic'''
				break
		else:
			print "okay as an identifier"


