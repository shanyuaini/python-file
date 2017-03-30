#_*_coding:utf-8 _*_
__author__ = 'sylar'
'''
def func(arg,*arg,**kwarg):
#arg 传入参数时对应一个参数.可以设置多个,
def func(arg,arg1,arg2='xx'):
如果arg2 = 'xx' 就是默认参数,定义时必须放在最后,arg2可以不传入值就使用默认值,如果传入了值.arg2就为传入的值

#*args 定义时只用定义一个参数,传入参数时可以任意个参数.事先可以不定义有多少个参数
def func(*arg):pass
func(arg1,arg2,arg3)
#这时候就会将传入的多个参数包装为一个列表传入.

#**kargs 定义时只用定义一个参数,传入参数时可以任意个参数.事先可以不定义有多少个参数
def func(**kargs):pass
func(k1=v1,k2=v2)
#这时候就会将传入的多个参数包装为一个字典传入.此时参数要定义key值
'''



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

###re 正则表达式
import re

re_str = '214sdhk981289hsdhdasjdk90890dsalx'
#match 从字符串开始的地方开始匹配,如果没有匹配就返回none
result_match = re.match('\d+',re_str)
print "      方法--->:",result_match.group()
#search.在整个字符串寻找.直到找到了,返回找到的第一个数据,没有找到返回none
result_search = re.search('\d+',re_str)
print "   search   方法--->:",result_search.group()
#findall 在整个字符串中找到所有的数据,并返回一个列表
result_findall = re.findall('\d+',re_str)
print "    findall  方法--->:",result_findall
#compile 相当于对语句进行编译,加快查找速度.和re用法一样的,编译后的对象可以使用.findall,.search,.match.一次只能检索一个字符串
com = re.compile('\d+')
print "   compile   方法--->:",com.findall(re_str)
#group  将符合条件的字符全部返回
#groups  只返回分组的内容表达式(\d+)的内容
result_group =re.search('(\d+)\w*(\d+)',re_str)
print "      方法--->:",result_group.group()
print "      方法--->:",result_group.groups()

###常用格式
'''
字符
\d 数字
\w 所有字母和数字
\t 制表符
. 除了回车以外的所有字符
次数
* 大于等于零次
+ 大于等于1次
? 0次或者1次
{m} 指定次数
{m,n} 出现m次到n次
'''
ip_str = '12.223.44.sdjklIISidsuf89.sfj.r34.m23oijlse.2_f192.168.33.208fjlkjIS()*(fdd'

print "   ip1   方法--->:", re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip_str)
print "   ip2   方法--->:", re.findall('(?:\d{1,3}\.){3}\d{1,3}',ip_str)
'''
###time
import time
#time 时间戳的值#将日志时间转换为时间戳做日志分析.比正则匹配效率高
print "   time   方法--->:",time.time()
#gmtime 结构化time元组 localtime ,在参数中加如时间戳的变量,就可以将时间戳形式返回为元祖形式的
print "    gmtime  方法--->:",time.gmtime()
print "    localtime  方法--->:",time.localtime()
#strftime 字符串格式化的时间 strptime
print "    strftime  方法--->:",time.strftime('%Y-%m-%d %H:%M:%S')
#print "    strptime  方法--->:",time.strptime('%Y-%m-%d',time.localtime())#可以将元祖方式的转为格式化的时间

#mktime 结构化转时间戳元组转时间戳
#print "    mktime  方法--->:",time.mktime(time.localtime())

#print "      方法--->:",time.asctime(time.localtime()) #将元祖的转为字符串
#print "      方法--->:",time.ctime(time.time())   #将时间戳的转为字符串
#查询函数执行花费的时间
import time
def func():
    start = time.clock()
    print "执行xxx行代码"
    end =time.clock()
    print 'used time ',start-end



import datatime
datetime.date：表示日期的类。常用的属性有year, month, day
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond
datetime.datetime：表示日期时间
datetime.timedelta：表示时间间隔，即两个时间点之间的长度
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
strftime("%Y-%m-%d")
import datetime
print datetime.datetime.now()
print datetime.datetime.now() - datetime.timedelta(days=5)

import sys
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.maxunicode     最大的Unicode值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
print val

import os
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.environ  获取系统环境变量
os.path.abspath(path)  返回path规范化的绝对路径
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
'''
































































