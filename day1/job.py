import os
#_*_coding:utf-8_*_
#first version
'''
pwd_menu = { #account list ant count
    'alex' : ['123456',0],
    'tom' : ['1234567',0],
    'jerry' : ['12345678',0],
    'sylar' : ['123456789',0]
}
logon_count = 0
logon_flag = False
lock_user = []
file_name = r'E:/\python-file/\day1/\lock_list.txt'#choose file

if os.path.exists(file_name) :#read lock file
    lock_read = file(file_name,'r').read('')
    if lock_read.strip():
        lock_user = lock_read.split()
    print lock_user
for name_count in range(3):

    user_name =raw_input("Please input you username:").strip()
    if len(user_name) == 0:
        continue
    if user_name in lock_user:#username locked
        print "You are locked"
        break
    if pwd_menu.has_key(user_name):
        for pwd_count in range(3):
            user_pwd = str(raw_input("Please input you passwd:").strip())#pwd
            logon_count += 1
            if len(user_pwd) == 0:
                continue
            if user_pwd == str(pwd_menu[user_name][0]):
                #while True:
                user_cmd=raw_input( "Welcome logon! Doing something!,input 'q' exit").strip()
                if user_cmd == 'q':
                    logon_flag = True
                break

    if logon_flag:
        print "Logout,See you next time!"
        break
    if int(logon_count) == 3:
        print "Lock this user!"
        if user_name in lock_user:
            break
        else:
            lock_user.append(user_name)
            print lock_user
            lock_file = open(file_name,'w')
            lock_file.writelines(lock_user)
            lock_file.close()
            break
'''
#second version
pwd_menu ={
    'name' : ['alex','tom','jerry','sylar'],
    'passwd' : ['123456','1234567','12345678','123456789']
}
file_name = r'E:/\python-file/\day1/\lock_list.txt'
lock_user = []
lock_count = 0
quit_flag = False

#读取被锁定用户文件,加载到锁定用户列表里

if os.path.exists(file_name):
    f = file(file_name)
    for line in f.readlines():
        line = line.strip()   #取消文件中的空格和回车
        line = line.split('\n')    #将字符改为列表
        lock_user.extend(line)      #这里使用组合两个列表
    f.close()


for input_count in range(3):
    input_name = raw_input("Please input you name: ").strip()
    if len(input_name) == 0:
        continue
    if input_name in lock_user:
        print "You account is locked"
        break
    else:#帐号不为空并没锁定就比对用户名
        if input_name in pwd_menu['name']:

            index = pwd_menu['name'].index(input_name) #取得用户名索引号
            for pwd_count in range(3):
                input_pwd = raw_input("Please enter you pwd :").strip()
                lock_count += 1
                if input_pwd == pwd_menu['passwd'][index]:
                    logon_user = raw_input( "Welcome logon in!\nInput 'q' quit:  ")
                    if logon_user == 'q':
                        quit_flag =True
                        break
    if quit_flag == True:#做输入用户名这里的退出标记
        break
    if lock_count >= 3: #如果密码输错3次,进行锁定用户
        if input_name in lock_user:
            break
        else:
            lock_user.append(input_name)
            print lock_user
            f = file(file_name,'w')
            for i in lock_user:
                f.write(i)
                f.write("\n") #使用换行给用户名做隔断
                print i
            f.close()
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









