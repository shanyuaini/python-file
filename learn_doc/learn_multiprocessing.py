#_*_coding:utf-8 _*_
__author__ = 'sylar'

'''多进程
在unix系统中所有的程序都是由fork()方法产生,所以每一个进程启动时都会产生一个父进程和子进程,在多进程中所有的进程都有对应的父进程产生
而线程又是最小执行单元,所以每个进程都会有至少一个主线程(不管子进程还是父进程都会有一个线程)
'''
'''
from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:',__name__
    if hasattr(os,'getppid'):
        print 'parent process:',os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello',name

if __name__ == '__main__':
    info('main line')
    print '----------'
    p = Process(target=f,args=('bob',))
    p.start()
    p.join()
'''


'''由于进程不共享内存,所以每个子线程都拿到了各自的数据.
而线程由于是共享内存,所以每个线程都拿到了同一个列表
#在Windows上执行有问题
'''
'''
from multiprocessing import Process
import threading

def run (info_list,n):
    info_list.append(n)
    print info_list

info = []
print '---------Process-----'
for i in range(10):
    p = Process(target=run,args=[info,i])
    p.start()


print '----------Thread------'
for i1 in range(10):
    p = threading.Thread(target=run,args=[info,i1])
    p.start()
'''

'''进程间的通信,由于进程和进程之间的内存独立的,
queue函数来共享
'''
'''
from multiprocessing import Process,Queue
def f(q,n):
    q.put([n,'hello'])      #将hello放入队列.
if __name__ == '__main__':
    q = Queue()   #Queue实例化
    for i in range(5):
        p = Process(target=f,args=(q,i))  #实例化多个进程
        p.start()
        print q.get(),id(q)  #多个进程都是使用的一个q

def f1(q1,n):
    q1.put([n,'hello'])
    print q1.get(), id(q1)
if __name__ == '__main__':
    q1 = Queue()   #Queue实例化
    for i in range(5):
        p1 = Process(target=f1,args=(q1,i))
        p1.start()
'''
'''Array进行内存共享
'''
'''
from multiprocessing import Process,Value,Array
def f(n,a,raw):
    n.value = 3.1415927   #通过value方法给 n复制别传出函数外部
    for i in range(len(a)):
        a[i] = -a[i]
    raw.append(999)
    print raw
if __name__ == '__main__':
    num = Value('d',0.0)   #Value方法设置num为一个可以共享内存的数据
    arr = Array('i',range(10))
    raw_list =range(10)
    print num.value
    print arr[:]
    p = Process(target=f,args=(num,arr,raw_list))  #将num传到每个子进程里处理
    p.start()
    p.join()
    print num.value,num  #此时再使用num的value方法就可以取到进程所共享的同一个数据
    print arr[:]     #同理列表也可以修改为一个负数的列表
    print raw_list   #原生的列表虽然也传到函数里处理了,但是没有使用value方法所以数据没有共享
'''
'''manager进行内存共享,支持大多数据类型
'''
'''
from multiprocessing import Process,Manager
def f(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    print d
    print l
    p = Process(target=f,args=(d,l))
    p.start()
    p.join()
    print d
    print l
'''

'''Lock移植线程的Lock方法 据说没啥用

from multiprocessing import Process,Lock
def f(l,i):
    l.acquire()
    print 'hello world',i
    l.release()
if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        p = Process(target=f,args=(lock, num)).start()
'''


'''进程池.限制最多几个进程同事在运行
'''
'''
from multiprocessing import Pool
import time
def f(x):
    print x*x
    time.sleep(1)
    return x*x
pool = Pool(processes=4)  #进程池数量,同时最多开启的进程数
res_list = []
for i in range(10):
    res = pool.apply_async(f, [i, ])#异步启动进程,默认是启动的不用start

    res_list.append(res)

for r in res_list:
    print r.get(timeout=0.3)
print '--------------------'
print pool.map(f,range(10))
'''

'''异步IO模型 select poll epoll  windows不支持epoll
'''




















