#!/usr/bin/env python
i = 0
list1 = []
list2 = []
sum1 = 0
sum2 = 0
while i < 5:
	a = int(raw_input("input a number:"))
	list1.append(a)
	sum1 += a
	i += 1
aver1 = float(sum1)/5
print list1,"sum1 = %d" %sum1,aver1

for j in range(5):
	b = int(raw_input("input a number:"))
	list2.append(b)
	sum2 += b
aver2 = float(sum2)/5
print list2,"sum2 = ",sum2,aver2

