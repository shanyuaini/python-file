#_*_coding:utf-8 _*_
__author__ = 'sylar'

dict1 = {}
list1 = 'abcdef'.strip()
for k,v in enumerate(list1):
    print k,v
    dict1[k] = v
print dict1
for i in dict1:
    i
    print dict1[i]



reversed(list1)