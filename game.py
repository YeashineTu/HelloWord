#!/usr/bin/python
#-*- coding utf-8 -*-
#date:20171011
#author:tyx
#==== 点球小游戏 ====
def isRight(value,list):
	if value not in direction:
		print('Your direction is not right,input again')
		return False
	else:
		return True

def isEqual(value1,value2):
	if(value1==value2[0]):
		print("sorry,you lost the score")
		return True
	else:
		print("Congratulations!")
		return False
import random
score_me=0
score_computer=0
isTrue=False
i=1
direction=['left','middle','right']
while(i<=3):
	com_direc=random.sample(direction,1)
	print("###Round %d"%i)
	print("Please input your direction,'left','middle'or'right' ")
	my_dirc=input()
	while(isTrue==False):
		isTrue=isRight(my_dirc,direction)
	if isEqual(my_dirc,com_direc):
		score_computer +=1
	else:
		score_me +=1
	i+=1
print('my score is :%d'%score_me)
print("computer's score is:%d"%score_computer)
