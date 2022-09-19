#元组
"""
tup1=("google","baidu","bilibili","pixiv")
print(tup1[-1],tup1[1:3])
inter = len(tup1)
print(inter)
minn = min(tup1)
print(minn) #按字典序
add = id(tup1)
print(add)
tup1=(1,2,3,4,5,6)
add = id(tup1)
print(add)
"""



#集合
"""
basket = {'apple','orange','orange','pear','banana'}
print(basket)
boolen = 'apple' in basket
print (boolen)
basket.add('wanghao')
print(basket)
basket.remove('wanghao')#如果元素被移除之前不存在，会发生错误
basket.discard('wanghao')#如果元素被移除之前不存在，不会发生错误
print(basket)
thisset = set(("google","Runoob","Taobao"))
booln = "google" in thisset  #判断这个元素是否在集合中存在
print (booln)
thisset.clear()  #清除所有元素
print(thisset)
 while len(thisset) > 0 :
  x=thisset.pop()
  print(x)
"""



#条件控制
"""
var1 = 0
var2 = 1
while  var1+var2 < 100:
    if ((var1+var2)%3 ==0):
        print("var1=",var1,"var2=",var2)
    elif ((var1+var2)%3 ==1):
        print("sorry1")
    else :
        print("sorry2")
    var1+=1 注意和if else等对齐
    var2+=1

"""



#循环语句
"""
#python里面没有do while循环，有for 和 while
#1.0 while 的基础用法
inter1 = 0
while inter1 < 10:
  print(inter1)
  inter1+=1
#while (inter1) : print("hello") #写在一行也是可以的

#1.1 while-else的用法
count =0
while count < 5 :
  print (count,"小于5")
  count +=1
else :
  print (count,"大于或等于5")

#2.0 for in  -else (break)循环
languages= {"C","C++","Perl","Python"}
for x in languages :
  print(x)

sites = ["baidu","google","runoob","taobao"]
for site in sites:
   if site == "runoob" :
     print("菜鸟教程！")
     break
   print("循环数据"+ site)
else :
   print("没有循环数据")
#2.1 range 函数的使用
for i in range (5) :      #指定0-n
  print(i)
for i in range (5,9) :    #指定区间 5-8
  print(i)
for i in range (1,9,3) :  #指定步长 3 6 8
  print(i)
for i in range (-1,-100,-30) :#负数步长
  print(i)
pass
list(range(5))
[0,1,2,3,4]
print(list) #?这是啥意思呢
"""



#生成器和迭代器

"""
#迭代器 的基本方法 iter()和next(),用来访问 集合 元素
list =[1,2,3,4]
it =iter(list)
print(next(it)) #>>>1
print(next(it)) #>>>2
for x in it :
   print(x,end=" ") #>>>3 4

import sys         #引入sys模块
list2 = [1,2,3,4]
it = iter(list)
while True :
 try:              #T要大写
     print(next(it))
 except StopIteration :  #用于标识迭代的完成，防止死循环的出现。（else : raise StopIteration)
     #sys.exit(0)    #正常结束
     break
print("pause,now another one")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
for i in range(5) :
    print(next(myiter))
#StopIteration 的使用
class MyNumber :
    def __iter__(ass): #用def来定义一个函数
        ass.b = 1
        return ass
    def __next__(ass):
        if ass.b <= 20:
            x=ass.b
            ass.b += 1
            return x
        else :
            raise StopIteration
myclass = MyNumber()
myiter = iter(myclass)
for i in myiter :
    print(x)

#生成器
import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True :
         if(counter > n):
             return 
         yield a
         a,b = b,a+b
         counter +=1 
f=fibonacci (10) # f 是一个迭代器，由生成器返回生成
while True :
    try : #我们把可能发生错误的语句放在try里面，用except来处理异常
        print(next(f),end=" ")
    except StopIteration:
        sys.exit(0)
"""
 

"""
#函数的定义和使用
def max(a,b):
    if a>b:
        return a
    elif a<b :
        return b
    else :
        return a
x=max(2,3)
print(x)
print(" ")
def printme(str):#传入什么字符就在打印一次
    print(str)
    return 
printme("ass")
printme("we")
printme(str="can")
print(" ")

#各种传参数
"传不可变对象实例"
def change (a):
    print(id(a)) #原有形参d的内存地址
    a=10    #内部形参被修改
    print(id(a))
a=1
print(id(a)) #与change函数第一个打印的值相同
change(a)    #10的地址
print(" ")
"传可变对象实例"
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值",mylist)
    return 
mylist=[10,20,30]
changeme (mylist)
print("函数外取值",mylist)
print(" ")

"传入参数时可以不按指定顺序"
def printf(name,age):
    "打印任何传入的字符串"
    print("名字：",name)
    print("年龄",age)
    return 
printf(age=50,name="runoob")
print(" ")
"有默认参数时"
def prints(name,age=50):
    print(name," ",age)
    return 
x=input()
prints(x,50)
# prints(x,age)   这个会报错！
prints(x)
print(" ")

#不定长参数
'加了*的参数会以元组（tuple）的形式导入，存放所有未命名的变量参数'
def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出")
    print(arg1)
    print(vartuple)
printinfo(70,60,50)    #>>>70 (60,50)
printinfo(70,60,50,40) #>>>70 （60，50，40）
print(" ")
"若没有指定参数，他就是一个空元组。我们也可以向不同函数传递未命名的变量"
def print_s(arg1,*var):
    "打印任何传入的参数"
    print("输出:")
    print(arg1)
    for i in var:
        print(i)
    return 
print_s(10)
print_s(70,60,50)
print(" ")
"若参数带两个星号**"
def print_f(arg1,**var):#加了两个星号的参数会以字典的形式导入
    print("输出：")
    print(arg1)
    print(var)
print_f(1,a=2,b=3)
print(" ")
"形参表中的星号也可以单独出现，*后的所有参数必须用关键字传入"
def f(a,b,*,c,d):
    return a+b+c+d
#f(1,2,3,4)会报错qwq
#f(1,2,c=3,4)也会报错qwq
x=f(1,2,c=3,d=4)
print(x)
print(" ")

#匿名函数lambda
"就是结构体很简单的函数，只有一句话捏，太简单了以至于不用命名"
x=lambda a:a+10
print(x(5))
sum =lambda var1,var2:var1+10+var2
print(sum(1,2))#冒号后应该为返回值
print(" ")
"我们也可以把匿名函数封装在一个函数内，使用同样的代码来创建多个匿名函数"
def myfunc(n):
    return lambda a:a*n
doubler =myfunc(2)#注意！doubler和tripler后面没有（）！
tripler =myfunc(3)
print(doubler(11)) #2*11
print(tripler(11)) #3*11
print(" ")
'''
#py3.8新增加的：强制位置参数(指定位置参数），msc2019好像运行不了qwq
def f(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
'正确的写法：'f(10,20,30,d=40,e=50,f=60)
#错误的写法1： f(10,b=20bc=30,e=50,f=60),因为b不能使用关键字参数的方式
#错误的写法2： f(10,20,30,40,50,f=60),因为e必须使用关键字参数的方式
'''
"""
"""
#输入和输出
#输出美化的方式:两种输出方式：表达式语句和print（）函数
s = 'hello world'
print(str(s))#str(s)返回一个用户易读的表达形式
print(repr(s))#repr(s)返回一个解释器易读的表达形式
print(repr((1,2,('google\n','baidu'))))
"一个高级一点的输出方式"
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))
"对于上面这种格式化（rjust右对齐填充空格，类似的还有ljust，center）的，我们更经常用print.format"
for x in range (1,11):
    print('{0:2d} {1:3d} {2:4d} '.format(x,x*x,x*x*x))
"还有不够位数则自动在数字左侧补0的.zfill（）"
print('12'.zfill(5))
print('-12.5'.zfill(7))#正负号和小数点都算位置
print('3.14159265359'.zfill(5))#超出就不补了，也不限制
"str.format的用法如下"
print('{}网址："{}!"'.format('b站','www.bilibili.com'))
print('{0}和{1}'.format('google','baidu'))
print('{1}和{0}'.format('google','baidu')) #里面的数字代表出现的次序，从0开始
print('{name}网址：{site}'.format(name='b站',site='www.bilibili.com'))
print('{0}和{1}和{other}'.format('ass','we',other='can'))
"一些格式化的转变,用冒号：实现"
table ={'google':1,'baidu':2,'taobao':3}
for name,number in table.items():
    print('{0:10}==>{1:10}'.format(name,number)) 
import math
print('常量PI的近似值为{0:.3f}'.format(math.pi))#0的意思是，冒号后的意思是至少有这么多宽度
"如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。"
"最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值"
print('baidu:{0[baidu]:d};google:{0[google]:d};taobao:{0[taobao]:d}'.format(table))

#旧式字符串格式化-用 % 操作符
import math
print('PI的值可以近似为：%5.3f'% math.pi)#注意，引号后没有逗号

#读取键盘输入-input()
str =input('请输入：')
print("你个憨憨输入了:",str)

#读写文件，文件处理：暂时略，详见runoob.com/python3/python3-inputoutput.html
"""


#面向对象编程（类class）
class myClass:
    i=12345
    def f(self):
     return 'hello world'
x = myClass()
print('这个类的数字是：',x.i)
print('这个类输出了：',x.f())
"类有一个名为__init__()的构造方法，在类实例化（即用类的定义来创建一个实例，如上面x=myClass())的时候会自动调用"
class Complex :
    def __init__(self,realpart,imagpart):#self 是惯用的参数名称，代表类的实例（不是类），但是它不是关键字，可以替换成其他的。
        self.r=realpart
        self.i=imagpart
x=Complex(3.0,-4.5)
print(x.r,x.i)
#类的方法（类里面的函数,形参表必须包含self，且作为第一个参数，代表类的实例）
class people :
    name=''
    age =0
    __weight =0
    def __init__(self,n,a,w):
        self.name =n
        self.age =a
        self.__weight =w
    def speak(self):
        print("%s 说：我%d 岁,%d 公斤。"%(self.name,self.age,self.__weight))
p=people('daonan',18,30)
p.speak()

#类的继承



