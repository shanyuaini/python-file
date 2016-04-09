#_*_coding:utf-8_*_
#作业1购物车 ,  作业2 信息查询表,根据输入的关键字模糊查询,并高亮显示并统计一共查到多少条信息
import sys,os
#首先让用户输入关键字,
def Break_Flag():
    while True:
        break_flag = raw_input('''是否继续(y/n):''')
        if break_flag == 'y' or break_flag == 'n':
            return break_flag
        else:
            print '''\t\t输入错误,请重新输入'''



filename = 'shopping.txt'
f = file(filename,'rb')
search_list = f.readlines()


break_flag = ''
while break_flag != 'n':
    while True:
        choice_word = raw_input("请输入你需要查询的物品:")
        if len(choice_word) >  0:
            break
        else:
            print "查询内容不能为空"
    search_count = 0
    searched_list = []
    print search_list
    for i in search_list:
        if i.count(choice_word) > 0:
            searched_list.append(i.replace(choice_word,'\033[31;42;1m%s\033[0m'%choice_word))
            search_count += 1
    if search_count > 0:
        for i in searched_list:
            print i
        print '''共查询到%s条信息''' % search_count
        break_flag = Break_Flag()
        print search_list
    else:
        print '没有找到你要查找的信息'
f.close()




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
