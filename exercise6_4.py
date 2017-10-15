#!/usr/bin/env python
#! -*-coding:utf-8-*-
def calcScore(score):
	if score >= 90 and score <=100:
		rank = 'A'
	elif score >= 80 and score < 90:
		rank = 'B' 
	elif score >= 70 and score < 80:
		rank = 'C' 
	elif score >= 60 and score < 70:
		rank = 'D'
	else:
		rank = 'E'
	return "Rank is " + rank

list1 = []
sum = 0
while True:
	inp = raw_input("Input your score,and enter 'q' to quit\n")
	if inp == 'q':
		break
	else:
		list1.append(int(inp))
		print calcScore(int(inp))
for i in list1:
	sum += i

aver = float(sum)/len(list1)
print "Average score is %d" % aver