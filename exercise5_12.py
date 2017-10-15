#!/usr/bin/env python
#-*-coding:utf-8-*-

"""系统限制。
写一段脚本确认一下你的 Python 所能处理的整数，长整数，浮点数和复 数的范围。"""
import sys

print sys.maxint
print -sys.maxint-1
print sys.float_info
print sys.long_info