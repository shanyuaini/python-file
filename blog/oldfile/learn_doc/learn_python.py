#_*_coding:utf-8 _*_
__author__ = 'sylar'


'''
python自学相关
python IDE-->help-->python doc
PEP: Python enhancement proposals :  python增强建议书,用来规范与定义python的各种加强与延伸功能的技术规格,好让python开发社区能有共同遵循的依据.
每个PEP都有一个唯一的编号.这个编号一旦规定了就不会再改变.例如PEP3000就是用来定义Python3.0的相关技术规格;而PEP33则是python的web应用程序接口WSGI(web server gateway interface1.0)规范
关于PEP本身的相关规范是定义在PEP1,而PEP8定义了Python代码的风格指南.有关PEP的列表可以参考PEP0:http://www.python.org/dev/peps/
'''
'''
命令行快速获取模块的帮助
import os   #导入模块
os.__doc__  #使用__doc__私有方法查看说明文档
dir(os)     #查看模块所有的元素
os.__all__  #过滤查看
os.__file__ #查看模块的路径
help(os)    #模块的帮助文档
'''