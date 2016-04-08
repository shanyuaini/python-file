#! /usr/bin/env python
# -*- coding: utf-8 -*-
from initial_account import *  #导入初始化账号信息模块
import pickle
import re
import time

def read_account():  #从文件中读出预存的账号信息
    with file("account.txt") as f:
        account_dict = pickle.load(f)
    return account_dict

def input_user(account_dict):  #输入银行卡号的函数
    while True:
        username = raw_input("请输入银行卡号：").strip()
        if username  not in account_dict:  #判断卡号是否存在
            print "\033[31;2m请输入正确银行卡号：\033[0m"
            continue
        else:
            return username

def check_pwd(account_dict,username):  #输入并检测密码的函数
    login_flag = False
    error_count = account_dict[username][1]  #读出字典中密码错误记录数
    while True:
        password = raw_input("请输入银行卡密码：").strip()
        if len(password) == 0:
            print "密码不能为空！"
            continue
        if password != account_dict[username][0]:
            error_count += 1
            write_lock(account_dict,username,error_count)  #写入错误记录函数
            if error_count == 3:
                print "\033[31;2m你的账号已被锁定！\033[0m"
                break
            print "密码错误，请重新输入！还有%d次机会"%(3 - error_count)
            continue
        else:
            print "\033[32;1m登录成功！\033[0m"
            error_count = 0
            write_lock(account_dict,username,error_count)  #清除错误记录
            login_flag = True
            return login_flag

def check_lock():  #检查锁记录函数
    if account_dict[username][1] == 3:
        print "\033[31;1m你的账号已被锁定！\033[0m"
    else:
        pass

def write_lock(account_dict,username,error_count):  #写入错误记录累加数
    account_dict[username][1] = error_count
    write_account(account_dict) #调用initial_account模块函数，将当前字典状态写入文件

def balance_query(username,choice = "1"): #查询余额函数
    balance = account_dict[username][2]  #余额变量
    cash = account_dict[username][3]  #可取现金变量
    interest = "%5" #利息为5%
    if choice == "1":
        print "你本月余额为\033[34;2m%d\033[0m。(可取现\033[34;2m%d\033[0m，利息\033[33;2m%s\033[0m)" %(balance,cash,interest)
        time.sleep(1)
    return balance,cash

def draw_money(): #取款
    choice_money = [100,200,500,1000,2000,3000]
    while True:
        print "请输入取款金额('0'退出)："
        for i in choice_money:
            print i
        input_money = raw_input("--->").strip()
        if input_money == "0":
            break
        elif input_money.isdigit() == False or int(input_money) not in choice_money:  #判断取款金额是否合法
            print "\033[31;2m请输入正确取款金额！\033[0m"
        else:
            balance,cash = balance_query(username,choice)  #调用查询余额函数
            balance = balance - int(input_money)*1.05  #扣款和利息
            cash = cash - int(input_money)  #更新取现额度
            if balance > 0 and cash > 0:
                account_dict[username][2] -= int(input_money)*1.05  #余额应为当前余额减去取款金额加利息
                account_dict[username][3] -= int(input_money)  #取现额度减少
                write_account(account_dict)  #将变更信息写入文件
                print "\033[32;1m取款成功！\033[0m"
                time.sleep(2)
                trade_detail(username,"取现",str(-int(input_money)),str(int(input_money)*0.05),balance,0)  #调用交易明细函数，将交易明细写入文件
            elif balance <= 0:
                print "\033[31;2m你的余额不足！\033[0m"
            elif cash < 0:
                print "\033[31;2m取现额度超过上限！\033[0m"
            balance_query(username)  #显示取款操作后的余额信息

def transfer_accounts(): #转账
    while True:
        another_username = input_user(account_dict)  #调用输入用户名函数
        if another_username == username:
            print "\033[31;2m不能对自己转账！\033[0m"
            continue
        confirm_username = raw_input("请再次输入对方银行卡号：")
        if another_username != confirm_username:
            print "\033[31;2m两次输入的银行卡号不一致！\033[0m"
        else:
            while True:
                transfer_fee = raw_input("请输入转账金额('0'退出)：")
                if transfer_fee.isdigit() == False:
                    print "\033[31;2m请输入数字！\033[0m"
                    continue
                else:
                    break
            if transfer_fee == "0":  #转账金额输入0则退出
                break
            balance,cash = balance_query(username,choice)  #调用查询余额函数
            if int(transfer_fee) > balance:
                print "\033[31;2m你的余额不足！\033[0m"
                break
            else:
                account_dict[username][2] -= int(transfer_fee)  #当前余额扣除转账金额
                account_dict[another_username][2] += int(transfer_fee)  #对方账户当前余额加上转账金额
                write_account(account_dict)  #记录到文件
                print "\033[32;1m转账成功！\033[0m"
                time.sleep(2)
                trade_detail(username,"转出",str(-int(transfer_fee)),"0",account_dict[username][2],0)  #记录转出明细
                trade_detail(another_username,"转入",transfer_fee,"0",account_dict[another_username][2],0)  #记录对方转入明细
                balance_query(username)
                break
def repay(account_dict,username):  #还款
    balance = account_dict[username][2]
    repay_money = 15000 - balance
    if repay_money == 0:
        print "\033[31;2m你本月无需还款\033[0m"
    else:
        while True:
            input_money = raw_input("你本月支出\033[31;2m%d\033[0m元，请输入还款金额:"%repay_money).strip()
            if input_money.isdigit() == False:
                print "\033[31;2m请输入数字\033[0m"
                continue
            input_money = int(input_money)
            if input_money == 0:
                break
            if input_money > repay_money:
                print "\033[31;2m请输入正确金额\033[0m"
                continue
            balance += input_money
            account_dict[username][2] = balance  #更新余额
            write_account(account_dict)
            trade_detail(username,"还款",str(input_money),"0",balance,0)  #记录
            print "\033[32;1m还款成功！\033[0m"
            time.sleep(1.5)
            if balance == 15000:
                print "\033[32;1m你本月账单已还清！\033[0m"
                time.sleep(2)
            break

def bill():  #账单
        bill_dict = {}
        bill_date = time.strftime("%Y-%m-%d")
        '''if "-30" not in bill_date:  #判断是否为30号，暂时屏蔽
            print "\033[31;2m本期账单未生成\033[0m"
        else:'''
        re_date = re.search("\d+\-\d*\-",bill_date).group()  #匹配到当前月份
        f = file("trade_detail.txt")  #读取交易明细文件
        for i in  f.readlines():
            if re_date in i and username in i:  #取当前月份及当前账户
                bill_dict.setdefault(i.split()[3],[[],[]])[0].append(int(i.split()[4]))  #以交易类型作为key，将交易金额作为values的第一个列表元素
                bill_dict.setdefault(i.split()[3],[[],[]])[1].append(float(i.split()[5]))  #以交易类型作为key，将利息作为values的第二个列表元素
        print "您本月账单如下："
        print re_date[:-1]  #打印年-月
        print "%-12s%12s%13s"%("交易类型","金额","利息")
        for i in bill_dict:
            print "%-12s%8s%11s"%(i,reduce(lambda x,y:x+y,bill_dict[i][0]),reduce(lambda x,y:x+y,bill_dict[i][1]))  #会总各交易类型金额和利息并打印
        balance = account_dict[username][2]
        if balance < 15000:
            choice = raw_input("您本月还需还款\033[31;2m%d\033[0m元，是否还款？(y)"%(15000 - balance))
            if choice == "y":
                repay(account_dict,username)  #调用还款函数
        else:
            print "\033[32;1m您本月账单已清\033[0m"
            time.sleep(2)

def trade_detail(username,tran_type = "",amount = "",interest = "",balance = "",flag = 1):#交易明细函数，flag为0时为记录，flag为1时为读取
    with file("trade_detail.txt","a") as f:
        if flag == 0:
            f.write('%-8s %10s %8s %8s %6s %3s %7s\n'%(username,time.strftime('%Y-%m-%d'),time.strftime('%H:%M:%S'),tran_type,amount,interest,balance))
        else:
            print '%s %s %s %s %s %s %s\n'%('卡号','日期','时间','交易类型','金额','利息','余额')
            with file("trade_detail.txt") as f:
                for line in f.xreadlines():
                    if username in line:
                        print line
            raw_input("按任意键返回")

def login_bank():  #封装登录
    account_dict = read_account()
    username = input_user(account_dict)
    if account_dict[username][1] == 3:
        print "\033[31;2m你的账号已被锁定！\033[0m"
    else:
        login_flag = check_pwd(account_dict,username)
    return account_dict,username,login_flag

def shopping_interface(pay):  #网购支付接口
    payment_flag = False  #支付标志位
    account_dict,username,login_flag = login_bank()
    choice = raw_input("确定支付\33[31;2m%d\033[0m元？(y)"%pay)
    if choice == 'y':
        balance,cash = balance_query(username,"")
        if balance >= pay:
            balance -= pay
            account_dict[username][2] = balance
            write_account(account_dict)
            trade_detail(username,"购物",str(-pay),"0",balance,0)
            print "\033[32;1m支付成功！\033[0m"
            time.sleep(2)
            payment_flag = True
        else:
            print "\033[31;2m你银行卡中的余额不足！\033[0m"
    return payment_flag

if __name__ == '__main__':
    print "******************欢迎进入银行系统*********************"
    account_dict,username,login_flag = login_bank()
    if login_flag:
        while True:
            print "******************请选择操作菜单******************"
            print '1.查询\n2.取现\n3.转账\n4.还款\n5.明细\n6.账单\n0.退出'
            choice = raw_input("--->")
            if choice == "0":
                break
            elif choice == "1":
                balance_query(username,choice)
            elif choice == "2":
                draw_money()
            elif choice == "3":
                transfer_accounts()
            elif choice == "4":
                repay(account_dict,username)
            elif choice == "5":
                trade_detail(username)
            elif choice == "6":
                bill()