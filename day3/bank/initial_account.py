#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
account_dict = {"62221":["123456",0,15000,7500],
                "62222":["123456",0,15000,7500],
                "62223":["123456",0,15000,7500]
                }  #定义账户信息字典，key为银行卡号，values[0]为密码，values[1]密码错误记录数，values[2]为余额，values[3]为取现金额上限

def write_account(account_dict,file_txt = "account.txt"):  #更新库文件内容的函数
    with file(file_txt,"w") as f:
        pickle.dump(account_dict,f)

if __name__ == '__main__':
    write_account(account_dict)

