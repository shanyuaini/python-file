#_*_coding:utf-8_*_
#


'''
购物车程序,要求用列表完成
1,要求用户输入一个工资,然后打印购物菜单
2,用户可以不断的购买商品,知道钱不够为止
3,退出时,格式化打印用户购买的商品和余额
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
        p_price = products[choice][1]
        if  salary >= p_price:
            shop_list.append(products[choice])
            salary -= p_price
            print "Has added\033[31;1m %s\033[0m into shop_list,your current balance is \033[31;1m%s\033[0m"%(products[choice][0],salary)
        else:
            print "money is not enough,try something else"
    elif choice =='quit':
        print '--------shopping list---------------'
        for k,v in enumerate(shop_list):
            print k,v
        print "your current balance is \033[31;1m %s\033[0m"%(salary)
        break


            #print '''你已购买了一个%s 单价%s元,剩余%s!'''%(v,menu[v],balance)


