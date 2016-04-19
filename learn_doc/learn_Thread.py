#_*_coding:utf-8 _*_
__author__ = 'sylar'

'''
进程下的线程是共享主进程的资源
全局解释器锁:防止进程有多个线程同时被执行.同一个进程的子进程同一时间只有一个能获取CPU使用权限(python特有,解决方案就是多进程)
io密集型用多线程,计算密集型用多进程,因为io操作不需要CPU参与,是由线程和硬件资源管理交互

###threading.Thread模块多线程
statr()
getName()
setName()
isDaemon()
setDaemon()
join(timeout)
run()
'''

'''
import  time
from threading import Thread
def foo(arg):
    for item in range(100):
        print item
        time.sleep(1)
#此时创建子线程所执行代码的这个线程就是主线程
t1 = Thread(target=foo,args=('t1',))  #一个线程对象  主线程创建完子线程不等待子线程执行完就继续向下执行
t1.start()  #开始运行一个线程
t1.join()   #主线程会等待子线程执行完.设置参数可以定义主线程等待几秒
print t1.getName()

t2 = Thread(target=foo,args=('t2',))  #一个线程对象
t1.setDaemon(True) #定义为一个daemon子线程.此时主线程会等待子线程
t2.start()  #开始运行一个线程
print t2.getName()
'''

'''
线程锁
import time
import threading
num = 0
def run(n):
    time.sleep(1) #模拟任务处理时间
    global num #引用全局变量
    num +=1   #执行操作
    print '\n%s'%num #返回输入
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()
这段代码就演示了启动了100个线程做同样的工作,但是由于没有对变量访问控制.造成了某些线程同时拿到了变量.所以返回了相同的值.造成最终结果出错
因此在对线程工作时要对某些变量进行加锁的操作.加锁以后其它的线程不能对该变量进行修改.只有当一个线程释放了锁.其它的线程才能去取得变量
'''

'''
import time
import threading
num = 0
def run(n):
    time.sleep(1) #模拟任务处理时间
    global num #引用全局变量
    lock.acquire()   #加锁
    num +=1   #执行操作
    lock.release()#释放锁
    print '\n%s' % num  # 返回输入
lock = threading.Lock()#申明锁
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()
'''
'''
import time
import threading
num = 0
num2 = 0
def run(n):
    time.sleep(1)
    global num
    global num2
    lock.acquire()
    num += 1
    lock.acquire()  #一个锁使用两次,就是死锁.此时就只能使用RLock.当然加了几把锁必须要释放几次
    num2 += 2
    lock.release()
    lock.release()
    print '\n%s,%s' %( num,num2)
lock = threading.RLock()#申明递归锁
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()
'''

'''
信号量.因为每次是多个线程同时获得锁.此时虽然数据是加了锁.但是同时拿到锁线程又可能会产生数据不一致.
''''''
import time
import threading
num = 0
def run(n):
    time.sleep(1)
    global num
    samp.acquire()
    time.sleep(1)
    num += 1
    print '\n%s,' % num
    samp.release()
samp = threading.BoundedSemaphore(4) #同时允许4个线程去访问数据
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()
'''
'''
简单的异步模拟,异步主要是靠事件(event)触发. select单进程异步
'''
import threading
import time
def producer():
    print '生产者:等人来买东西...'
    event.wait() #阻塞检测标致位值 等待时间出发.消费者来了没有
    event.clear()  #如果wait等待到标志位值为true就执行后面的代码.先将标志位还原.
    print '生产者:有人来了,'
    print '生产者:找东西'
    time.sleep(5)
    print '生产者:东西找到了'
    event.set()

def consumer():
    print '消费者:去买东西...'
    event.set() #设置标志位值,触发事件
    print '消费者:等待找东西'
    time.sleep(2)
    event.wait() #不断的去检测.set的值
    print '消费者:付钱'



event = threading.Event()
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()