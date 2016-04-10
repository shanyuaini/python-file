#!/usr/bin/env python
#coding:utf-8
__author__ = 'silence'
import time,sys
import GameControl
user = GameControl.UserOperate()
role = GameControl.RoleOperate()
menu_list1 = [u"注册账号",u"登录游戏",u"退出游戏"]
menu_list2 = [u"创建角色",u"选择角色",u"删除角色",u"退出游戏"]
menu_list3 = {"1":u"新的征程",'2':u"载入旧档"}

#菜单列表
def menu_list(menu):
    print '+++++++++++++++++'
    for index,p in enumerate(menu):
        print "|",index,p,"\t|"
    print '+++++++++++++++++'

#字典列表
def menu_dic(dic):
    print '+++++++++++++++++'
    for k,v in sorted(dic.items(),key = lambda x:x[0]):
        print "|",k,v,"\t|"
    print '+++++++++++++++++'

#游戏背景
def login_info():
    login_info = u'''
    John and Liz 是高中同学时的恋人,后来Liz考上
了北京城市学院,Jhon没有,为了跟女朋友在一起,他来到了
北京打工（一家网吧当网管），挣钱为Liz交学费,后来LIZ
毕业后工作了,遇到了公司的高富帅peter,然后两人就苟且
在了一起,JHON发现后非常伤心,发誓要把LIZ夺回来,然后
他发粪学习,增加自身能力，参加自考,学习老男孩PYTHON，
若干年后,当上了某大型互联网公司的IT总监,月薪5万，北
京买了车和房,偶然又见到了LIZ,此时她已被高富PETER甩
了,LIZ提出再回到JHON身边时,JHONE优雅的说...'''
    for i in login_info:
        print i+"",
        time.sleep(0.05)
    print ""

#角色删除
def role_del(login_name):
    role_name_list = role.role_list(login_name)
    if len(role_name_list) >0:
        while True:
            role.show_role(role_name_list)
            role_del_choice = raw_input(u"请输入要删除的角色名(exit返回):").strip()
            if role_del_choice == "exit":
                print u"正在返回上一级...."
                break
            elif role_del_choice in role_name_list:
                role_del_status = role.del_role(login_name,role_del_choice)
                if role_del_status:
                    print u"删除角色%s成功" %role_del_choice
                    break
                else:
                    print u"删除角色%s失败" %role_del_choice
                    break
            else:
                print u"角色名不存在..."
    else:
        print u"您当前没有角色..."

#载入选择
def role_login_choice(login_name,role_name_input):
    while True:
        menu_dic(menu_list3)
        load_choice = raw_input(u"请输入编号选择如何进入游戏(exit退出游戏):")
        if load_choice == "1":
            print u"新的征程..."
            role_info = role.reload_role(login_name,role_name_input)
            role_info[-1] = 1000
            role_info[-2] = 1
            role_info[-3] = 1000
            role_info[1] = 20
            role_info[3] = u"单身汉一个"
            role_info[4] = u"无业游民"
            return role_info
        elif load_choice == "2":
            print u"载入存档..."
            role_info = role.reload_role(login_name,role_name_input)
            return role_info
        elif load_choice == "exit":
            print u"正在退出..."
            time.sleep(0.75)
            sys.exit()
        else:
            print u"选择错误"
            continue

#载入模块
def role_load(login_name):
    role_name_list = role.role_list(login_name)
    if len(role_name_list) >0:
        while True:
            role.show_role(role_name_list)
            role_name_input = raw_input(u"请输入可选的角色名:").strip()
            if role_name_input in role_name_list:
                role_info = role_login_choice(login_name,role_name_input)
                return role_info
            else:
                print u"角色名输入有误,别闹...."
    else:
        print u"您还没有创建游戏角色,请先创建角色....."

#载入角色选择
def role_op(login_name):
    while True:
        menu_list(menu_list2)
        menu_choice2 = raw_input(u"请输入序号选择操作:").strip()
        if menu_choice2 == "0":
            print u"创建角色"
            role_add_status = role.add_role(login_name)
            if role_add_status:
                print u"创建角色成功..."
            else:
                print u"创建角色失败..."
        elif menu_choice2 == "1":
            print u"选择角色"
            role_info = role_load(login_name)
            return login_name,role_info
        elif menu_choice2 == "2":
            print u"删除角色"
            role_del(login_name)
        elif menu_choice2 == "3":
            print u"退出游戏"
            sys.exit()
        else:
            print u"输入错误"

#角色流程
def login_user():
    login_name = user.login_control()
    if login_name != None:
        role_info = role_op(login_name)
        return role_info

#登录流程
def login_game():
    print u"\033[32;1m游戏背景:\033[0m"
    login_info()
    print u"\033[31;1m免责声明：\n欢迎来到模拟人生游戏平台,请遵守游戏规则,\n未成年人请在成年人的监护下进行游戏...\033[0m"
    begin_game = raw_input(u"请按回车键开始游戏....")
    print u"\033[32;1m开始游戏,请等待系统载入....\033[0m"
    time.sleep(0.75)
    while True:
        menu_list(menu_list1)
        menu_choice1 = raw_input(u"请输入序号选择操作:").strip()
        if menu_choice1 == "0":
            print u"正在注册账号....."
            user.add_user()
        elif menu_choice1 == "1":
            print u"正在登录游戏...."
            #user = GameControl.UserOperate()
            role_info_1 = login_user()
            while True:
                if role_info_1[1] == None:
                    role_info_1 = role_op(role_info_1[0])
                else:
                    return role_info_1
        elif menu_choice1 == "2":
            print u"退出游戏"
            sys.exit()
        else:
            print u"输入错误"

if __name__ == "__main__":
    while True:
        login_info = login_game()
        if login_info[1] != None:
            if login_info[1][1] > 0:
                scene = GameControl.GameScene(login_info[0],login_info[1])
                scene.game_main()
            else:
                print u"你选择的角色在游戏中自杀,请换一个角色登录..."

