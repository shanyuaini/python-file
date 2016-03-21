import os
pwd_menu = { #account list ant count
    'name' : ['alex','tom','jerry','sylar'],
    'pwd' : ['123456','1234567','12345678','123456789'],
    'count' : ['0','0','0','0']
}
print pwd_menu
user_list = pwd_menu['name']
logon_count = pwd_menu['count']
print logon_count

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









