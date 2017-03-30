最近在学习html感觉眼睛要看瞎了,就写了个文件对比的小玩意,只是简单改了下difflib在这里分享之.写完才发现好像svn和编辑器有这个功能不过只是对比一个文件的历史版本,不知道可不可以对比不同的文件
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 16:17
# @Author  : sylar
# @Site    : 
# @File    : diff.py
# @Software: PyCharm

import difflib
import sys

#获取输入文件
try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print("Error:"+str(e))
    print("Usage: python diff.py filename1 filename2 >diff.html!")

#读取文件函数
def readfile(filename):
    try:
        fileHandle = open(filename,'rb')
        text=fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print("readfile error:"+str(error))
        sys.exit()

#默认生成的html不支持utf8.做了下字符串拼接的函数
def utf8_str(msg):
    meta_str = '<meta charset="UTF-8">'
    msg = msg.split('<head>')
    out_html = '{0}{1}\n    {2}{3}'.format(msg[0], '<head>',meta_str, msg[1])
    return out_html

#简单检查参数 
if textfile1 == "" or textfile2 == "":
    print("Usage: python diff.py filename1 filename2 >diff.html!")
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

#实例化HtmlDiff()
d = difflib.HtmlDiff()

#对比文件
msg = d.make_file(text1_lines, text2_lines)
out_html = utf8_str(msg)

print(out_html)
```

![](http://7xread.com1.z0.glb.clouddn.com/246d2dc8-5186-4fdf-86d9-612c976ad90e)