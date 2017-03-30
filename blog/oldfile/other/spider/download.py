#_*_coding:utf-8 _*_
__author__ = 'sylar'

import urllib
import urllib.request
import urllib.parse
import re,json
from bs4 import BeautifulSoup


#pip install beautifulsoup4  pip install lxml
url = 'http://www.xicidaili.com/'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html)


print(soup.find_all(id="ip_list"))
iplist = re.findall('(?:\d{1,3}\.){3}\d{1,3}',html)
print(iplist)

'''
iplist = (re.findall('(?:\d{1,3}\.){3}\d{1,3}',html))
print(iplist)
ipdict = {}
for i in iplist:
    print(i)
    re.findall(i+'</td>
    <td>')
    '''