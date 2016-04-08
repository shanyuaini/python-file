#_*_coding:utf-8_*_
#用户登录程序
import sys
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit:
    username = raw_input('\033[32;1mUsername:\033[0m')
    lock_check = file(lock_file)
    #当用户输入用户名后打开lock文件,检查此用户是否已经锁定
    for line in lock_check.readlines():
        line = line.split()
        if username == line[0]:
            sys.exit('\033[31;1m User %s is locked !\033[0m'%username)#跳出程序

    password = raw_input('\033[32;1mPassword:\033[0m')
    f = file(account_file,'rb')
    match_flag = False
    for line in f.readlines():
        user,passwd = line.strip('\n').split()
        #print user ,passwd
        if username == user and password == passwd:
            print 'Match',username
            match_flag = True  #把标记改为True,然后跳出.
            break  #这个只是跳出这个for循环
    f.close()
    if match_flag == False:#没有匹配到就将count+1
        print "User unmatched"
        retry_count+=1
    else:
        print "Welcome login"
else:#当while循环不满足.就执行这里,如果在while中用break跳出就退出程序了.可能会造成没有写锁文件
    print 'You account is locked'
    f = file(lock_file,'ab')
    f.write(username+'\n')
    f.close()
