#_*_coding:utf-8 _*_
__author__ = 'sylar'

import urllib,json,time
from urllib import request
from urllib import parse

#while True:
content = input("请输入待翻译的内容(输入Q退出程序):")
if content == 'q':
    flag = False
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data = {
    'type': 'AUTO',
    'i': content,
    'doctype': 'json',
    'xmlVersion': '1.8',
    'keyfrom': 'fanyi.web',
    'ue': 'UTF-8',
    'action': 'FY_BY_ENTER',
    'typoResult': 'true'
}    #通过观察网页的form_data,补充浏览器的访问数据
data = urllib.parse.urlencode(data).encode('utf-8')#将的python数据转换为Unicode的utf-8编码
#伪装浏览器方法1
# #head ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
#req = urllib.request.Request(url, data, head)
#伪装浏览器方法2
req = urllib.request.Request(url, data,)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36')


response = urllib.request.urlopen(req)  #将url和data数据传入 用urlopen方法去打开网页
html = response.read().decode('utf-8')  #将unicode文件专为utf-8编码文件
print(html)
target = json.loads(html)
#print(html)
#{"type":"EN2ZH_CN","errorCode":0,"elapsedTime":1,"translateResult":[[{"src":"i love you","tgt":"我爱你"}]],"smartResult":{"type":1,"entries":["","我爱你。"]}}
#网站传回来的数据不符合要求

print(target["translateResult"][0][0]['tgt'])

