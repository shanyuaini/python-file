#_*_coding:utf-8_*_
'''函数的定义
def sayHi(name,age,job):
    print "Hello, %s ,How are you?"  %name,age
    print "MY age" , age
    print "my job" , job

sayHi('sylar',22,'it')
def sayHi(name,age,job='IT'):  #默认参数有值
    print "Hello, %s ,How are you?"  %name,age
    print "MY age" , age
    print "my job" , job
sayHi('sylar',22,'hr')

def sayHi(name,age,job='IT',salary):  #不能将有默认值的参数放在没有默认值的参数前面
    print "Hello, %s ,How are you?"  %name,age
    print "MY age" , age
    print "my job" , job
sayHi('sylar',22,'hr',5000)
'''
'''函数的赋值   a 被称为关键参数,必须赋值
def func(a,b=5,c=10):
func(3,7)  #a = 3 ,b = 7, c = 10
func(25,c=24) #a=25,b=5,c=24
func(c=50,a=100) #a=100,b=5,c=50

'''
'''局部变量和全局变量
局部变量值在一段代码生效的变量,

name = 'tom' #全局变量
def sayhi():
    print name
    name2 = 'jerry'  #局部变量
    print name
print name
函数内部的局部变量不能和全局变量重名!并且全局变量传到函数里不能修改
name = 'tom' #全局变量
def sayhi():
    print n
    n = 'jerry'  #局部变量
    #name = 'tom'  #错误
    print name
sayhi(name)
要在函数内修改全局变量,必须要在函数内声明,
name = 'tom' #全局变量
def sayhi():
    global name
    name = 'jerry'  #此时可以修改,但是不建议这么使用
    name2 = 'jerry'  #局部变量
    print name
'''
'''函数返回值;将函数执行完成的结果return,默认可以没有返回值
def sayhi(name):
    print name
print sayhi('jj')

return 代表函数的结束.并返回一个值
def multiply(x,y):
    if x>y:
        return x/y
    else:
        return x*y
res = multiply(6,2)
if res>30:
    print "doing somethin"
else:
    print "do else"
'''
'''不知道函数有多少个参数,此时参数传进来是一个元祖
def sayhi(*args):
    print args
sayhi('arg1','arg2')
#在不知道参数的顺序规则时,可以让使用者按规则定义参数,此时参数传进来是一个字典
def sayhi(**):
    if kwargs.has_key('name')
        print kwargs['name']
sayhi(name='sylar')
'''
'''匿名函数
g = lambda x: x**2   #匿名函数的方式
g=(4)
print g(4)

示例1
def f(x):     #正常函数
    return x**2
print map(f, range(10)) #将range(10)的值赋给f运算
这个过程就可以简化为
prit map(lambda x:x**2,range(10))
示例2#给字典排序输出
dic1 ={9:2,4:3,'a':'test','*':'$'}
print sorted(dic1.items(),key = lambda x:x[0])
'''

'''
#迭代器,只记录一个开始和结束,当循环时,按照规则递增,并只记录当前位置输出
import time
def run():
    print "test 1"
    time.sleep(1)
    print "test 2"
    time.sleep(1)
    print "test 3"
    time.sleep(1)
    print "test 4"
    time.sleep(1)
run()
print "doing sth else"  #此时程序是阻塞的,必须等待函数执行完毕才能执行后面的代码

def run():
    print "test 1"
    yield 1
    time.sleep(1)
    print "test 2"
    time.sleep(1)
    print "test 3"
    time.sleep(1)
    print "test 4"
    time.sleep(1)
run() #此时函数就不会运行
print type(run())#此时函数就编程了一个迭代器,
print "doing sth else"


def run():
    print "test 1"
    yield 1  #中断函数,并保存函数现在的状态
    time.sleep(1)#比如说去调用外面的网页,需要等待时间,用sleep模拟等待时间
    print "test 2"
    yield 2
    time.sleep(1)
    print "test 3"
    yield 3
    time.sleep(1)
    print "test 4"
    yield 1
    time.sleep(1)
task =run()
task.next()#从yield中断处,跳回函数
print "doing sth else" #此时去处理其它的代码,
task.next()
print "doing sth else2"
task.next()
print "doing sth else3"


def run1():
    for i in range(100):
        print '-->',1
        yield i
task1 =run1()
task1.next()#从yield中断处,跳回函数
print "doing sth else" #此时去处理其它的代码,
task1.next()
print "doing sth else2"
task1.next()
print "doing sth else3"
'''
'''
a = range(10)
print [i for i in a if i<5]  #先循环for i in a 再判断i大于5 ,就将值赋给i 输出
'''
'''
#序列化
dic1 = {1:3}
import pickle   #import json
f = file('test.pkl','w')   #f = file('test.json','w')
pickle.dump(dic1,f)  #json.dump(dic1,f)
print pickle.dumps(dic1)
f.close()
#反序列化
f =file('test.pkl')   #f = file(test.json)
data =pickle.load(f)  #data = json.load(f)
print data
'''
'''正则表达式 http://www.cnblogs.com/huxi/archive/2013/02/05/2892479.html

import re
a = 'lsjljdkj*(@*jkd92839ksdjkl819009dsjd0)_2j'
m=re.match("\w",a)  #从开头匹配
print m.group()
m=re.match("\w+",a)
print m.group()
m=re.match("[a-zA-Z]+",a)
print m.group()
m=re.search("ksdjk",a)  #查找
print m.group()
print re.findall('[a-zA-Z]+',a)  #
print re.findall('[^a-zA-Z]+',a)
print re.split('\d+',a)
print re.sub('\d+',"|",a)
print re.sub('\d+',"|",a,count=2)
'''
'''分组

import re
ip= '10.34.134.3'
re.search('\d+.',ip)
re.search('\d+.',ip).group()
m=re.search('(?P<first>\d+.)(?P<sencond>\d+.)',ip).groups()
m.groupdict()
'''
'''创建模块 pypi.python.org  pip打包官方存放地
pip install  #这个自动去pypi找安装包
easy_install

def func1():
    pass
def func1():
    pass
def func1():
    pass
if __name__ == '__main__'#当执行模块自身时就从这里开始执行,如果当模块调用.则需要执行模块名及函数
    print :priactive'
    func1
    func2
    func3
python标准库,(书名)
'''

'''函数递归,把这一次函数执行的结果当下一次执行的输入

def calc(n):
    if n/2>0:
        print '-->',n
        calc(n/2)
calc(12)

def calc(n):

    if n/2>0:
        return calc(n/2)
    print '-------'
    return n
print calc(12)

def calc(n):
    if n/2>0:
        calc(n/2)
    print '-------'
    return n
print calc(12)
'''
'''二分查找
'''
data_list = range(0,100,2)

def binary_search(find_num,data):
    mid = len(data)/2
    if mid > 0:
        if find_num >data[mid]:
            print "data should in right",mid, data[mid:]
            binary_search(find_num,data[mid:])
        elif find_num < data[mid]:
            print "data should in left",mid,data[:mid]
            binary_search(find_num,data[:mid])
        else:
            print"find the num:%s" %data[mid]
    elif data[0] == find_n:
        print "\033[32;1mfind the num %s\033[0m"% data[mid]
    else:
        print "cannot find the num",find_n
if __name__ == '__main__':
    find_n =raw_input("find: ").strip()
    if find_n.isdigit():
        find_n = int(find_n)
        binary_search(find_n,data_list)

        if find_n in data_list:
            print '--->%s exist in list'


'''作业信用卡
功能要求1 额度15000
2,可以体现,手续费5%
3,每月最后一天出账单(每月30天)写入文件
4,记录每月日常消费流水
5,提供还款接口
优化
每月10号为还款日,过期未还,安全欠款额0.05%计息

'''