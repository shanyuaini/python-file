#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 12:38
# @Author  : sylar
# @Site    : 
# @File    : day1_homework.py
# @Software: PyCharm

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
