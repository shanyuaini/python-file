menu ={
    'Beijing':{
        "ChaoYang":{
            'CBD' : ['CICC','CCTV'],
            'JinRongJie':[''],
            'Wangjing' :['momo','chuizi']
        },
        "HaiDian" :['BaiDu','YouKu']
    },
    'ShangHai':{
        "PuDong":['Ctrip','1 shop'],
        "PuXI" :['China Bank','America Bank']
    }
}
'''
for k,v in menu.items():
    print k,v
'''

exit_flag = False
while not exit_flag:
    for index,key in enumerate(menu.keys()):
        print index,key
    choice_1 = raw_input("city choice").strip()
    if choice_1.isdigit():
        choice_1 = int(choice_1)
        key_1 = menu.keys()[choice_1]
        print key_1
        while not exit_flag:
            for index,key in enumerate(menu[key_1]):
                print '-->',index,key

            choice_2 = raw_input("city choice").strip()
            if choice_2.isdigit():
                choice_2 = int(choice_2)
                key_2 = menu[key_1].keys()[choice_2]
                while not exit_flag:
                    for index,key in enumerate(menu[key_1][key_2]):
                        print '-->-->',index,key

                    choice_3 = raw_input("city choice").strip()
                    if choice_3.isdigit():
                        print "this is the last level..."
                    elif choice_3 == 'quit':
                        exit_flag = True
                    elif choice_3 == 'back':
                        break
else:
    print "===going to quit"
