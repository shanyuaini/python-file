#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 12:38
# @Author  : sylar
# @Site    : 
# @File    : day1_homework.py
# @Software: PyCharm
'''
作业一编写登录接口
-输入用户名密码
-认证成功后显示欢迎信息
-输错三次后锁定,
思路:1,首先生成用户字典.包括一个计数器.本来想把计数器的值也保存,感觉有点难
2,生成几个基础变量
3,先去找目录下面是否有lock_user的记录文件.
4,用户名先判断一次是否被锁定
5,如果没有锁定则判断用户名是否在列表中
6,通过用户名在字典中读取密码,判断密码是否正确
7,最后判断是否输错密码3次,如果是3次就将用户名写到lock_list文件中
'''

user_dict = {"sylar" : "123456",
             "jt" : "123456"
             }

def locked_user(name):#检查用户是否锁定
    f = open("locked_user.txt", "r+")
    for i in f:
        if name == i.strip():
            print("Sorry,you are locked")
            exit()
    f.close()

def add_locked_user(name): #将用户加入锁定列表
    add_name = "%s%s"%("\n",name)
    f = open("locked_user.txt", "a")
    f.write(add_name)
    f.close()

def input_name():  #用户名输入,空用户和不在用户列表的用户重新输入,正确用户进入密码界面
    while True:
        user_name = input("Please input name:")
        if len(user_name) == 0:
            continue
        if user_name == 'q':
            exit()
        locked_user(user_name)
        if user_name in user_dict.keys():
            inspect_pwd(user_name)
        else:
            continue

def inspect_pwd(name):  #检查用户密码,重试三次锁定
    retry_count = 0
    while retry_count < 3:
        user_pwd = input("Please input pwd:")
        print(type(user_pwd))
        if user_pwd == user_dict[name]:
            print("Welcome")
        else:
            print("pwd failed")
        retry_count += 1
    else:
        add_locked_user(name)




if __name__ == "__main__":
    input_name()
