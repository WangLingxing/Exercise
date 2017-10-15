#!/usr/bin/env python
# coding:utf-8

"""
(a)研究这段代码并 述这段代码想做什么.在所有的(#)处都要填写你的注释. 
(b)这个程序有一个很大的问题,比如输入 6,12,20,30,等它会死掉,实际上它不能处理任何的偶
数,找出原因. 
(c)修正(b)中 出的问题.
"""
#导入string模块
import string

#进入循环
while 1:

    #输入数字
    num_str = raw_input('Enter a number: ')

    #捕获异常
    try:
        #字串转换成数字
        num_num = string.atoi(num_str)

        #中断while循环
        break

    #抛出异常
    except ValueError:
        print "invalid input... try again"

#从1-num_num的列表
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`

#定义i=0
i = 0

#当i小于fac_list列表长度时进入循环
while i < len(fac_list):

    #能被整除，则从列表中去掉这个数
    if num_num % fac_list[i] == 0:
        del fac_list[i]  #这里出错，使用del后列表长度会变化导致循环未全部遍历
        i = i - 1  #减去删除掉的index

    #循环叠加
    i = i+1

#输出
print "AFTER:", `fac_list`
