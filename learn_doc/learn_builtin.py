#_*_coding:utf-8 _*_
__author__ = 'sylar'

list_info = [1,2,3,4]
dict_info = {
    'k1' : 'v1',
    'k2' : 'v2'
}
#help 获取帮助
print "    help  方法--->:", help(list_info)

#dir 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
#如果参数包含方法__dir__(),该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print "   dir   方法--->:", dir()

#vars 对应dir所列出来的key,返回key和value
print "   vars   方法--->:",vars(),

#type 查看对象属性
print "\n   type   方法--->:",type(dict_info)

#import,reload 导入模块,reload强制重新导入,from 导入某个模块中的函数,变量
import os
reload(os)
from sys import path


#id 查看对象的内存ID编号
print "   id   方法--->:",id(list_info)

#cmp 传入两个对象x,y 如果x小于y返回-1,相等返回0,x大于y返回1
print "   cmp   方法--->:",cmp(2,3),cmp(2,2),cmp(2,1)

#abs 取绝对值
print "   abs   方法--->:", abs(-9)
#bool 去bool值
print "   bool   方法--->:", bool(-1),bool(1),bool(0)

#divmod 传入两个参数x,y.用x除以y,返回两个参数,第一个参数是商,第二个数是余数.用在自动分页
print "  divmod    方法--->:",divmod(10,2)

#max,min,sum,pow 最大值,最小值,和
print "    max,min,sum  方法--->:",max(list_info),min(list_info),sum(list_info)
#pow x的y次方再除以z的余数,只有两个参数就直接返回乘方
print "     pow 方法--->:",pow(2,10)
print "     pow 方法--->:",pow(2,10,3)

#len 返回对象序列或集合的项数。
print "   len   方法--->:",len(list_info)

#all 如果所有的为真.才返回真
print "   all   方法--->:",all([1,2,3,1])
print "   all   方法--->:",all([1,2,3,0])

#any只要一个为真,返回真
print "   any  方法--->:",any([1,0,0,0])
print "   any   方法--->:",any([0.0,0,0])

#chr ASCII字符对应的数字编号.根据数字查字符
print "   chr   方法--->:",chr(70)
print "   chr   方法--->:",chr(71)
print "   chr   方法--->:",chr(72)
#ord ASCII字符对应的数字编号,根据字符查数字
print "   ord   方法--->:",ord('a')
print "   ord   方法--->:",ord('b')
print "   ord   方法--->:",ord('c')
#hex,bin,oct 数字对应的16进制,2进制,8进制
print "  hex    方法--->:",hex(20)
print "   bin   方法--->:",bin(20)
print "    oct  方法--->:",oct(20)

#range 从x,开始循环到y,每次循环x+z.  既x开始,y停止,步长z
print "   range   方法--->:",range(100,200,2)
#range 的迭代方法.返回一个生成器.
for i in xrange(100,200,2):print "  xrange    方法--->:", i

#enumerate 输出列表的key,并可以定义key的起始值
list_cninfo = ['中文','英文','德文','俄文']
for i in enumerate(list_cninfo,1):print "   enumerate   方法--->:",i[0],i[1]


#format 格式化输出字符.相当于%s
s = "my name is {0},i'm {1} years old"
print "      方法--->:",s.format('sylar','18')

#apply 填入函数和函数的参数.并执行函数
def Func(you_arg):print "  apply    方法--->:",you_arg
apply(Func,(['sylar']))

#map 遍历序列里的每一个参数传入函数中,并返回结果.函数体计算结果
print "   map   方法1--->:",map(lambda x:x+100,list_info)
def foo_map(arg):
    return arg+100
print "   map   方法2--->:",map(foo_map,list_info )
#相当于进行下面这样的运算
temp =[]
for item in list_info:
    temp.append(item + 100)
print temp
#filter 遍历序列里的每一个参数传入函数中,进行过滤
def foo_filter(arg):
    if arg > 2:
        return True
    else:
        return False
print "   filter   方法--->:",filter(foo_filter,list_info)
print "   filter+lambda   方法--->:",filter(lambda x:x > 2,list_info)
#reduce 遍历序列并累加,每次的返回值和剩下的元素传入函数体继续操作,直到只返回一个值,必须传入两个参数
print "   filter+lambda   方法--->:",reduce(lambda x,y:x + y ,list_info)

#zip 将多个序列重新组合为元祖,当对于key没有值时就不生成元祖
x = [1,2,3,4]
y = [4,5,6,7]
z = [7,8,9,1]
print "   zip   方法--->:",zip(x,y,z)
x1 = [1,2,3,4,5]
y1 = [4,5,6,7]
z1 = [7,8,9,]
print "   zip   方法--->:",zip(x1,y1,z1)

#eval 将字符串做表达式进行运算
a1 = '8*8'
a2 = '16+8'
print "   eval   方法--->:",eval(a1),eval(a2)

###反射
#1,将字符串做模块名称使用
temp = 'sys'
model = __import__(temp)
print "   __import__   方法--->:",model.path
'''例子
while True:
    reflex = raw_input('输入你要导入的模块')
    if reflex in ['os','sys']:
        model_foo = __import__(reflex)
        print "   __import__   方法--->:", model_foo.path
    else:
        print "输入错误重新输入"
'''
#2,将字符串当作函数名执行函数
func = 'path'
#getattr 去模块中找函数,如果找到函数,返回整个函数
print "   getattr   方法--->:",getattr(model,func)

#hasattr判断模块中是否有某个函数
print "   hasattr   方法--->:",hasattr(model,func)

#delattrs删除模块中某个函数
#print "   delattr   方法--->:",delattr(model,func)

###常用模块:
import random
print "   random   方法--->:", random.random()  #生成0到1之间的随机数
print "   randint  方法--->:",random.randint(1,10)#在某个范围内生成一个随机数x<=i<=y
print "   randrange  方法--->:",random.randrange(1,10,)#在某个范围内生成一个随机数x<=i<y
#简单的验证码
checkcode =[]
for i in range(6):
    current = random.randrange(0,6)
    if current != i:
        temp1 = chr(random.randint(65,90))
    else:
        temp1 = str(random.randint(1,9))
    checkcode.append(temp1)
print ''.join(checkcode)

#md5加密
import hashlib
m = hashlib.md5()
m.update('admin')
print m.hexdigest()
print m.digest()


###pickle 序列化,将数据转换为一种特殊数据模型,以方便进程间的数据交互
# python的特殊数据模式,python的所有对象都可以用pickle传输,json只能序列化常用数据类型
import pickle
#dumps将数据转换为pkl模式的数据加载到内存
str_dumps =pickle.dumps(dict_info)
print "   dumps   方法--->:",str_dumps
#dump 将数据转换为pkl模式的数据写到pkl文件
with open('test.pkl','wb') as f:
    pickle.dump(dict_info,f)
#loads反序列化,将序列化数据转换为普通模式的数据类型
str_loads = pickle.loads(str_dumps)
print "   loads   方法--->:",str_loads
#load 反序列化,将序列化的文件转换读入内存
with open('test.pkl','rb') as f:
    result_pkl = pickle.load(f)
    print "   load   方法--->:",result_pkl