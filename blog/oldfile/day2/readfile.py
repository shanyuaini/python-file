#_*_coding:utf-8_*_
'''
Windows和Linux交互的时候要用rb,wb,ab二进制的形式交互
'''


#read
'''
f = file("python1.csv")
for line in f.readlines():
    print line,
f.close()
'''
#write
f =file('test.txt','w')
f.write("this is the first line\n")
f.write("this is the second line\n")
f.write("this is the third line\n")
f.close()
#append
f = file('test.txt','a')
f.write("this is the append line\n")
f.close()
#read and write   r+ w+  r+文件不存在会报错,w+文件不存在会创建

f = file('test.txt','r+')
print 'first line',f.readline()
print 'second line',f.readline()
f.write("change third line")
f.close()
'''
f.tell()       告诉,读文件的时候游标所在的位置
f.seek(7)      游标回到某个位置
f.flush()      把缓存的数据刷新到硬盘上
f.read()       把整个文件内容读入一个字符串
f.readlines()  把一个文件内容读入一个列表
f.xreadlines() 不会把整个文件读到内存里,只会记录一个开始和结束.然后一行一行的从硬盘里读
for line in f.xreadlines():
    print line
f.writelines() 一组字符串,列表写到多个行
f.truncate()   如果不输入位置,从当前游标位置到最后都删除
f.closed       判断文件是否被关闭

'''
#Linux下执行修改文件内容模仿fileinput 模块功能
#import fileinput
#for line in fileinput.input("passwd",inplace=1,backup='.bak'):
#   print line.replace("man","sylar")
import sys
if '-r' in sys.argv:  #sys.argv 读取文件名及参数
    rep_argv_pos = sys.argv.index('-r')#-r参数表示修改
    find_str = sys.argv[rep_argv_pos +1]#-r后第一个参数表示老的字段
    new_str = sys.argv[rep_argv_pos +2]#-r后第二个参数表示新的字段
f = file('passwd','r+')

while True:   #用readline读取文件,因为readlines默认游标在文件最后,后面不方便用seek操作游标
    line = f.readline()   #用变量保存每一行,进行超找
    if find_str in line:
        last_line_pos = f.tell() -len(line)  #记录游标的位置到上一行末尾
        f.seek(last_line_pos)   #将游标定位
        new_line = line.replace(find_str,new_str)#替换字段,并写入新变量
        f.write(new_line)   #将变量写入文件
        print  line
        break
f.close()
'''
###字符编码
在python中直接使用中文会报错,所有的python不进行字符编码申明都会默认以ASCII处理.
Unicode 万国字符集,内存中都是用Unicode
UTF-8: 英文用一个字节存,中文用3个字节

name = "中文"
name1 = u"中文"   #表示数据改为Unicode
name_list =[name, "test"]
print type(name1)
print type(name)
print len(name1)
print len(name)
print name_list

'''
