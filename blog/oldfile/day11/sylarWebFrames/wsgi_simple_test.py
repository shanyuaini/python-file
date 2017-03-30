#_*_coding:utf-8_*_
__author__ = 'sylar'

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server  #通过这个模块建立一个服务器和浏览器交互

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']



if __name__ == '__main__':

    httpd = make_server('', 8001, simple_app)
    print "Serving on port 8001..."
    httpd.serve_forever()