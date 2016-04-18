#_*_coding:utf-8 _*_
__author__ = 'sylar'

import MySQLdb
from day5 import conf


class MySqlHelper(object):

    def __init__(self):

        self.__conn_dict = conf.conn_dict
    def Get_Dict(self,sql,params):

        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCount =cur.execute(sql,params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    def Get_One(self,sql,params):#接受到用户名密码和查询语句
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql, params)#按照用户输入的用户名密码去查找
        data = cur.fetchone() #查找结果返回
        print data
        cur.close()
        conn.close()
        return data
