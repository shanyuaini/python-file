#_*_coding:utf-8 _*_
__author__ = 'sylar'

dict1 = {
    'name' : 'sylar',
    'age' : 32,
    'job' : 'ops'

}
#遍历keys,values
for k in dict1:print k,dict1[k]
#遍历keys,values 效率低
for k,v in dict1.items():print k,v

#clear 清空字典,相当于dict1.
#print dict1.clear()



#创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值,value只能设置一个
seq = ('name','age','job')
print "   fromkeys   方法--->:",dict1.fromkeys(seq,10)

#get 返回指定key的值，如果值不在字典中返回默认值。不指定默认值则返回none
print "   get   方法--->:",dict1.get('name'),dict1.get('sex')
#has_key 判断字典中是否有对应的key
print "  has_key    方法--->:",dict1.has_key('age')

#items 将整个字典的key和value以两个元祖的方式返回,python3中使用迭代方法,不直接返回列表值
print "   items   方法--->:",dict1.items()
#keys 查看字典所有的key
print "   keys   方法--->:",dict1.keys()
#values 返回字典中的所有values
print "   values   方法--->:",dict1.values()

#view 返回对应的集合
print "   view   方法--->:",dict1.viewitems(),dict1.viewkeys(),dict1.viewvalues()

#iteritems item的迭代方法,python3里已废除直接作为item方法.
for k,v in dict1.iteritems():print k,v
#itervalues() itervalues都是迭代器
print dict1.iterkeys(),dict1.itervalues(),dict1.iteritems()

#pop 删除指定的key,并返回对应的alue,如果没有找到key
#print "    pop  方法--->:",dict1.pop('name')  #能找到
print "    pop  方法--->:",dict1.pop('sex','man')   #没找到,可以指定返回值.没有指定返回值就没有返回

#popitem 随机删一个key,value 并返回他们的值
print "    popitem  方法--->:",dict1.popitem()

#setdefault 给字典添加一个key,value.并返回值,如果key已经存在,则不会改变对应的值,并返回该值.
print "    setdefault  方法--->:",dict1.setdefault('addr','sichuan')


#copy 复制字典,浅copy
dict2 = dict1.copy()
print "   copy   方法--->:",dict2
'''深浅copy
对复杂的数据类型进行copy.由于是对内存对象进行copy.而在字典中.每个key,value都有单独的内存空间
如果字典的一个value又是一个列表或者字典等复杂的数据类型时只是相当于对这个value做了一个软链接.
在修改alue下一级结构中的值时,copy操作的新旧两个字典中的这个value由于是指向同一个内存对象,
会发生两个字典中的值都在改变,这就是浅copy.为了节约内存空间

#copy
dict_info = {
    'list1' : [1,2,3],
    'v2' : 30,
    'v3' : 40
}
copy_info = dict_info
print id(copy_info['v2']),id(dict_info['v2'])
#这种情况,两个字典中的数据都是同一份内存对象.和变量赋值一样,其中一个改变了key,value两个字典都会改变

#浅copy
copy_info = dict_info.copy()
copy_info['v2'] = 35
copy_info['list1'][0] = 5
print copy_info,dict_info
print id(copy_info),id(dict_info),id(copy_info['v2']),id(dict_info['v2']),id(copy_info['list1']),id(dict_info['list1'])
#此时可以看到浅copy时只是对第一层次进行了单独建立内存对象,在第二级因为是还是同一个内存对象.

#深copy
import copy
copy_info = copy.deepcopy(dict_info)
copy_info['list1'][0] = 10
copy_info['v2'] = 35
print copy_info,dict_info
print id(copy_info),id(dict_info),id(copy_info['v2']),id(dict_info['v2']),id(copy_info['list1']),id(dict_info['list1'])
#在实际场景中,会有就是需要copy两份不同内存对象的数据.分别做操作
'''











