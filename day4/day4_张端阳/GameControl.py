#!/usr/bin/env python
#coding:utf-8
__author__ = 'silence'
import pickle,os,time,sys

#角色属性类
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lv = 1
        self.salary = 1000
        self.assets = 1000
        self.gril_friend = u"单身汉一个"
        self.job = u"无业游民"
        self.sex = "m"

    def set_lv(self,lv):
        self.lv = lv

    def set_assets(self,assets):
        self.assets = assets

    def re_role_info(self):
        role_info = []
        role_info.append(self.name)
        role_info.append(self.age)
        role_info.append(self.sex)
        role_info.append(self.gril_friend)
        role_info.append(self.job)
        role_info.append(self.salary)
        role_info.append(self.lv)
        role_info.append(self.assets)
        return role_info

#角色操作类https://github.com/getlantern/lantern/archive/latest.tar.gz
class RoleOperate(object):
    def __init__(self):
        pass

    #判断角色名是否存在
    def role_exists(self,role_name):
        user_list = os.listdir("role_info")
        for user in user_list:
            role_list = os.listdir("role_info/%s" %user)
            if (role_name+".pkl") in role_list:
                return True
        return False

    #返回角色列表
    def role_list(self,user):
        role_name_list = []
        role_info = os.listdir("role_info/%s" %user)
        for role in role_info:
            role_name_list.append(role.split(".")[0])
        return role_name_list

    #打印角色列表
    def show_role(self,role_name_list):
        for role in role_name_list:
            print role

    #添加角色
    def add_role(self,user):
        role_name_list = self.role_list(user)
        if len(role_name_list) >3:
            print u"您的游戏角色已经达到3个,不能创建更多角色,如果想创建更多的角色,请删除无用的角色..."
        elif len(role_name_list) <=3:
            role_name = raw_input(u"请输入角色名字:").strip()
            role_exists_status = self.role_exists(role_name)
            if not role_exists_status:
                role_age = raw_input(u"请输入角色年龄:").strip()
                if role_age.isdigit() and int(role_age) <109 and int(role_age) > 0:
                    role_age = int(role_age)
                    #role_sex = raw_input(u"请输入角色性别(w代表女性,m代表男性):").strip()
                    #if role_sex.lower() in ["w","m"]:
                    role1 = Person(role_name,role_age)
                    role_info = role1.re_role_info()
                    UserOperate.write_user(role_info,"role_info/%s/%s.pkl" %(user,role_name))
                    return True
                else:
                    print u"年龄输入错误,请重新注册"
            else:
                print u"角色已存在,请重新注册"

    #删除角色
    def del_role(self,user,role):
        if os.path.exists("role_info/%s/%s.pkl" %(user,role)):
            os.remove("role_info/%s/%s.pkl" %(user,role))
            return True

    #载入角色进度
    def reload_role(self,user,role):
        if os.path.exists("role_info/%s/%s.pkl" %(user,role)):
            role_info = UserOperate.read_user("role_info/%s/%s.pkl" %(user,role))
            return role_info

    #写入角色进度
    @staticmethod
    def write_load(user,role,role_info):
        UserOperate.write_user(role_info,"role_info/%s/%s.pkl" %(user,role))

#用户操作类
class UserOperate(object):
    def __init__(self):
        pass

    #加密密码
    def md5(self,str):
        import hashlib
        import types
        if type(str) is types.StringType:
            m = hashlib.md5()
            m.update(str)
            return m.hexdigest()
        else:
            return ''

    #读取用户文件
    @staticmethod
    def read_user(userfile):
        try:
            f = file(userfile,'rb')
            info = pickle.load(f)
            f.close()
            return info
        except IOError:
            info = {}
            return info

    #写入用户文件
    @staticmethod
    def write_user(user_info,userfile):
        f = file(userfile,'wb')
        pickle.dump(user_info,f)
        f.close()

    #注册用户
    def add_user(self):
        user_info = self.read_user("user_file.pkl")
        while True:
            input_user = raw_input(u"请输入注册账号(exit返回):").strip()
            if len(input_user) == 0:
                print u"输入不能为空，请重新输入"
                continue
            elif input_user in user_info:
                print u"账号已存在，请使用其他账号"
                continue
            elif len(input_user) < 3:
                print u"用户名太短,请输入至少3个字符"
                continue
            elif input_user == "exit":
                print u"正在返回上一级...."
                return False
            else:
                while True:
                    password_1 = raw_input(u"请输入密码(exit返回):")
                    if len(password_1) ==0:
                        print u"密码不能为空,请重新输入"
                        continue
                    '''
                    elif password_1 == "exit":
                        return False
                    '''
                    password_2 = raw_input(u"请再次输入密码:")
                    if password_1 != password_2:
                        print u"两次密码输入不匹配,请重新输入密码"
                        continue
                    elif password_1 == password_2:
                        user_info[input_user] = [self.md5(password_1),""]
                        self.write_user(user_info,"user_file.pkl")
                        if os.path.exists("role_info"):
                            os.mkdir("role_info/%s" %input_user)
                        else:
                            os.mkdir("role_info")
                            os.mkdir("role_info/%s" %input_user)
                        print u"注册成功,您的账户为:%s,密码为:%s\t请牢记你的账号密码" %(input_user,password_1)
                        return True


    #传入用户名和密码，验证用户登录
    def login_verification(self,username,password):
        user_info = self.read_user("user_file.pkl")
        if username not in user_info:
            info = -1 #-1代表用户不存在
            return False,info
        elif username in user_info:
            if user_info[username][1] == "locked":
                info = 0 #0代表用户锁定
                return False,info
            elif user_info[username][0] == self.md5(password) and user_info[username][1] != "locked":
                info = 1 #代表用户正常登录,返回用户类型
                return True,info
            else:
                info = 2
                return False,info

    #锁定用户
    def lock_user(self,username):
        user_info = self.read_user("user_file.pkl")
        if username in user_info:
            user_info[username][1] = "locked"
            self.write_user(user_info,"user_file.pkl")
            return True
        else:
            return False

    #登录控制
    def login_control(self):
        retry_count = 0
        temp_list = []
        while retry_count < 3:
            input_name = raw_input(u"请输入您的用户名:").strip()
            retry_count += 1
            temp_list.append(input_name)
            if len(input_name) ==0:
                print u"空用户名不被允许",
                continue
            input_pwd = raw_input(u"请输入您的密码:")
            login_status = self.login_verification(input_name,input_pwd)
            if login_status[0]:
                print u"%s,欢迎进入游戏......" %input_name
                return input_name
            elif not login_status[0]:
                if login_status[1] == 0:
                    print u"用户已锁定"
                    break
                elif login_status[1] == -1:
                    print u"用户不存在"
                    continue
                elif login_status[1] == 2:
                    print u"用户名密码不正确"
                    continue
        else:
            #print temp_list,input_name,retry_count
            user_info = self.read_user("user_file.pkl")
            if retry_count == 3:
                if temp_list[0]==temp_list[1] == input_name and input_name in user_info:
                    locked = self.lock_user(input_name)
                    if locked:
                        print u"%s,你输入错误三次密码，账户已被锁定" %input_name

#场景类
class GameScene(object):
    def __init__(self,login_name,role_info_list):
        self.login_name = login_name
        self.role_info = role_info_list

    def game_info(self):
        de_info = u"欢迎来到屌丝人生游戏,你可以通过自己的选择改变一生的命运...."
        print de_info
        time.sleep(0.5)

    def study(self):
        over_status = self.age_info()
        if over_status:
            while True:
                print u'''\033[32;0m
++++++++++++++++++++++++++++++++
| 1 Linux运维     学费6000￥     |
| 2 Python开发    学费50000￥    |
| 3 Java开发      学费150000￥   |
++++++++++++++++++++++++++++++++\033[0m
            '''
                study_choice = raw_input(u"请输入编号(exit返回):").strip()
                if study_choice == "1":
                    if self.role_info[-1] < 6000:
                        print u"穷屌丝,等你赚够了钱再来吧,我们这里不是收容所.."
                    else:
                        if self.role_info[-2]<=10:
                            self.role_info[1] += 1
                            self.role_info[-2] +=4
                            self.role_info[-1] -= 6000
                            print u"屌丝%s粪斗了一年,学会了坑爹的Linux运维.." %self.role_info[0]
                        else:
                            print u"骚年你的水平这么高,还来学个毛线的Linux运维啊.."
                elif study_choice == "2":
                    if self.role_info[-1] <50000:
                        print u"穷屌丝,等你赚够了钱再来吧,我们这里不是收容所.."
                    else:
                        if self.role_info[-2]<=30:
                            self.role_info[1] +=1
                            self.role_info[-2] +=15
                            self.role_info[-1] -= 50000
                            print u"屌丝%s粪斗了一年,学会了优雅的Python开发.." %self.role_info[0]
                        else:
                            print u"骚年你的水平这么高,还来学个毛线的Python开发啊.."
                elif study_choice == "3":
                    if self.role_info[-1] <150000:
                        print u"骚年,等你赚够了钱再来吧,我们这里不是收容所.."
                    else:
                        if self.role_info[-2]<=100:
                            self.role_info[1] +=1
                            self.role_info[-2] +=32
                            self.role_info[-1] -= 150000
                            print u"屌丝%s粪斗了一年,学会了高大上的Java开发.." %self.role_info[0]
                        else:
                            print u"骚年你的人生已经达到巅峰了,赶紧去创造你的价值去吧.."
                elif study_choice == "exit":
                    break
                else:
                    print u"别闹,好好学习.."
        else:
            u"\033[31;40m你已经在游戏中自杀...\033[0m"

    def change_work(self):
        over_status = self.age_info()
        if over_status:
            while True:
                print u'''\033[32;0m
++++++++++++++++
| 1 linux运维   |
| 2 Python开发  |
| 3 java开发    |
++++++++++++++++\033[0m
                '''
                work_choice = raw_input(u"输入编号(exit返回):").strip()
                if work_choice == "1":
                    print u"请回下一个问题:",
                    linux_q = raw_input(u"Linux下列出目录下文件的命令是什么:").strip()
                    if linux_q.lower() in ["ls","dir"]:
                        self.role_info[-3] = self.role_info[-2] * 1000
                        self.role_info[4] = u"linux运维"
                        print u"你获得了Linux运维的工作,薪资为%s￥/月" %self.role_info[-3]
                    else:
                        print u"这份工作你生忍不了,你还是在学习下再来吧~"
                elif work_choice == "2":
                    print u"请回下一个问题:",
                    python_q = raw_input(u"Python中用于正则匹配的模块叫什么:").strip()
                    if python_q.lower() == "re":
                        self.role_info[-3] = self.role_info[-2] * 2000
                        self.role_info[4] = u"Python开发"
                        print u"你获得了Python开发的工作,薪资为%s￥/月" %self.role_info[-3]
                    else:
                        print u"这份工作你生忍不了,你还是在学习下再来吧~"
                elif work_choice == "3":
                    print u"请回下一个问题:",
                    python_q = raw_input(u"Java虚拟机中用于编译.java文件的命令叫什么:").strip()
                    if python_q.lower() == "javac":
                        self.role_info[-3] = self.role_info[-2] * 3000
                        self.role_info[4] = u"java开发"
                        print u"你获得了Java开发的工作,薪资为%s￥/月" %self.role_info[-3]
                    else:
                        print u"这份工作你生忍不了,你还是在学习下再来吧~"
                elif work_choice == "exit":
                    break
                else:
                    print u"连选择都不会,你可以自杀了.."
        else:
            print u"\033[31;40m你已经在游戏中自杀...\033[0m"

    def work(self):
        over_status = self.age_info()
        if over_status:
            #salary = self.role_info[-2] * self.role_info[-3]
            print u"你的工资太low了,赶紧换工作吧"
            self.role_info[-1] += self.role_info[-3]
            print u"经过一段时间的努力,你得到了%s￥报酬.." %self.role_info[-3]
        else:
            print u"\033[31;40m你已经在游戏中自杀...\033[0m"

    def make_friends(self):
        over_status = self.age_info()
        if over_status:
            while True:
                print u'''\033[32;0m
++++++++++++++++
| 1 女屌丝(liz) |
| 2 白富美(lara)|
| 3 技术屌丝    |
| 4 技术大牛    |
++++++++++++++++\033[0m
                '''
                friend_choice = raw_input(u"输入编号(exit返回):").strip()
                if friend_choice == "1":
                    print u"%s:Hi,美女,能做我女朋友吗?" %self.role_info[0]
                    time.sleep(1)
                    if self.role_info[-2] < 20:
                        print u"女屌丝:滚一边儿去,姐不喜欢你这种一副屌丝样儿的~~"
                        time.sleep(1)
                        print u"%s:妈蛋,等哥哥有钱了,天天让你...." %self.role_info[0]
                        time.sleep(1)
                    else:
                        if self.role_info[-1] >100000:
                            self.role_info[3] = u"女屌丝(liz)"
                            print u"女屌丝:好啊好啊,我等哥哥表白已经等得花儿都快谢了~~"
                            time.sleep(1)
                            print u"%s:走开房去,正好过七夕~~\n二人度过了一个美妙的夜晚~~" %self.role_info[0]
                            time.sleep(1)
                        else:
                            print u"女屌丝:没钱还敢来调戏老娘,小样你胆子很肥啊~~"
                            time.sleep(1)
                            print u"%s:妈蛋,等哥哥有钱了,天天让你...." %self.role_info[0]
                            time.sleep(1)
                elif friend_choice == "2":
                    print u"%s:Hi,靓女,能做我女朋友吗?" %self.role_info[0]
                    time.sleep(1)
                    if self.role_info[-2] < 80:
                        print u"白富美:就你这一副屌丝样儿的,还想泡我?等你能买得起房、车和几十万的包包的时候再来吧~~"
                        time.sleep(1)
                        print u"%s:艹~~,你给哥等着,总有一天哥天天让你...." %self.role_info[0]
                        time.sleep(1)
                    else:
                        if self.role_info[-1] >1000000:
                            self.role_info[3] = u"白富美(lara)"
                            print u"白富美:我看上了一个20万的包包,帮我买了吧~~"
                            time.sleep(1)
                            print u"%s:给,我的信用卡,拿去刷~没有额度限制~~" %self.role_info[0]
                            time.sleep(1)
                            print u"白富美:么么哒~~我们去开房吧~~"
                            time.sleep(1)
                            print u"%s:走去夏威夷度个长假~~~\n二人度过了一个愉快的旅行~~" %self.role_info[0]
                            time.sleep(1)
                        else:
                            print u"白富美:穿的人模狗样的,原来还是一穷逼,等你年薪过百万的时候在来找我吧~~"
                            time.sleep(1)
                            print u"%s:艹~~,你给哥等着,总有一天哥天天让你...." %self.role_info[0]
                            time.sleep(1)
                elif friend_choice == "3":
                    print u"%s:大牛,能交个朋友吗?" %self.role_info[0]
                    time.sleep(1)
                    if self.role_info[-2] < 20:
                        print u"技术屌丝:哥们儿,给你交朋友简直是掉价啊,你还是学习下咱们在做基友吧~~"
                        time.sleep(1)
                    else:
                        if self.role_info[-1] < 5000:
                            print u"技术屌丝:哥们儿,吃个饭你都付不起钱,你还是赶紧赚钱吧~~"
                            time.sleep(1)
                        else:
                            self.role_info[-2] += 1
                            self.role_info[-1] -= 5000
                            print u"技术屌丝:哥们儿,走一起吃饭去~"
                            time.sleep(1)
                            print u"%s:草了,跟大牛交个朋友真不容易~~" %self.role_info[0]
                            time.sleep(1)
                elif friend_choice == "4":
                    print u"%s:大神,能交个朋友吗?" %self.role_info[0]
                    time.sleep(1)
                    if self.role_info[-2] < 50:
                        print u"技术大牛:哥们儿,给你交朋友简直是掉价啊,你还是再学习下吧~~"
                        time.sleep(1)
                    else:
                        if self.role_info[-1] < 50000:
                            print u"技术大牛:没钱你装个毛线,还是滚蛋吧~~"
                            time.sleep(1)
                        else:
                            self.role_info[-2] += 10
                            self.role_info[-1] -= 50000
                            print u"技术大牛:哥们儿,来一起搞下大数据~~"
                            time.sleep(1)
                            print u"%s:草了,跟大神交个朋友真不容易~~" %self.role_info[0]
                            time.sleep(1)
                elif friend_choice == "exit":
                    break
                else:
                    print u"连选择都不会,你可以自杀了.."
        else:
            print u"\033[31;40m你已经在游戏中自杀...\033[0m"

    def show_info(self):
        over_status = self.age_info()
        if over_status:
            print u'''亲爱的玩家%s
你的年龄现今为:%s
你的工作现为:%s
你的女朋友为:%s
你的薪资现为:%s
你的级别现在为:%s
你的总资产现为:%s
''' %(self.role_info[0],self.role_info[1],self.role_info[4],self.role_info[3],self.role_info[5],self.role_info[-2],self.role_info[-1])
        else:
            print u"\033[31;40m你已经在游戏中自杀...\033[0m"

    def write_info(self):
        UserOperate.write_user(self.role_info,"role_info/%s/%s.pkl" %(self.login_name,self.role_info[0]))
        print u"正在保存游戏进度,请稍后..."
        time.sleep(1)

    def over_lifetime(self):
        over_choice = raw_input(u"你确定你要在游戏中结束你罪恶的一生吗,(y/n)默认为n:").strip()
        if over_choice.lower() == "y":
            self.role_info[1] = -1
            print u"%s结束了自己的一生.." %self.role_info[0]
        else:
            print u"你还需要在考虑考虑.."

    def age_info(self):
        if self.role_info[1] < 0:
            return False
        else:
            return True

    def game_main(self):
        self.game_info()
        while True:
            print u"\033[31;1m%s 级别Lv:%s 资产Assets:%s\033[0m" %(self.role_info[0],self.role_info[-2],self.role_info[-1])
            print u'''你可以通过以下途径来改变自己的一生...\033[31;1m
++++++++++++++++
| 1 学习技能    |
| 2 改变工作    |
| 3 交友       |
| 4 赚钱       |
| 5 查看信息    |
| 6 结束一生    |
| 7 保存进度    |
| 8 退出游戏    |
++++++++++++++++\033[0m
            '''
            life_choice = raw_input(u"请输入编号改变人生吧:").strip()
            if life_choice == "1":
                self.study()
            elif life_choice == "2":
                self.change_work()
            elif life_choice == "3":
                self.make_friends()
            elif life_choice == "4":
                self.work()
            elif life_choice == "5":
                self.show_info()
            elif life_choice == "6":
                self.over_lifetime()
            elif life_choice == "7":
                self.write_info()
            elif life_choice == "8":
                exit_choice = raw_input(u"你还没有保存游戏进度,是否保存游戏进度(y/n)默认为y:").strip()
                if exit_choice.lower() == "n":
                    sys.exit()
                else:
                    self.write_info()
                    sys.exit()
            else:
                print u"再输入错误就自行了断吧,上面有那个功能..."
                time.sleep(1)

if __name__ == '__main__':
    pepole = Person("lisi",22)
    pepole.set_lv(5)
    role_info = pepole.re_role_info()
    print role_info
    scene = GameScene(role_info)
    scene.game_main()
