#_*_coding:utf-8_*_
__author__ = 'jieli'

from wsgiref.simple_server import make_server
import re

from day11.sylarWebFrames.app import urls


def url_parse(request,start_response):

    request_url = request.get("PATH_INFO")
    #print '---path:',request_url
    for item in urls.url_list:
        pattern,view_func = item
        #print request
        m = re.match(pattern,request_url)
        if m:
            return view_func(request=request,http_response=start_response)
    else:
        html =  '<h2>Does not match any of this below urls</h2><p style="color:red">'

        for i in urls.url_list:
            html += '%s<br/>' % i[0]

        html += "</p>"

        status = '404 OK'
        headers = [('Content-type', 'text/html')]

        start_response(status, headers)

        return [html]


def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    #start_response(status, response_headers)
    return url_parse(environ,start_response)



if __name__ == '__main__':

    httpd = make_server('', 8001, simple_app)
    print "Serving on port 8001..."
    httpd.serve_forever()