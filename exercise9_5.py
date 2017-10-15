#!/usr/bin/env python
# -*-coding:utf-8-*-

f=open('score.txt','r')  
scores=[]  
for i in f:  
    if 0<=int(i.strip())<=100:  
        scores.append(int(i.strip()))  
    if int(i.strip())<60:  
         print 'score is F' ,i  
    elif 60<=int(i.strip())<=69:  
         print 'score is D',i  
    elif 70<=int(i.strip())<=79:  
         print 'score is C',i  
    elif 80<=int(i.strip())<=89:  
         print 'score is B',i  
    elif 90<=int(i.strip())<=100:  
         print 'score is A',i  
    else:  
         print 'score wrong,please input again',i  
f.close()  
print 'average score is %f' %(sum(scores)//len(scores))  