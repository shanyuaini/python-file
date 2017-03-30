#_*_coding:utf-8 _*_
__author__ = 'sylar'


import urllib.request
import urllib
url = 'http://www.whatismyip.com.tw'

#用爬虫去采集代理ip
# iplist =

proxy_support = urllib.request.ProxyHandler({'http':'106.75.128.89:80'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)