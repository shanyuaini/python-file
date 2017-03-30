#_*_coding:utf-8_*_
'''
num = input('需要查找的数字:') #循环一个序列,找到需要的数字
count = 0
while count < 10000:

    if count == num:
        print "count: ",count
        choice = raw_input("是否继续循环?(y/n)")
        if choice == 'n':
            break
        elif choice == 'y':
            num = input('重新输入需要查找的数:')
            while num < count:
                num = input('循环已经过了请重新输入:')
            continue
        else:
            continue
    else:
        print "当前count",count
    count += 1
'''
import sys
num = 0
count = 0
while count < 9999:

    print "当前count",count
    if count == num:
        num = input('需要查找的数字:')
        while num < count:
            choice = raw_input("是否继续循环?(y/n)")
            if choice == 'n':
                sys.exit()
            else:
                num = input('循环已经过了请重新输入:')
    else:
        print "当前count",count
        count += 1










'''
import sys
count = 0
while True:
    print_num = input('选择你要暂停的行:')
    while count < 9999:
        if print_num <= count:
            if print_num == count:
                print "当前行为第%s行"%count
                choice = raw_input('是否需要继续(y/n):')
                if choice == 'n':
                    sys.exit()
                else:
                    break
            else:
                if print_num < count:
                    print "已经过了"
            break
        else:
            count += 1
            print "当前行为第%s行"%count

'''
