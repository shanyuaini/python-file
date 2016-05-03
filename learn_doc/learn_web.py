#_*_coding:utf-8 _*_
__author__ = 'sylar'



#www.cnblogs.com/wupeiqi/articles/4491246.html
#python 的web规范wsgi #day11
from wsgiref.simple_server import make_server




def Runserver(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    userUrl = environ['PATH_INFO']
    if userUrl == '/index/':
        return '<h1> Hello Web</h1>'
    elif userUrl == '/login/':
        return '<h1> login</h1>'
    else:
        return 'not find'


if __name__ == '__main__':
    httpd = make_server('',8000,Runserver)
    print 'serving http on port 8000'
    httpd.serve_forever()


#MVC和MTV
'''
MVC:Model,View.Controller
Controller:主要是业务处理.
model:主要是数据库相关
View:是html文件
MTV:Model,Template,View
model:主要是数据库相关
View:业务相关
template: html
'''
