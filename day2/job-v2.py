#_*_coding:utf-8 _*_
__author__ = 'sylar'
#作业1购物车 ,  作业2 信息查询表,根据输入的关键字模糊查询,并统计一共查到多少条信息

def shop_list():#读取购物菜单
    filename = 'shopping.txt'
    f = file('shopping.txt','rb')
    menu = []
    for line in f.xreadlines():
        line = line.strip().split()
        menu.append(line)
    for key in menu:
        print menu.index(key), menu[menu.index(key)]
    return menu

def salary():
    while True:
        salary = raw_input("请输入你的工资:").strip()
        if len(salary) == 0:
            continue
        salary = int(salary)
        return salary

def choice_judge():
    choice_flag = False
    while choice_flag is False:
        choice = raw_input("请选择你要购买的物品,输入q退出:")
        if choice == 'q':
            return choice
        if len(choice) != 0:
            choice = int(choice)
        for i in menu:     #检查choice是否在别表的index中存在
            if choice == menu.index(i):
                choice_flag = True
                return choice

def price(salary,choice,menu):   #买一次返回一个余额
    if salary >= int(menu[choice][1]):
        balance = salary - int(menu[choice][1])
        # price(balance,choice,menu)
        print '''
        你购买了一个%s,
        花费%s元
        余额为%s元 ''' % (menu[choice][0], menu[choice][1], balance)
        return balance
    else:
        print "你的余额不足,请重新选择"
        return salary


balance = salary()
shopping_list = []
while True:

    menu = shop_list()
    choice = choice_judge()
    if choice == 'q':
        print shopping_list
        break
    balance = price(balance,choice,menu)
    shopping_list.append(menu[choice])
    print balance, shopping_list





























