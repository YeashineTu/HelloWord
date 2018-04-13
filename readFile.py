#!/usr/python/bin
# -*- coding:utf-8 -*-
#try:
	f=open('fileSource.txt',encoding='utf-8')
	for data in f.readlines():
		sum=0
		data=data.split()
		for sorce in data[1:]:
			sum+=int(sorce)
		print('%s'%' '.join(data))
		data.append(sum)
	#	print ('%s:%d'%(data[0],int(data[1:])))
		print("%s的总分是:%d"%(data[0],sum))  ##多个参数，后面用元组
#except:
#	print('No file exits')


#print(';'.join([1,2,3]))
