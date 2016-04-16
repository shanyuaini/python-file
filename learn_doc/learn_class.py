#_*_coding:utf-8 _*_
__author__ = 'sylar'


'''
新式类和经典类
新式类定义方法 #object所有类的基类,是用C写的调用接口
class new_class(object):
经典类定义方法
class old_class:


经典类BUG
    class A:
      ^ ^  def save(self): ...
     /   \
    /     \
   /       \
  /         \
class B     class C:
  ^         ^  def save(self): ...
   \       /
    \     /
     \   /
      \ /
    class D
'''

class A:
    def __init__(self):
        print 'This is A'
    def save(self):
        print 'save method from a'
class B(A):
    def __init__(self):
        print 'This is B'
class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        print 'save method from ---c---'
class D(B,C):
    def __init__(self):
        print 'This is ---d---'
t = D()
t.save()
'''
这种模型中,实例化时要使用save方法,因为经典类用的深度优先
按照模型先找B的.再找C的.因为C已经对save方法重写了.应该使用C的save方法
但是经典类的模型,因为B没有save方法所以去找A.就不让C的重写生效
'''

'''
抽象类 就像一个类的规范,只定义一个类的框架没有实现功能的代码
抽象类必须有另外的来按照抽象类的定义的规范来写实现功能的代码
'''
class Alert:#抽象类
    def Send(self):pass#抽象方法
class Winxin(Alert):   #实现抽象类的类
    def __init__(self):
        print '要开始干事了'
    def Send(self):   #要实现抽象类必须要将抽象类中的抽象方法实现
        print '发送weixin'


'''
继承:
基类(父类),派生类(子类)
'''
class Father(object):
    def __init__(self):
        self.Fname = 'sylar'
    def Func(self):
        print 'Father.func'
    def Bad(self):
        print '抽烟喝酒'
class Son(Father):   #继承
    def __init__(self):
        self.Sname ="tom is sylar's son"
        Father.__init__(self)  #不显示执行构造函数,子类就不能调用父类的构造函数
        #super(Son,self).__init__() 也是执行父类的构造函数.只是需要父类的基类为object
    def Bar(self):
        print 'Son.bar'
    '''
    def Bad(self):   #在子类中重写一个方法,就不继承了父类的方法了.
        print 'son唱歌'
    '''
    def Bad(self):   #在子类中增加一个方法的功能,在原基础上
        Father.Bad(self)
        print '唱歌'

s1 = Son()
s1.Bar()
s1.Func()

'''
对象=属性+方法,属性（特征）和行为来描述一个对象
一个对象的特征也称为属性（attribute）。它所具有的行为也称为方法（method）
类是对象的模板或蓝图，类是对象的抽象化，对象是类的实例化。类不代表具体的事物，而对象表示具体的事物。
class object:
    def __init__():
        pass
    def method1():
        pass
'''

'''
属性:动态字段和静态字段
'''
class human:
### 类属性-->也称为静态字段(类的全局变量),对象在调用是属性相同
    class_name = 'jerry'

###构造函数实例化类的必要函数,定义类对象的属性因为属性不属于类，而是属于各个类的实例。也就是说属于对象。
#因此我们可以给每个实例设置不同的属性.所以类定义时,将对象自己传入是必须的,也就是self参数
    def __init__(self,name,age):#self是class sylar类自身(实例化封装的对象), name, age是实例化对象时传入的参数
        self.Name = name  #对象自身的属性每个对象的值都不相同,便于对象调用--->也称为动态字段,对象属性(对象的全局变量)
        self.Age = age

object1 = human('sylar',18)  #实例化一个对象
object2 = human('tom',8)
print object1.Name,object2.Name  #只能通过对象调用动态字段所以就看出来self.Name属性属于对象不属于类
print human.class_name, object2.class_name #静态字段可以被对象和类调用.(因为对象是属于类的)


'''
静态方法和动态方法
'''
class human1:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
###静态方法
    # 不实例化类就可以使用类,和调用模块中的方法是一样的功能.只是申明这个方法是属于这个类的!
    ## python为了满足面向对象的特性而将调用模块的方式改成更符合面向对象编程的规范
    @staticmethod    #加上静态方法的装饰器
    def foo():       #因为是类的方法所以不能传入对象self,可以传入参数
        print '大家都要努力学习'

###动态方法,同动态字段,是属于对象的,需要实例化才能使用.类是不能使用这个方法
    def sport(self):
        print self.Name + ' 正在参加运动会'
human1.foo()
object1_1 = human1('sylar',18)
object1_1.sport()

'''
property,将一个方法伪装为属性
'''
class human2:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
###特性,模拟访问动态字段的方式去访问方法
    @property
    def bar(self):
        print self.Name + ' day2 去酒吧玩了'

object1_2 = human2('sylar',18)
object1_2.bar  #访问特性


'''
私有方法和私有字段



'''
class human3:
    def __init__(self, name, age, flag):
        self.Name = name
        self.Age = age
        self.__addr = flag  #私有字段,不能直接访问
    def show(self):     #通过一个方法去访问私有字段 不建议
        print self.__addr
    def __show(self):   #私有访问,不能直接访问
        print 'ooo'
    def foo(self):      #通过一个方法去访问私有字段不建议
        self.__show()

    @property   #讲一个私有属性当作一个属性.这个方法就具有只读属性
    def bar(self):
        return self.__show()

object1_3 = human3('sylar', 18, 'day3 去酒吧了')
#print object1_3.__addr #不能直接访问
object1_3.show()
#object1_3.__show() #不能直接访问
object1_3.bar
#object1_3._human3__show()   #默认不能从外部访问,在python中强制访问,不建议使用


'''
只读特性和只写特性
下面这个列子就说明只读可写的作用.在使用了只读的时候.私有字段不能修改
class test1:
    def __init__(self):
        self.__pravite = 'sylar1'
    @property
    def Show(self):
        return self.__pravite
class test2(object):
    def __init__(self):
        self.__pravite = 'sylar2'
    @property
    def Show(self):
        return self.__pravite
t1 = test1()
print t1.Show
t1.Show = 'change1'
print t1.Show

t2 = test2()
print t2.Show
t2.Show = 'change2'
print t2.Show
'''
class human4(object):  #让类能够继承,才支持只读可写特性
    def __init__(self, name, age, flag):
        self.Name = name
        self.Age = age
        self.__addr = flag  #私有字段,不能直接访问

###只读特性
    @property   #讲一个私有属性当作一个属性,通过这个bar
    def bar(self):
        return self.__addr
###可改特性
    @bar.setter   #
    def bar(self,value):
        self.__addr = value

object1_4 = human4('sylar', 18, 'day4 去酒吧了')
print object1_4.bar
object1_4.bar = 'day4 又去KTV了!'
print object1_4.bar

'''
析构函数,python解释器会自动销毁对象在不使用时.析构函数定义就是当销毁对象时所执行的代码
'''
class human5():  #让类能够继承,才支持只读可写特性
    def __init__(self, name, age, ):
        self.Name = name
        self.Age = age
    def __del__(self):
        print '解释器要销毁我了'

'''
__call__方法,给对象添加一对括号时就会执行类里的一个特殊方法,在其它语言中没有这个方法
对象本来就是一个类的实例化结果.所以其它语言里都不能直接再执行对象.python里执行对象时就会调用类的特殊方法
'''
class Call_class():  #让类能够继承,才支持只读可写特性
    def __init__(self, ):
        pass
    def __call__(self):
        print '我是一个对象啊!'

f1 = Call_class()
f1()   #Call_class()()   (Call_class()) 这两种写法都可以执行call





