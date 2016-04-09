#_*_coding:utf-8_*_
#作业1购物车 ,  作业2 信息查询表,根据输入的关键字模糊查询,并统计一共查到多少条信息
import sys,os
'''
def shop_list():#读取购物菜单
    filename = 'shopping.txt'
    f = file('shopping.txt','rb')
    menu = []
    for line in f.xreadlines():
        line = line.strip().split()
        menu.append(line)
#    for key in menu:
 #        menu.index(key),menu[menu.index(key)]
    return menu
    #print menu,type(menu)

def price_judge(choice_goods,menu):
    if choice_goods in menu.has_key():
        pass

while True:

    salary = raw_input("请输入你的工资:").strip()
    if len(salary) == 0:
        continue

    menu = shop_list()

    for key in menu:
        print menu.index(key),menu[menu.index(key)]
    print menu
    while True:
        choice = raw_input("请选择你要购买的物品,输入q退出:")

        if len(choice) != 0:
            choice = int(choice)

        for i in menu:
            if choice == menu.index(i):
                break
        else:
            continue


            print choice





'''




'''
salary =raw_input("请输入你的工资:")
while True :
'''
