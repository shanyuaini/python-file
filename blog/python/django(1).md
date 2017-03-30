Django入门(一)
=
官方网站: [点击](https://www.djangoproject.com/)

Django 项目是一个python定制框架，它源自一个在线新闻 Web 站点，于 2005 年以开源的形式被释放出来。Django 框架的核心组件有：  
- 用于创建模型的对象关系映射  
- 为最终用户设计的完美管理界面  
- 一流的 URL 设计  
- 设计者友好的模板语言  
- 缓存系统。  

设计模式MVC和MTV
===
简单来说就是按照不同的功能将文件打包归类的方法.

- MVC: 大多数web框架使用的设计模式  
Models: 数据库操作  (模型)  
Views: html模版 	   (视图)  
Controllers: web后台处理函数 (控制器)  

- MTV:django中使用的设计模式  
Models: 数据库操作 (模型)  
Templates: html模版 (视图)  
Views: web后台处理函数 (控制器)  

>>PS: 关于设计模式,不太懂,这里有个文章[点击](https://www.gitbook.com/book/wizardforcel/django-design-patterns-and-best-practices/details)

![](http://7xread.com1.z0.glb.clouddn.com/eab4e97e-605b-4ce2-bda6-a9a38c480131)


基本操作
==

安装
===
```
pip install django
```

###创建项目
一个项目可以有创建多个APP
```
(python3) D:\git>c:\users\admin\python3\Scripts\django-admin.exe startproject Mysite
#windwons中需要将django-admin加入环境变量,不然就要使用绝对路径使用命令
```
![](http://7xread.com1.z0.glb.clouddn.com/9a945907-e13f-404f-91cd-46033af47431)

>>PS:执行这条命令之后会创建一个项目主文件夹Mysite打包所有的项目文件,在主文件夹下面又会生成一个项目配置文件, 


setting.py: 项目主配置文件  
urls.py: 路由文件  
wsgi.py: 项目的socket服务  
templates: html模版  
manager.py: 项目主程序,封装了django的默认命令通过执行该文件启动管理项目  


>>PS: 使用pycharm的时候最好用ide自己的创建newproject功能.在cmd创建的项目在pycharm会有一些路径问题.应该是pycharm的bug.不能正确读取项目的配置吧.也或许是settings某些配置需要手动配置.很早就发现这个问题,一直没有仔细研究


创建app
===

```
cd  D:\git\Mysite
(python3) D:\git\Mysite>python manage.py startapp monitor
```
![](http://7xread.com1.z0.glb.clouddn.com/e15e68d0-d351-4683-83ef-a78d7690cfe6)


同时在settings.py中注册一下app.一定要逗号.
![](http://7xread.com1.z0.glb.clouddn.com/15c5dbde-f42a-431d-b450-ad144626479b)

>>PS: 在项目主文件夹下创建APP 

每个app下的默认目录有如下文件

![](http://7xread.com1.z0.glb.clouddn.com/628b5d74-7918-453d-ba51-bfd0a35424a3)

migrations: 数据管理模块  
admin.py: django自带的后台配置管理  
apps.py: APP的配置文件  
models.py: MTV中的models,只能是一个文件,不能动  
views.py: MTV中的views,可以改为一个文件夹  

运行第一个APP
===

```
(python3) D:\git\Mysite>python manage.py runserver 127.0.0.1:8000
```

- 在执行之前我们先要给urls路由文件定义一个页面

```
from django.conf.urls import url
from django.contrib import admin
from monitor import views #导入monitor这个app的views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home)  #表示访问home页面由views.home函数处理
]
```

- 同时给views.py定义一个函数来处理请求

```
from django.shortcuts import render
from django.shortcuts import HttpResponse 

# Create your views here.

def home(request):
    return HttpResponse('Django app "monitor" is runnning')  #使用HttpResponse给用户返回一个'OK'
```

![](http://7xread.com1.z0.glb.clouddn.com/180a1a79-ad7b-48bf-bbe4-dfe64f484e5d)


数据库操作
===
djang的数据库在settings.py里的DATABASES()配置,默认使用sqlite,而数据库的管理是通过migrations,新建的models文件会经过migrations生成migrations代码文件,migrate通过migrations代码文件生成数据库的表数据.所以要先makemigrations再进行migrate

- makemigrations生成migrations文件
```
(python3) D:\git\Mysite>python manage.py makemigrations
```

![](http://7xread.com1.z0.glb.clouddn.com/2aa710ba-88b6-44a9-b811-93a25644a7cb)

makemigrations会根据models.py中的代码去和当前migrations代码对比生成新的migrations代码.

- migrate根据migrations创建数据库相关

```
(python3) D:\git\django\Mysite>python manage.py migrate
```
![](http://7xread.com1.z0.glb.clouddn.com/8c7586dc-fe24-4852-b06f-cdf4f6932028)

migrate会根据当前的migrations代码和django已经使用中的migrations文件做对比对数据库表进行操作

>>PS: Django默认是依赖一些数据库表

默认admin
===
默认后台的管理员

```
(python3) D:\git\django\Mysite>python manage.py createsuperuser
```

![图片描述](http://7xread.com1.z0.glb.clouddn.com/a6a066ca-46ee-47f0-959d-920744e71d7a)

![](http://7xread.com1.z0.glb.clouddn.com/3341a4ac-72c8-4547-afe9-d19abacf4541)


静态文件设置,按照规范应该设置统一路径
===
1. html在项目的settings.py里设定,应该设在templates
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ...
```
2. js,css,images也是在settings里设置

```
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static')
)
```

路由系统  urls.py 
===
将用户不同请求的发送到后端进行不同的处理,定义路由有两种方式

- 根据路由规则对应views中函数,支持正则表达式


```
#urls.py中定义
url(r'^blogs/(\d*)', views.blogs),  
url(r'^blogs/(?P<name>\w*)/(?P<id>\d*)', views.blogs),
url(r'^blogs/(?P<name>\w*)', views.blogs,{'id':333}),
```
>>PS: #urls会自动把blogs/后的数据作为arg传给后端.'/'分割参数 "r'^blogs/(\d*)/(\d*)"就会传两个参数
#monitor.views定义blgos函数
```
def blogs(request,arg):  
    return HttpResponse(arg) ###将获取到的arg返回
```
>>PS: request封装了请求的所有数据,  
>>request.POST可以取得用POST方法请求的数据   
>>request.GET可以取得用GET方法请求的数据.  
>>arg是urls.py通过分析链接发过来的参数

![](http://7xread.com1.z0.glb.clouddn.com/67a58d34-1509-436f-9135-5e06e1743e52)

- 根据APP对路由规则进行分类(二级路由)

在项目的urls.py加入代码:
```
from django.conf.urls import include
from cmdb import urls
urlpatterns = [
    url(r'^cmdb/', include('cmdb.urls')),
]
#建立指向cmdb的路由规则
```
新建一个cmdb的app,并在app中新建urls.py
```
from django.conf.urls import url
from cmdb import views
urlpatterns = [
    url(r'^myhome/', views.myHome),
]
#在APP中建立myhome的路由规则
```
views.py中加入代码
```
from django.shortcuts import HttpResponse
def myHome(request):
    return HttpResponse('app "cmdb" home')
```

![](http://7xread.com1.z0.glb.clouddn.com/97bbfe62-bac4-47cd-838a-497af96946a9)




数据库的基本增删改查
===
django有自己的orm.简单来说就是在models.py创建一个类就是创建一张表,类里的字段就生成一个列(也就是数据库的字段),一般每个APP都有自己的models.py

>>同样我也说不清楚这个,文档: [点击](http://www.open-open.com/lib/view/open1420814506140.html)

创建表
=====
1. 在app的models.py加入代码:  

```
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
```

2. 执行migrate

![](http://7xread.com1.z0.glb.clouddn.com/ede776af-0e37-4199-b890-b6c1c31e6b8e)

此时我们就可以在migrations目录下发现文件
![](http://7xread.com1.z0.glb.clouddn.com/0ab196a4-7314-4686-9328-12bad92dffe1)


增删改查
=====
```
#增
models.UserInfo.objects.create(username='sylar',password='123456',age=73)
dic = {'username':'tom', 'password':'123456','age':73}
models.UserInfo.objects.create(**dic)
# 查.all()所有,.filter('条件') .first() 第一条
models.UserInfo.objects.filter(age=73).first()
#删
models.UserInfo.objects.filter(username='tom').delete()
#查.all()所有,.filter('条件')
#改
models.UserInfo.objects.all().update(age=20)
models.UserInfo.objects.filter(username='tom').update(age=80)
user_list = models.UserInfo.objects.all()
```

数据展示的小例
=====
1. cmdb的views.py增加代码:

```
from django.shortcuts import render
def db_handle(request):
	#自定义添加几条数据
    user_list = models.UserInfo.objects.all()
    return render(request,'db.html',{'li':user_list})
    #使用render渲染,同时返回用户db.html和数据字典
```
2.cmdb的urls.py代码:
在url中增加db
```
urlpatterns = [
    url(r'^myhome/', views.myHome),
    url(r'^db/', views.db_handle),
]
```

3.在项目templates文件夹增加一个db.html代码

```
<table border="1">
    <thead>
        <tr>
            <th>用户名</th>
            <th>密码</th>
            <th>年龄</th>
        </tr>
    </thead>
    <body>
        {% for item in li %}
        //根据返回的数据字典的key 'li'循环数据
             <tr>
                <td>{{ item.username }}</td>
                <td>{{ item.password }}</td>
                <td>{{ item.age }}</td>
				//将取得数据展示
			</tr>
        {% endfor %}
    </body>
</table>
```
![](http://7xread.com1.z0.glb.clouddn.com/9afee54e-0e07-4c8a-9c56-d2b1f67a177f)

用户数据提交 
===
>>PS: 如果用post方式提交要将settings里的MIDDLEWARE:'django.middleware.csrf.CsrfViewMiddleware',注释

db.html
```
    <form action="/cmdb/db/" method="post">
    //action地址一定要以'/'结束.不然django会报错
        <p><input type="text" name="username"/></p>
        <p><input type="password" name="password"/></p>
        <p><input type="text" name="age"/></p>
        <p><input type="submit" value="提交"/></p>
    </form>
```

```
def db_handle(request):

    if request.method == "POST":
        #print(request.POST)
        Age = int(request.POST['age'])
        user_name = request.POST['username']
        pass_word = request.POST['password']
        dic = {'username': user_name, 'password': pass_word, 'age': Age}
        models.UserInfo.objects.create(**dic)
        #models.UserInfo.objects.create(**dic)
    user_list = models.UserInfo.objects.all()
    return render(request,'db.html',{'li':user_list})
```
![](http://7xread.com1.z0.glb.clouddn.com/ec29cdf0-ae7f-4d1a-8241-a0c5a156a3ea)


了解了这些配合js,css就可以写简单又丑陋的网站了.....
