#_*_coding:utf-8_*_

'''练习
购物车程序,要求用列表完成
1,要求用户输入一个工资,然后打印购物菜单
2,用户可以不断的购买商品,直到钱不够为止
3,退出时,格式化打印用户购买的商品和余额
'''
'''实现方法
1,先让用户输入工资,然后展示所有物品
2,用户选择物品后取得单价和工资判断,单价不高于工资就进入购买

'''


products = [['apple',5000],['ipad',3000],['bike',2000],['tea',50],['cup',400],['phone',1200]]
salary = int(raw_input("Please input you salary: "))
shop_list = []
while True:
    for index,p in enumerate(products):
        print index,p[0],p[1]
    choice = raw_input("Buy something: ")
    if choice.isdigit():
        choice = int(choice)
        p_price = products[choice][1]#给单价变量复制products 的第choice个列表的 的第2位,因为每个小列表第二位都是单价
        if  salary >= p_price:#判断薪水是否大于等于物品单价,因为每个单价都不一样,所以先取单价再做判断
            shop_list.append(products[choice])#将每个物品都是小列表,直接将列表追加到购物车,名称和单价都加进去了
            salary -= p_price
            print "Has added\033[31;1m %s\033[0m into shop_list,your current balance is \033[31;1m%s\033[0m"%(products[choice][0],salary)
        else:
            print "money is not enough,try something else"
    elif choice =='quit':#如果用户选择退出,就是用轮询购物车列表打印所有物品
        print '--------shopping list---------------'
        for k,v in enumerate(shop_list):
            print k,v
        print "your current balance is \033[31;1m %s\033[0m"%(salary)
        break


        #print '''你已购买了一个%s 单价%s元,剩余%s!'''%(v,menu[v],balance)


