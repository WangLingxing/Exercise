#!/usr/bin/env python
# coding:utf-8

"""
设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,
下面是规则.你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从 下面的规则中产生,这个规则本身是个悖论.
(a) the paper covers the rock, 布包石头.
(b)石头砸剪子,
(c)剪子剪破布.
在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,
然后由你的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用 if 语句.
"""
from random import choice
def Rochambeau(humanInput, PCInput):
	if PRS_dic[humanInput] - PRS_dic[PCInput] == 0:
		print "It is a tie."
	elif PRS_dic[humanInput] - PRS_dic[PCInput] == 1\
	or PRS_dic[humanInput] - PRS_dic[PCInput] == -2:
		print "You Win!"
	else:
		print "You Lose."

PRS_list = ['P', 'R', 'S']
PRS_dic = {'P':-1, 'R':1, 'S':0}

if __name__ == '__main__':
	while True:
		inp = (raw_input("Enter 'R' for 'Rock'\
,'S' for 'Scissors' and 'P' for 'Paper'(q to quit):")).upper()
		if inp == 'Q':
			break
		else:
			PCInput = choice(PRS_list)
			print "PC enter " + PCInput
			Rochambeau(inp, PCInput)
