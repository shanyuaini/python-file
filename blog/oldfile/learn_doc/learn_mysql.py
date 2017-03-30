#_*_coding:utf-8 _*_
__author__ = 'sylar'

'''
#查
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')#打开连接服务器
cur =conn.cursor()#打开连接
reCount = cur.execute('select * from admin')  #有多少行
print reCount
data = cur.fetchall()   #把这条语句得到的语句全拿出来
print data
cur.close()
conn.close()
'''
'''
#增
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor()
sql = 'insert into admin (name,address) values(%s,%s)'  #操作的sql语句
params = ('sylar_1','china')  #插入的数据
reCount = cur.execute(sql, params)
conn.commit()  #提交数据
cur.close()
conn.close()
#插入多条
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor()
sql = 'insert into admin (name,address) values(%s,%s)'  #操作的sql语句
params = [
    ('sylar_1','china')  #插入的数据
    ('sylar_2','usa')
]
reCount = cur.executemany(sql, params)
conn.commit()  #提交数据
cur.close()
conn.close()

'''
'''
#删
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor()
sql = 'delete from admin where name = %s'  #操作的sql语句
params = ('sylar_1',)  #插入的数据
reCount = cur.execute(sql, params)
conn.commit()  #提交数据
cur.close()
conn.close()
'''
'''
#改
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor()
sql = 'update admin set name = %s where id = 3'  #操作的sql语句
params = ('sylar_1',)  #插入的数据
reCount = cur.execute(sql, params)
conn.commit()  #提交数据
cur.close()
conn.close()
'''
'''
#事务性
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor()
sql = 'update admin set name = %s where id = 1'  #操作的sql语句
params = (0,)  #改的数据的数据
reCount = cur.execute(sql, params)

sql = 'update admi set name = %s where id = 2'  #操作的sql语句
params = (200,)  #改的数据的数据
reCount = cur.execute(sql, params)
conn.commit()  #默认是加了事务的.两个都执行成功了才提交
cur.close()
conn.close()
'''
'''
#取列名
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor(cursorclass= MySQLdb.cursors.DictCursor)
reCount = cur.execute('select * from admin')
data = cur.fetchall()
cur.close()
conn.close()

print reCount
print data
'''
'''
#按条输出fetchone , fetchmany
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user= 'root', passwd = '123456',db = 'day5')
cur =conn.cursor()
reCount = cur.execute('select * from admin')
print cur.fetchone()
#cur.scroll(1,mode='absolute')   #absolute,数据太少,没实验是什么功能
print cur.fetchone() #一条一条的输出
cur.scroll(-1,mode='relative')   #relative跳回上一条
cur.close()
conn.close()
'''
#获取自增长的ID,插入其它表,做表关联
import MySQLdb
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', passwd = '123456', db = 'day5')
cur = conn.cursor()
sql = 'insert into media (address) values (%s)'
params = ('china',) #这种情况下china后面要加个逗号,不然会一直报参数不足
reCount = cur.execute(sql,params)
conn.commit()
media_id = int(cur.lastrowid)  #获取新插入的字段的id
sql1 = 'insert into content (media_id) values (%s)'
params1 = (media_id,)
reCount1 = cur.execute(sql1,params1)
conn.commit()



