#_*_coding:utf-8 _*_
__author__ = 'sylar'


from threading import Thread


def foo(arg):
    print arg



t1 = Thread(target=foo,args=(1,))  #一个线程对象
t1.start()  #开始运行一个线程


