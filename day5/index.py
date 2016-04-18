#_*_coding:utf-8 _*_
__author__ = 'sylar'


from day5.model.admin import Admin

def main():
    user =raw_input('username:')
    pwd = raw_input('passwd:')
    admin = Admin()
    result = admin.check_validate(user,pwd)  #用户输入的用户名密码传入model.admin.py
    if not result:  #因为没有查找到返回的是none,就是否
        print '用户名密码错误'
    else:  #查找到了
        print '登录成功'



if __name__ == '__main__':
    main()