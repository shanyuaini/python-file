#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 13:29
# @Author  : sylar
# @Site    : 
# @File    : day2_shopping.py
# @Software: PyCharm
'''
一个简单的商品购买流程,以及购物车
思路:
1,管理员登录后可以操作选择1添加商品,2修改商品,3删除商品,4,设置用户,5用户总金额
2,用户登录后展示商品列表,输入1,2,3,4...选择商品.
3,默认将用户购买的物品存入购物车,当购物车总价超过用户可用金额,禁止购买
4,用户输入q退出,并付账,.
'''
import os

#写文件
def file_up(file,data,mod='a'):
    f = open(file,mod)
    f.write(data)
    f.close()
#读文件
def file_read(file):
    f = open(file,'r')
    data = f.readlines()
    return data



# 增加商品信息,一种用字典,一种让管理员输入
def add_comm():
    # shop_dict = {
    #     "Bike" : "2500",
    #     "Caffe": "50",
    #     "Iphone" : "5000",
    #     "Mac" : "14000",
    #     "Tea" : "20",
    #     "Cup" : "400"
    # }
    # for k,v in enumerate(shop_dict,1):
    #     file = "shop_list.txt"
    #     data = '%s %s\n'%(v,shop_dict[v])
    #     file_up(file,data)
    while True:
        comm_goods = input("Setting comm_goods's name:").strip()
        if comm_goods == 'q':
            break
        else:
            price = input("Setting comm_goods's price:").strip()
        file = "shop_list.txt"
        data = '%s %s\n'%(comm_goods,price)
        file_up(file, data)
#add_comm()

def display_item(data):
    for k,item in enumerate(data,1):
        print(k, item, data[item])
#display_item(comm_list())

def comm_list(): #读取商品列表
    f = file_read("shop_list.txt")
    item_list = dict()
    for line in f:
        line = line.strip()
        comm_goods,price = line.split(" ")
        item_list[comm_goods] = price
    return (item_list)
#comm_list()





def update_price(data):# 这里用迭代器处理更好,过两天仔细看下迭代器再来修改
    while True:
        old_file = "shop_list.txt"
        new_file = "shop_list.txt.bak"
        tmp_file = "new_price_list.txt"
        display_item(data)
        change_comm = input("Please input change goods :")
        if change_comm == 'q':
            break
        if len(change_comm) == 0:
            continue
        for k,v in enumerate(data,1):
            if int(change_comm) == k:
                new_price =input("Please input new price:")
                new_data = '%s %s\n' % (v, new_price)
                file_up(tmp_file, new_data)
               # print(data)
            else:
                new_data = '%s %s\n' % (v, data[v])
                file_up(tmp_file, new_data)
        if new_file in os.listdir('./'):
            os.remove(new_file)
        else:
            pass
        os.rename(old_file,new_file)
        os.rename(tmp_file,old_file)
# update_price(comm_list())

# def del_comm















