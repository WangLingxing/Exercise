#!/usr/bin/env python
#-*-coding:utf-8-*-
import random
list1 = random.sample(range(1,33),6)
list1.sort()
list1_1 = []
list1_1.append(random.randint(1,16))
listo=list1+list1_1
count = 0
print listo
while True:
	list2 = random.sample(range(1,33),6)
	list2.sort()
	list2_1 = []
	list2_1.append(random.randint(1,16))
	listd = list2 + list2_1
	if listo==listd:
		break
	count += 1

print count
print listd
