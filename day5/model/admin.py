#_*_coding:utf-8 _*_
__author__ = 'sylar'


from day5.utility.sql_helper import MySqlHelper




class Admin(object):
    pass
    def __init__(self):
        self.__helper = MySqlHelper()

    def Get_One(self, id):
        sql = 'select * from admin where id =%s'
        params = (id,)
        return self.__helper.Get_One(sql, params)
    def check_validate(self,username,password):#接收用户输入的帐号密码
        sql = 'select * from admin where name=%s and password=%s'#将要执行的SQL语句做为参数
        params = (username,password)#将用户输入的帐号密码作为参数
        return self.__helper.Get_One(sql,params)#将两个参数传入utility.sql_helper.py

'''
from utility.sql_helper import MySqlHelper
class Admin(object):

    def __init__(self):
        self.__helper = MySqlHelper
    def Get_One(self,id):
        sql ='select * from admin where id =%s'
        params = (id,)
        return self.__helper.get_one(sql,params)
    def check_validate(self,id):
        sql = 'select * from admin where name=%s and password=%s'
        param = (id,)
        return self.__helper.Get_One(sql,param)

'''

