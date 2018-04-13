##打卡第一天 20161116   写代码还是蛮愉快的
#是单行注释
#'''XXX''' 三个点是多行注释
'''
#hello word
print("hello word")

x=2*2
print(x)
input("x=")
y=abs(-1)
print(y)

######从某个模块导入函数，
#方法一
from  math import sqrt
y=int(sqrt(9))
print(y)

#方法二 方法二：import math  math.sqrt
import  math
y=int(math.sqrt(9))
print(y)
#########################

#####转译符号 \'  \''
print("let\'s go")

###字符串拼接
x="hello,"
y="world!"
print (x+y)

#值转化为字符串
print (str(43))


##分片  索引左闭右开
y=[1,2,3,4,5,6,7,8,9]
print (y[1:2])   #[2]

y=[1,2,3,4,5,6,7,8,9]
print (y[6:])   #[7,8,9]

#负数的情况  是重右边开始数的  就是左开右闭
y=[1,2,3,4,5,6,7,8,9]
print (y[-2:-1])    #[8]


#分片 第三个参数  步长  步长为负数 从右往左
t=[1,2,3,4,5,6,7,8,9]
print (t[0:10:2])   #[1,3,5,7,9]


#分片   分片中的两个索引作为边界，左闭右开   三个的话，第三个是步长[左边界，右边界，步长] 步长可以是负数
tag='1234567890'
print(tag[1:4])
#'234'
tag1=[1,2,3,4,5,6,7]
print(tag1[-3:])
#最后三个[5,6,7]
print(tag1[-3:0])
#没有交集，所有结果是空的[]
print(tag1[:])
#全部[1,2,3,4,5,6,7]
print(tag1[:3])
#[1,2,3]
###有步长的
print(tag1[1:6:2])
#[2,4,6]
print(tag1[1:5:2])
#[2,4]

#序列相加
a=[1,2,3]
b=[3,4,5]
print(a+b)  #[1, 2, 3, 3, 4, 5]

#序列乘法
t=[1,2,3]
t1='ha'
print (t1*2)    #'haha'
print (t*2)    #[1,2,3,1,2,3]

'''
######  2016-11-16  43/491

####--------------------------分割线----------------------------------------###
###201770222
####--------------------------分割线----------------------------------------###
###201770229凌晨  计划每天至少看20页书  做一个编程题   Mark 
##第二章  列表&元组  相当于数组
# 数组第一个元素是0，最后一个元素是-1
'''
arry1=['hello',42]
arry2=['haha',8]
total=[arry1,arry2]
print(total)

#结果是：
#[['hello', 42], ['haha', 8]]


zifuchuan='Hello'
print(zifuchuan[0])
#  结果是 H
print(zifuchuan[-1])
#  结果是 o

third=input('year:')[3]
print(third)
#结果是7


print('please input your year:')
year=input()
print('the third is:')
print(year[3])
#结果是7

#in 运算符  可以检查文件的可读可写
string1='rwhahaha'
word='r'
print(word in string1)  # TRUE

if(word in string1):
    print("YES")

print('rw' in string1) #支持一段字符串的

string1='hello'
string2=[11,22,33]
print(len(string1)) #3
print(max(string1)) #o
print(min(string1)) #e
print(len(string2)) #3
print(max(string2)) #33
print(min(string2)) #11

#list函数 将字符串转化为列表
print(list('hello')) #['h', 'e', 'l', 'l', 'o']

#join()函数
#语法：  'sep'.join(seq)
#返回值：返回一个以分隔符sep连接各个元素后生成的字符串
a='123456'
print(','.join(a))

#列表操作
#改变元素
a=[1,2,3]
a[0]=2
print(a)
#删除元素
del a[0]
print(a)
#分片赋值
a=[1,2,3]
a[1:]=list('ar')
print(a)   #[1, 'a', 'r']
######  2017-03-01  54/491
'''
'''
#####2017-03-02
##列表的方法
#append 在列表末尾追加新对象
lst=[1,2,3]
lst.append(5)
print(lst)     #[1, 2, 3, 5]

#count  统计元素在列表中出现的次数
lst=['ha','to','wo','to']
count=lst.count('to')
print(count)          #2

#extend(）方法可以在列表末尾一次性追加另一个序列的多个值
a=[1,2,3]
b=[4,5,6]
print(a+b)  #[1, 2, 3, 4, 5, 6]
print(a)    #[1, 2, 3]
a.extend(b)  #返回值是a,也就是改变了a的值，而连接操作+是没有改变a原来的值的   连接操作创建了a和b的副本 所以效率比extend低
print(a)    #[1, 2, 3, 4, 5, 6]

#index 查找列表中，第一个匹配的索引位置
lst=['how', 'are', 'you','you']
print(lst.index('you'))  #2


#insert（索引位置，插入的值）  插入列表
lst=['how','are','you']
lst.insert(1,'old')
print(lst)    #['how', 'old', 'are', 'you']

#pop 移除列表的元素，参数为空默认移除最后一个   返回值为删除的数据   同时会修改原列表  既修改列表又返回元素值
#其他的函数 直接打印
lst=['how', 'old', 'are', 'you']
#lst.pop(1)
print(lst.pop(1))  # old
print(lst)  #['how', 'are', 'you']

###入栈 append  出栈pop
lst=[1,2,3]
lst.append(lst.pop())
print(lst)  #[1,2,3]  出栈后又入栈 不变   先进先出要pop(0)

#remove()  移除列表中第一个匹配的值
lst=['ha','oks','ha']
lst.remove('ha')
print(lst) #['oks', 'ha']

#reverse（）反向存放
lst=[1,4,2]
lst.reverse()
print(lst) #[2,4,1]

#sort
x=[1,6,3]
y=x.sort()
print(x)    # [1, 3, 6]
print(y)   # none
#修改了X但是返回了none    可以整理下返回值和是否改变原变量的值得情况

t1=[1,6,3]
t2=t1   # 另一种写法：t2=t1[:]
t1=t2.sort()
print(t1)
'''
'''
列表：lst=[1,2,'ha','b']
字符串：str='hello'
元祖：（1,2,3）  不能修改的,逗号隔开就是元组   序列包含：元祖、列表。。。

a=(40+2,)
print(a)  #(42,)
print(a*3) #(42, 42, 42)   元组的组成是元素，乘法是复制

'''
####20170307########
# tuple和list一样  参数都是序列 一个返回列表 一个返回元组 列表可变，元组不可变   字符串也不可变 元组没有方法
# 字符串(strings),列表(lists)，元组(tuples)，我们可以统称为序列
'''
print(tuple([1,2,3]))          #(1,2,3)
print(tuple(['a','b','c']))   #('a', 'b', 'c')
print(tuple('abc'))             #('a', 'b', 'c')
print(tuple((1,2,3)))           #(1,2,3)

#
#sort()是可变对象(字典、列表)的方法，无参数，无返回值，sort()会改变可变对象，因此无需返回值。
# sort()方法是可变对象独有的方法或者属性，而作为不可变对象如元组、字符串是不具有这些方法的，如果调用将会返回一个异常。
#sorted()是python的内置函数，并不是可变对象(列表、字典)的特有方法，
# sorted()函数需要一个参数(参数可以是列表、字典、元组、字符串)，无论传递什么参数，都将返回一个以列表为容器的返回值
# 如果是字典将返回键的列表。
a=[3,2,1]
b=reversed(a)   #返回的是容器的返回值
print(b)       # <list_reverseiterator object at 0x0000000000FE1B00>   ；理解为指针？
print(tuple(b))  #（1,2,3）

str="hello,%s,%s world"
value=('world1','hello2')
print(str %value)   #hello,world1,hello2 world


str="pi =%.3f"
pi=(3.1415926)
print(str % pi)   #pi =3.142
#print(str %.3f pi)  #错误的
pi1='%.3f'
pi1=(3.1415926)
print(str % pi)   #pi=3.142        打印的变量前面加%   变量要是什么格式转变要在前面定义好  %s  或者%

#模板格式化  在python中Template可以将字符串的格式固定下来，重复利用。emplate属于string中的一个类
from string import Template
str=Template('I want to be a $value girl')
print(str.substitute(value='nice'))
str1=Template('I want to be a ${value}ce girl')  #是单词的一部分 $valuerl  这样会搞不清楚哪个是变量  所以要括起来
print(str1.substitute(value='ni'))

#$$是美元符号  类似转译
str2=Template('insert a $$ $value')
print(str2.substitute(value='symbol')) #insert a $ symbol

result='%s plus %s equals %s' %(1,2,3)   #要打印出来的肯定是字符串的形式，然后字符串里用%s 填充的值前面加%  （‘the prrint is %s’，%value）
result='%s plus %s equals %s' %(1,2,3)   #要打印出来的肯定是字符串的形式，然后字符串里用%s 填充的值前面加%  （‘the prrint is %s’，%value）
print(result)                     #1 plus 2 equals 3

str3='hello world!'
print('%.5s' %str3)   #宽度.精度

#find 方法   在字符串中找到子串位置，返回第一个字母的索引，没有返回-1   in是找单个字符的
#find（‘str’,起点，终点）
title='I am learning python'
print(title.find('python'))  #14
print(title.find('hello'))  #-1
print(title.find('am',3,10))  #-1

#r'读模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式
f=open('F:\自动化LOADRUNNER\HelloWord\hello.txt','r')
#lines=f.read()  #返回字符串
a=f.read(4)    #此时文件还没读完，在第四个字节处，再读取，就是从第四个开始读，要读取全部的，可以先关闭文件，再打开从新读取
b=f.read()     #或者用seek把当前位置移动到自己想要的位置f.seek(5)
print(a)
print(b)
f.close()
###
#1hel
#lo world!
#2hello world!
#3hello world!
#4hello world!
###
f=open('F:\自动化LOADRUNNER\HelloWord\hello.txt','r')
#lines=f.read()  #返回字符串
a=f.read(4)
f.seek(0)
b=f.read()
print(a)
print(b)
f.close()

f=open('F:\自动化LOADRUNNER\HelloWord\hello.txt','r')
a=f.readline(6)
print(a)   #1hello
f.seek(0)
for i in range(3):  #range(3)=[0,1,2]
 print(f.readline())   #1hello world!/n  循环读取每一行
f.close()

f=open('F:\自动化LOADRUNNER\HelloWord\hello.txt','r')
list=f.readlines()   #返回每一行，用一个列表展示
print(list)   #['1hello world!\n', '2hello world!\n', '3hello world!\n', '4hello world!']
f.close()

a=['1','2','3'] #列表中元素必须是字符串 [1,2,3]不行
b='+'
print(b.join(a))   #'1+2+3'

#split(分隔符，分割几次)通过指定分隔符 对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
a='www.baidu.com'
print(a.split('.'))#['www', 'baidu', 'com']
print(a.split('.',1)) #['www', 'baidu.com']
print(a.split('ai'))#['www.b', 'du.com']

#lower（） 将字符串变成小写  大小写不明感的地方找到字符串
str=['name','hello']
name=input()  #Name
print(name)   #Name
print(name.lower()) #name

if name.lower() in str:
    print("find it")
else:
    print("not in")

#replace（被替换的，替换成什么）  返回被替换后的字符串
#translate 也是替换 但是一个字符的  这个要用到table=maketrans(from,to)  str.translate(table[, deletechars]);
#table -- 翻译表，翻译表是通过maketrans方法转换而来。
#deletechars -- 字符串中要过滤的字符列表。
#from string import maketrans  么有了
str="hello girls girls"
a=str.replace('girls','boys')  #hello boys boys
print(a)
table=str.maketrans('i','o')
print(str.translate(table))  #hello gorls gorls

#strip   str.strip 返回去除两边不包含内部的空格的字符串
str="   hello    hello word!    "
print(str.strip()) #hello    hello word!

#####第四章：字典######
#电话号码以及0开头的数字，要用字符串表示  原样输出用数字字符串
name=['lily','susen','yeashine']
tel=['3039381','3038367','3039380']
print(tel[name.index('yeashine')])  #3039380
#字典是另一种可变容器模型，且可存储任意类型对象。

#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
#d = {key1 : value1, key2 : value2 }

d={'alice':'3038379','yeashine':'3039380'}
print(d['yeashine'])   #3039380

x=[]
x=[None]*43  #空表需要初始化
x[42]='ha'
print(x)

y={}   #变长的  空字典建立
y[42]='ha'
print(y)  #{42,'ha'}
y['43']='hi'
print(y) #{42: 'ha', '43': 'hi'}

#字符的格式化字符串 %（键值）s  %(键值)d  键值不用加‘’ 打印格式是print（‘%是（键值）’ %date）

d={'alice':'3038379','yeashine':'3039380'}
print('%(yeashine)s' %d )   #3039380
#字典的方法
#d.clear()
#d.copy()  返回一个具有相同键值对的新字典
#d.fromkeys 使用给定的键值建立新字典
####第5章  条件、循环
x=1
y=2
z=3
x,y=y,x      #交换变量
print(x,y,z) #2 1 3

if 1<2:
    print(12)
    if 3<4:
        print(34)
    print(12)
else:
    print(3)  #和缩进有关 12  34 12
str='hello'
if  'hello' in str:
    print(1)

a=10
b=11
if a<11 and a>1:
    print('yes')
else:
    print('no')
if b==10 or b==11:
    print('yes2')
else:
    print('no')

#####断言 assert 检查点
assert 1==2   #AssertionError  这个是断言检查不通过的错误信息
#########96页  20170316
###循环
x=1
while x<=100:
    print(x)
    x+=1

    a=range(10)
print(a) #range(0, 10)
for num in range(1,10):
    print(num)
#函数
def myfunction():
    print("this is my firsrfunction")

myfunction()
'''
#匹配出所有s开头，e结尾的单词
# def no_boring_zeros(n):
#     # your code
#     if n==0:
# 	    return n
#     while(n%10==0):
#         n=n/10
#     return int(n)
#
#
# print(no_boring_zeros(0))











































