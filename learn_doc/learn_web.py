#_*_coding:utf-8 _*_
__author__ = 'sylar'

'''
bootstrap
前端设计
需要jquery支持

'''
'''
MVC&MTV都分为三部分
Controller   (控制器)URL分发器.接受用户操作
Model        (模型)DB数据访问操作接口
View         (视图)业务逻辑处理和展现.

MTV在django中的MVC实现.Controller由框架自己实现,将MVC中View的逻辑处理和展现拆分为Template和View
Model        (模型)数据存取层,
Template     (模板)表现层,html.
View         (视图)业务逻辑处理.模型和模版的桥梁

'''


'''
用pycharm生成的django项目目录结构
--learn_django       #以项目名命名的配置文件,web框架相关的目录
----setting.py       #数据库相关配置
----urls.py          #url分发器
----wsgi.py          #wsgi接口

--app01              #项目相关
----migrations
------admin
------apps.py        #项目自己的配置文件,通常可以不用
------models.py      #MTV或MVC模型,数据库定义的接口和调用
------tests.py       #测试
------views.py       #试图
--template           #html模版
--manager.py         #web框架,定义一个web服务器.用于开发时用的web服务器.调试用
'''

'''
manager.py  configration #调试配置

script parameters:  runserver 127.0.0.1:8000
'''

'''基本用法
查看learn_django项目和注释
https://docs.djangoproject.com/en/1.9/
'''
