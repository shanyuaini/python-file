#_*_coding:utf-8 _*_
__author__ = 'sylar'


from threading import Thread
import  time
class MyThread(Thread):
    def run(self):

        print '我是线程'
        Thread.run(self) #

def Bar():
    print  'bar'



t1 = MyThread(target=Bar)
t1.start()

print 'over'