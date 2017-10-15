#!/usr/bin/env python
#-*-coding:utf-8-*-

def tr(srcstr, dststr, string, flag=True):
	src_dst = {}
	mystring = ''
	if len(srcstr) == len(dststr):
		if flag:
			for key, value in zip(srcstr,dststr):
				src_dst.setdefault(key, value)
			for i in string:
				if i in src_dst:
					mystring += src_dst[i]
				else:
					mystring += i
			return mystring
		else:
			for key, value in zip(srcstr.lower(), dststr):
				src_dst.setdefault(key, value)
			for i in string:
				if i.lower() in src_dst:
					mystring += src_dst[i.lower()]
				else:
					mystring += i
			return mystring

	else:
		if flag:
			for key, value in zip(srcstr[:len(dststr)],dststr):
				src_dst.setdefault(key, value)
			for i in string:
				if i in src_dst:
					mystring += src_dst[i]
				elif i not in srcstr:
					mystring += i
			return mystring
		else:
			for key, value in zip(srcstr[:len(dststr)].lower(),dststr):
				src_dst.setdefault(key, value)
			for i in string:
				if i.lower() in src_dst:
					mystring += src_dst[i.lower()]
				elif i not in srcstr:
					mystring += i
			return mystring
	

if __name__ == '__main__':
	str1 = tr('abcdef', 'mon', 'abcdefghi',True)
	print str1