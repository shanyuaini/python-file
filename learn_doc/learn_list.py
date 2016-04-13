#_*_coding:utf-8 _*_
__author__ = 'sylar'

list_all = ['a','sylar','22','open','4','sklfj','open',16,'sjk113','skf_kjdk','open','skj*&%)','f_s2df']
list_num = [1,4,7,3,5]
list_alp = ['axod','sccde','lsoM','JLKSI','KDIiid']

#append 在列表末尾添加一个值
list_alp.append('append')
print ' append 方法--->:',list_alp

#count 记录一个值在列表中出现的次数
print ' count 方法--->:',list_all.count('open')

#extend将两个表合并
list_all.extend(list_num)
print ' extend 方法--->:',list_all

list_alp.insert(2,'sylar')
print ' insert 方法--->:',list_alp

#index ,打印列表中某个值的index
print ' index 方法--->:',list_all.index('a')

#pop 删除列表中的key和value,默认是最后一个
print ' pop 方法--->:',' pop--->:',list_all.pop(),' list_all--->:',list_all
print ' pop 方法--->:',' pop--->:',list_all.pop(0),' list_all--->:',list_all
#remove 删除列表中找到的值,如果有相同的只删除找到的第一个,如果值不存在会引发一个错误
print ' remove 方法--->:',list_all.remove('open'),' list_all--->:',list_all

#reverse 将列表的元素进行反向排序
print ' reverse 方法--->:',list_all.reverse(),list_all

#sort按照ASCII码给列表排序
print '  方法--->:',list_all.sort(),list_all




