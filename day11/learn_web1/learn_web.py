#_*_coding:utf-8 _*_
__author__ = 'sylar'
from wsgiref.simple_server import make_server


def index():
    return 'index'
def login():
    #file打开html文件
    #html文件读取

    return 'login'
url = (
    ('/index/',index),
    ('/login/',login),
    ('/manage/',index)
)

def Runserver(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    userUrl = environ['PATH_INFO']    #获取用户输入url

    func = None
    for item in url:
        if item[0]==userUrl:
            func = item[1]
            break
    if func:

        result = func()
    else:
        result = '404 !'
    return result


if __name__ == '__main__':
    httpd = make_server('',8000,Runserver)
    print 'serving http on port 8000'
    httpd.serve_forever()