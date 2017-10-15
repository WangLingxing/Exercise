#!/usr/bin/env python
#-*-coding:utf-8-*-
"""使用 random 模块中的 randint()或 randrange()方法生成一个随机数集合:
从 0 到 9(包括 9)中随机选择，生成 1 到 10 个随机数。
这些数字组成集合 A(A 可以是可变集合，也可以不是)。同理，按此方法生成集合 B。
每次新生成集合 A 和 B 后，显示 结果 A | B 和 A & B"""
import random
Aset = set()
Bset = set()
times = random.randint(1,10)

for i in range(times):
	Aset.add(random.randint(0,9))
for j in range(times):
	Bset.add(random.randint(0,9))
print Aset,Bset
print Aset | Bset
print Aset & Bset