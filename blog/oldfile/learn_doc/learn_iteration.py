#_*_coding:utf-8 _*_
__author__ = 'sylar'

###反射
#1,将字符串做模块名称使用
temp = 'sys'
model = __import__(temp)
print "   __import__   方法--->:",model.path
'''例子
while True:
    reflex = raw_input('输入你要导入的模块')
    if reflex in ['os','sys']:
        model_foo = __import__(reflex)
        print "   __import__   方法--->:", model_foo.path
    else:
        print "输入错误重新输入"
'''
#2,将字符串当作函数名执行函数
func = 'path'
#getattr 去模块中找函数,如果找到函数,返回整个函数
print "   getattr   方法--->:",getattr(model,func)
#hasattr判断模块中是否有某个函数
print "   hasattr   方法--->:",hasattr(model,func)


###装饰器
def login(func):  #执行装饰器时,将原函数传入装饰器 ,这一步主要是将要原函数传入装饰器内
    def wrapper(arg):  #真正的装饰器函数申明,并接受原函数的参数
        user =raw_input("login(原函数执行前添加的代码):").strip()
        if user == 'sylar':
            print "---Welcome login---(原函数执行前添加的代码)"  #要装饰的代码执行前所执行的代码!
        result = func(arg)      #此时在装饰器内执行原函数 task(str_arg)被func(arg)
        print "原函数执行后添加的代码"     #在原函数执行完之后要加入的代码
        return result   #此时返回原函数的返回值返回给装饰器wrapper
    return wrapper   #将装饰器的函数体返回给login,注意不能加().不然在调用装饰器时就会自动执行.

@login   #调用装饰器,此时会将task函数体当作参数传入login函数
def task(str_arg):#原函数
    if str_arg == 'something':#这里是是验证task('something') 传入的参数没有问题
        print "原函数体 !",str_arg
        return 'someth'  #原函数返回一个返回值,也是没有问题的.
res =  task('something')  #此时执行的原函数task()已经被替换为login()
print res


###函数的递归,把这一次执行的结果.当作下一次执行的输入参数
def calc(n):
    if n / 2 > 0:
        print '->',n
        calc(n/2)
    print '----------'
calc(12)

def calc1(n):
    print '--->',n
    if n/2 > 0:
        return calc1(n/2)
    print '----------'
    return n
print calc1(12)
#可以看到calc完整的执行了4次,而calc只完整执行了一次


###二分查找,快速查找海量数字
data_list = range(0,100)
def binary_search(find_num,data):
    mid = len(data)/2       #先取得列表的长度中间值
    if mid > 0:
        if find_num > data[mid]:#如果传入的数 大于传入列表的中间数就取列表中间数的右边部分
            print 'data should in right',mid,data[mid:]
            binary_search(find_num,data[mid:])#用递归方法将结果传回函数继续判断
        elif find_num < data[mid]:#如果传入的数 小于传入列表的中间数就取列表中间数的左边部分
            print 'data should in left',mid,data[:mid]
            binary_search(find_num, data[:mid])#用递归方法将结果传回函数继续判断
        else:
            print 'find the num: %s'%data[mid]
    elif data[0] == find_n:
        print '\033[32;1mfind the num: %s\033[0m'%data[mid]
    else:
        print 'cannot find the num',find_n

if __name__ == '__main__':
    find_n =raw_input('find:').strip()
    if find_n.isdigit():
        find_n = int(find_n)
        binary_search(find_n,data_list)#将输入的数字作为binary_search的find_num参数传进去
        if find_n in data_list:
            print '--->%s exist in list'%find_n


###迭代器 yield
'''
当我们用range(1000)的时候,会直接在内存中直接生成整个列表
而当我们使用xrange(1000)时,会将整个文件句柄返回.就只记录开始,结束和当前值.
我们使用的时候就由迭代器每次加1循环.可以大量节省内存,和查询时间
###
在一个函数执行时,就要等待一个函数的结束才能继续执行函数后面的代码(阻塞)
使用迭代器就可以在必要的时候记录当前状态并跳出函数.执行其它的代码
当我们需要是有可以跳回函数里执行函数里的代码.
迭代最后一次执行时会返回一个异常来
'''
def run():
   '''
    import time
    print 'test1,第一次跳出'#模拟去交互数据.比如去访问外部一个很慢的网站需要5秒才能响应
    yield 1#用sleep模拟此处需要交互等待的一段时间
    time.sleep(5)
    print 'test2,第二次跳出'
    yield 2
    print 'test3,第三次跳出'
    yield 3
    print 'test4,第四次跳出'
    yield 4
    '''
   for i in range(4):
       print '我函数的第%s次运算完成,就去执行后续代码'%i,i
       yield i

task = run() #这个时候run()已经变成了一个迭代器,不会执行
task.next() #第一次进入函数执行到遇到第一个yield时跳出来执行后续代码
print '这段时间我可以去执行其它的代码,当这里运算完成了'
print '第一次跳回函数'
task.next()#外面的代码执行到这里就跳回函数里执行,遇到第二个时跳出.
print '执行其它的代码'
print '第二次跳回函数'
task.next()
print '执行其它的代码'
print '第三次跳回函数'
task.next()
print '第四次跳回函数'
print '执行其它的代码'


###异常处理
'''
正常情况下当程序出错时,程序就崩溃了.有的时候我们希望程序出错了,但是不跳出程序
try:  #标记需要抓取异常的代码段
    #正常代码
    #
except NameError,err:     #对异常的处理.NameError抓取哪一类异常,err异常信息
    print err  #对异常信息做什么操作
#常用异常类型
AttributeError                  试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError                            输入/输出异常；基本上是无法打开文件
ImportError                     无法引入模块或包；基本上是路径问题或名称错误
TypeError                         传入对象类型与要求的不符合
IndexError                       下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError                           试图访问字典里不存在的键
KeyboardInterrupt           Ctrl+C被按下
NameError                       使用一个还未被赋予对象的变量
UnboundLocalError          试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError                       传入一个调用者不期望的值，即使值的类型是正确的
下面这两类抓不住
SyntaxError                      Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
IndentationError             语法错误（的子类） ；代码没有正确对齐
'''
try:
    name = 'sylar'
    name_list = ['tom','jerry','sylar']
    #print  Name
    #print name_list[4]
    f = file('xxx.py')
except NameError, a:  #name类型异常
    print a
except IndexError, b:    #index类型异常
    print b
except Exception, all:  #Exception 是抓住所有类型的异常
    print all
else:
    print '---no err happend'  #当所有的except语句没有执行.就会执行else!
finally:
    print '---no matter ' #无论有没有抓到异常都会执行finally,通常来做收尾工作,关闭文件之类
print '----do something else----' #正常情况下代码执行不到这里,因为前面有了异常程序就崩溃了

#自定义异常类型
class myException(Exception): #自定义一个异常
    pass
try:
    print '----doing somethin----'
    raise myException   #raise语句触发异常,可以出发系统默认异常,也可以出发自定义异常,
                        # 比如连接mysql,可以将mysql异常定义为自己的异常来触发
except myException, c:
    print '我自己做的异常'

###断言,必须满足这个条件就会继续往下走,负责就引发一个异常
#assert (1 == 1)





















