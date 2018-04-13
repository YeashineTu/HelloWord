#!/usr/bin/python
# -*- coding: utf-8 -*-
#data 20171016
#author:tyx
'''
<?xml version="1.0" encoding="utf-8" ?>
<contents>
    <content>
      <key>Client_Login_Info_dlyh</key>
      <value>登录账户:</value>
    </content>
</contents>
'''
try:
	f=open('readManyLang.xml','w',encoding='utf-8')  ##不写encoding,写的文件是乱码
	f.write('<?xml version="1.0" encoding="utf-8" ?>'+'\n')
	f.write('<contents>'+'\n')

	fSource=open('dataSource.txt',encoding='utf-8')  ##wirte会自己新建，read不行，打不开会报错，要加异常捕获
	for data in fSource.readlines():
		data=data.replace('"','')
		data=data.replace(' ','')
		data=data.replace('\n','')
		data=data.replace(';','')
		data=data.split('=')
		f.write('    <content>'+'\n')
		f.write('      <key>'+data[0]+'</key>'+'\n')
		f.write('      <value>'+data[1]+'</value>'+'\n')
		f.write('    </content>'+'\n')
	f.write('</contents>')
	f.close()
	fSource.close()
except:
	print ('file not exits!')