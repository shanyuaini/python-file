import os
pwd_menu = { #account list ant count
    'alex' : ['123456',0],
    'tom' : ['1234567',0],
    'jerry' : ['12345678',0],
    'sylar' : ['123456789',0]
}
print pwd_menu
logon_flag = False
lock_user = []
file_name = r'E:/\python-file/\day1/\lock_list.txt'#choose file
if os.path.exists(file_name) == True:
    lock_read = file(file_name,'r').read()
    lock_user = lock_read.split()
    print lock_user
for name_count in range(3):
    user_name =raw_input("Please input you username:").strip()
    if len(user_name) == 0:
        continue
    if user_name in lock_user:#username locked
        print "You is locked"
        logon_flag = True
        break
    if pwd_menu.has_key(user_name):
        logon_count = int(pwd_menu[user_name][1])
        print logon_count
        for pwd_count in range(3):
            user_pwd = str(raw_input("Please input you passwd:").strip())
            print type(user_pwd)
            logon_count += 1
            print logon_count
            if len(user_pwd) == 0:
                continue
            if user_pwd == str(pwd_menu[user_name][0]):
                #while True:
                print "Welcome logon"

                '''else:
                    logon_flag = True
                    break'''
    if logon_flag:
        print "Logout,see you next time!"
        break
    if int(logon_count) == 3:
        print "Lock this user!"
        lock_user.append(user_name)
        lock_file = open(file_name,'w')
        lock_file.write(repr(lock_user))
        lock_file.close()
        print lock_user
        break





'''
file_name = r'E:/\python-file/\day1/\logon_pwd.txt'#choose file
if os.path.exists(file_name) == False:#file not exist,writ count
    logon_count = open(file_name,'w')
    logon_count.write(str(logon_count))
    logon_count.close()
    print logon_count
else:#file exist, read count
    logon_count = file(file_name,'r').read()
    pwd_menu['count'] = logon_count


for logon_count in range(3):
    user_name =raw_input("Please input you username:").strip()
    if len(user_name) == 0:
        continue
    if user_name in user_list:
        user_count = user_list.index(user_name)####get user_count

'''




'''

for logon_count in range(3):
    user_name = raw_input("Please input you username:").strip()
    user_name = str(user_name)
    print user_name
    if len(user_name) == 0:
        continue
    for user_name in pwd_menu['name']:
        user_pwd = raw_input("Please input you passwd:").strip()
        if len(user_pwd) == 0:
            user_pwd = raw_input("Please input you passwd:").strip()
            continue



    else:
        print "Not found this name!try again"

'''









