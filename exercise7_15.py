#!/usr/bin/env python
#-*-coding:utf-8-*-

def calc_set():
	Aset = set(raw_input('Input A set elements:').split())
	Bset = set(raw_input('Input B set elements:').split())
	op = raw_input('Please input Operator:')

	if op == 'in':
		print Aset in Bset
	elif op == 'not in':
		print Aset not in Bset
	elif op == '&':
		print Aset&Bset
	elif op == '|':
		print Aset|Bset
	elif op == '^':
		print Aset^Bset
	elif op == '<':
		print Aset<Bset
	elif op == '>':
		print Aset>Bset
	elif op == '<=':
		print Aset<=Bset
	elif op == '>=':
		print Aset>=Bset
	elif op == '==':
		print Aset == Bset
	elif op == '!=':
		print Aset!=Bset

if __name__ == '__main__':
	calc_set()
