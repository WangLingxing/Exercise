#!/usr/bin/env python
#-*-coding:utf-8-*-
import random
def setRandom():
	Aset = set()
	Bset = set()
	times = random.randint(1,10)
	
	for i in range(times):
		Aset.add(random.randint(0,9))
	for j in range(times):
		Bset.add(random.randint(0,9))
	
	print "Aset was ",Aset
	print "Bset was ",Bset

	return (Aset,Bset)

def checkSet(Aset,Bset):
	for i in range(3):
		Cset = set(map(int, raw_input('Please input A|B:').split()))
		Dset = set(map(int, raw_input('Please input A&B:').split()))

		if Cset == Aset|Bset and Dset == Aset&Bset:
			print 'You are right!'
			break
		else:
			print 'Wrong answer!'

	else:
		print 'Aset|Bset is:',Aset|Bset
		print 'Bset&Bset is:',Aset&Bset  

if __name__ == '__main__':
	sets = setRandom()
	checkSet(sets[0], sets[1])
