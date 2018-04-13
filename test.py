'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score


bart=Student('Yeashine','26')
print(bart)
print (bart.name)
print(bart._Student__score)
#print(bart.__score)
print (bart.get_score())
bart.set_score(27)
print (bart.get_score())


class Animal(object):
    def __init__(self,name):
        self.name = name
    def run(self):
        print("animal is running")

class Dog(Animal):
    def run(self):
        print ("dog is running")

##dog=Dog()  报错了
dog=Dog('ba')
print (hasattr(dog,'name'))
print (hasattr(dog,'run'))
#print (hasattr(dog,name))  报错
print (isinstance(dog,Dog))
print(dir(dog))
class Student(object):
    __slots__=('name')
s=Student()
s.name='ye'
s.age=9
print(s.name)
print(s.age) ##报错



##width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width    ##get方法 所以是返回一个值 用return

    @width.setter
    def width(self,value):    ##定义set方法，多了一个变量
        if not isinstance(value,int):  ##注意这里不是self  if not isinstance(self,int)
            raise ValueError('类型不对')  ###一旦执行了raise语句，raise后面的语句将不能执行  异常抛错
        if value<0:
            raise ValueError('width must be bigger than 0')
        self._width=value       ##这个是set 所以是赋值

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._width*self._height

s = Screen()
s.width= 5   ##不是s.width(5)
s.height = 6
print(s.resolution)

from enum import Enum
Month=Enum('Month','Jan Feb')

j=Month.Jan
print (j)

class Animals(Enum):
    ant = 1
    bee = 2
    cat = 3
    dog = 4

a=Animals.ant
print (a)






from io import StringIO
from io import BytesIO  #二进制文件
f=StringIO()
f1=StringIO('!my!\ncode!')
f3=BytesIO(b'\xe4\xba\x8c\xe8\xbf\x9b\xe5\x88\xb6\xe6\x96\x87\xe4\xbb\xb6')
f2=BytesIO()
f.write('hello!\nworld!')
f2.write('二进制文件'.encode('utf-8'))#有‘’
print('f:'+f.getvalue())  #getvalue()方法用于获得写入后的str
print('f2:',f2.getvalue()) #这里不能用+  要用，  类型不同
print('f3:',f3.read())
while True:
    s=f1.readline()
    if s=='':
        break
    print ('f1:',s.strip('!'))   #strip()方法返回从字符串的开始和结束(默认空格字符)中删除指定所有字符的字符串的副本,就去掉前后的  strip('*')
'''
