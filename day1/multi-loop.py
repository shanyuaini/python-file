"""
passwd = "test"
for i in range(3):
    user_pwd = raw_input("Please input you passwd:").strip()
    if len(user_pwd) == 0:
        continue
    if user_pwd == passwd:
        while True:
            print "Welcome login!"
            user_choice = raw_input('''
            1,run a cmd!
            2,send a file
            3,exit the level
            4,kill the program
            ''').strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print "run a cmd!"
            if user_choice == 2:
                print "send a file"
            if user_choice == 3:
                print "jump this level!"
                break
        if user_choice == 4:
            print "going to logout!"
            break
        #break  #zhege difang bu neng  break,yingwei haihui zhixing  , mohu de tiao chu.
    print "going to something"
"""
"""
passwd = "test"
logout_flag = Flase
for i in range(3):
    user_pwd = raw_input("Please input you passwd:").strip()
    if len(user_pwd) == 0:
        continue
    if user_pwd == passwd:
        while True:
            print "Welcome login!"
            user_choice = raw_input('''
            1,run a cmd!
            2,send a file
            3,exit the level
            4,kill the program
            ''').strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print "run a cmd!"
            if user_choice == 2:
                print "send a file"
            if user_choice == 3:
                print "jump this level!"
                break
            if user_choice == 4:
                logout_flag = True
                break
    if logout_flag:   #tiaochu for xunhuan
        print "going to logout!"
        break

    print "going to something"
"""

"""
passwd = "test"
logout_flag = False
for i in range(3):
    user_pwd = raw_input("Please input you passwd:").strip()
    if len(user_pwd) == 0:
        continue
    if user_pwd == passwd:
        while True:
            print "Welcome login"
            user_choice = raw_input('''
            1,run a cmd
            2,send a file
            3,re-enter passwd
            4,exit
            ''').strip()
            if user_choice == 1:
                print "going to run a cmd!"
            if user_choice == 2:
                print "going to send a file!"
            if user_choice == 3:
                print "Please choice other passwd"
                break
            if user_choice == 4:
                logout_flag = True
                break
    if logout_flag:
        print "Logout,see you next time!"
        break
    print "let us doing some thing!"
"""
name_list = ["alex","eric","jack"]
print name_list
name_list.insert(2,"sylar")
print name_list
name_list.append("tom")
print name_list
name_list.append("rain")
print name_list
print name_list[1:4]
print name_list[-1]
print name_list[-3:]
print name_list[:4]
name_list[1] = "Eric"
name_list2 = ["alex","eric","jack"]
name_list.extend(name_list2)
print name_list
print name_list.count("alex")
name_list.sort()
print name_list
name_list.reverse()
print name_list

for i in range(name_list.count("alex")):name_list.remove("alex")
print name_list


































































