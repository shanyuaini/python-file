Django入门(二)
=

urls匹配
==
在urls.py中url的书写格式是url(r'^路径/路径/$', views.somefunc).逗号前面的部分表示浏览器显示的路径,逗号后面是后端的控制器代码的位置(通常是一个函数).使用模糊匹配时路径会按一定规则分割做为参数传递给后端函数.后端要注意接受多个参数(静态匹配除外)

官方文档: [点击](https://docs.djangoproject.com/en/1.10/topics/http/urls/)

- To capture a value from the URL, just put parenthesis around it.
- There’s no need to add a leading slash, because every URL has that. For example, it’s ^articles, not ^/articles.
- The 'r' in front of each regular expression string is optional but recommended. It tells Python that a string is “raw” – that nothing in the string should be escaped. See Dive Into Python’s explanation.

>>1. 要从url中用括号()包围需要捕获参数.  
>>2. r'^articles/ 不能写成r'^/articles,因为这里是正则表达式不适用linux中的'/'根的概念  
>>3. 'r'字符表示使用正则表达式匹配

静态匹配
===
明确的定义路径

```
url(r'^articles/2017/$', views.arts_test),
#url(r'^articles/(2017)/$', views.arts_test)这样写 后端arts_test(request,arg) arg应该能获取到2017这个字符
```
在后端views定义一个arts_test来响应用户请求

```
def arts_test(request):
    return HttpResponse('OK')
```
![](http://7xread.com1.z0.glb.clouddn.com/d99fcdd1-acbd-4b6d-b5e3-28fa461c86d0)

>>PS: 此时可以看到整个articles/2017会做为request传递给后端函数

模糊匹配
===
按照一定规则进行匹配,例如按照年月日对文章进行分类查找 ,

```
url(r'^articles/2[0-9]{3}/[0-9]{2}/[0-9]+/$', views.dynamic_test),
```
dynamic_test
```
def dynamic_test(request):
    print(request)
    return HttpResponse('dynamic_test')
```

![](http://7xread.com1.z0.glb.clouddn.com/b1ec7dcb-7429-478e-8e67-653870935da5)

Named groups
===
通过正则表达式,让urls传递将后端的参数的参数名指定.后端的参数名必须于前端定义的别名相同才能取到对应值.


```
url(r'^articles/(?P<user_name>\w*)/(?P<file_name>\d*).(?P<file_type>\w*)',views.name_groups)
#(?P<别名>正则表达式'\d'数字,'\w'字符)
```

```
def name_groups(request,user_name,file_type,file_name):
    print(request,user_name,file_name,file_type)
    return HttpResponse('name_groups')
    #name_groups的参数必须和url中一对应,相当于name_groups函数设置了默认参数,通过urls修改默认参数的值
```

![](http://7xread.com1.z0.glb.clouddn.com/1aacb6e0-3ea6-45d7-b6bf-9b31d8fdf48f)


include去冗余代码
===
include不只是可以引入urls文件,还可以去除重复代码(抄一个官网的例子):

```
urlpatterns = [
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/history/$', views.history),
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/edit/$', views.edit),
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/discuss/$', views.discuss),
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/permissions/$', views.permissions),
]
```
```
urlpatterns = [
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/', include([
        url(r'^history/$', views.history),
        url(r'^edit/$', views.edit),
        url(r'^discuss/$', views.discuss),
        url(r'^permissions/$', views.permissions),
    ])),
]
```

额外传递参数extra options
===

在url中定义一个字典传递一个参数,函数中的参数名要和字典的key一致

```
url(r'^extra_opt/2017/$', views.extra_opt,{'ext':'opt'}),
```
```
def extra_opt(request,ext):
    print(ext)
    return HttpResponse(ext)
```
![](http://7xread.com1.z0.glb.clouddn.com/46acfdb9-6733-4c43-bd9e-11c51ac9694d)


其他的方法:
===

还太肤浅,不能完全理解下面几种定义的作用和方法

- Reverse resolution of URLs
- Naming URL patterns
- URL namespaces
- URL namespaces and included URLconfs

获取请求数据
==

request参数会封装用户的请求传递到后端,Django中只支持GET和POST方法
request.GET 明文提交数据,GET,默认是获取数据,只能读取数据
request.POST 非明文提交数据,默认是提交数据,涉及数据创建和修改



官方文档: [点击](https://docs.djangoproject.com/en/1.10/ref/request-response/#module-django.http)
>> 没有找到关于具体说明,暂时先放一个HttpRequest地址.

template处理
==

django中使用 DTL 来渲染html
telmplate 文档: [链接描述](https://docs.djangoproject.com/en/1.10/topics/templates/)

先介绍下django中给用户返回数据的方法,有两种:

- HttpResponse 返回一个字符串
- render 直接返回一个html文档

render文档: [点击](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/)

简单的给Mysite项目的cmdb制作一个可访问的首页
```
#cmdb/urls.py
urlpatterns = [
	...
	url(r'^$', views.index),
	...
]

#cmdb/views.py
def index(request):
    return render(request,'cmdb/index.html')

#templates/cmdb/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>Welcome!!</p>
</body>
</html>
```

templates渲染
===




变量
=====

在html文件中使用{{Variables}}来表示

同时传递到模版的变量也适用变量实例类型的方法
```
{{ my_list.0 }}				#list[index]
{{ my_dict.key }}  			#字典的方法
{{ my_object.attribute }} 	#对象的属性
...
```

小例
```
#views.py
def index(request):
    if request.method == 'GET':
        user_info = {
            'user_id' : '001',
            'user_name' : 'sylar'
        }
        return render(request,'cmdb/index.html',{'user_obj':user_info})
    else:
        return render(request,'404.html')
	#render 是以列表的形式将数据返, 在模版中使用这个字典的key属性就可以取相应的值
	
#index.html
<p>Welcome {{user_obj.user_name}}!You ID is {{ user_obj.user_id }} </p>
#user_obj.user_name == user_info['user_id']
```

![](http://7xread.com1.z0.glb.clouddn.com/5e4be66e-d883-4096-9c0a-42ca102979aa)

循环
=====
使用{% loop_code %},需要注意的是循环语句需要结束.
```
{% for foo in user_obj %}
	somecode
{% endfor %}
{% if user_obj %}
	somecode
{% endif %}
```

小例:
```
#views.py
def index(request):
    if request.method == 'GET':
        user_info = [
            {'user_id' : '001','user_name' : 'sylar'},
            {'user_id' : '002','user_name' : 'tom'},
            {'user_id' : '003','user_name' : 'jerry'},
         ]
        return render(request,'cmdb/index.html',{'user_obj':user_info})
    else:
        return render(request,'404.html')
	
#index.html
{% for foo in user_obj %}
    {% if foo.user_id == '002' %}
    {#% if forloop.counter>2 %#}
    {#% if forloop.counter|divisibleby:'2' %#}
        <p style="color: red">Welcome {{foo.user_name}}! </p>
        <p style="color: red">You ID is {{ foo.user_id }}!!</p>
    {% else %}
        <p>Welcome {{foo.user_name}}! </p>
        <p>You ID is {{ foo.user_id }}!!</p>
    {% endif %}
{% endfor %}
#{#% somestrings %#} 注释
#forloop.counter>2 循环计数器,默认从1开始计数,要从0开始就要使用counter0
#divisibleby:'2': 是否可以被2整除
```
>> 更多内置方法: [点击](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/)

![](http://7xread.com1.z0.glb.clouddn.com/2fc81a0f-7366-45b8-96f5-7cd21af970a3)



模版继承和调用extends和include
=====
来之官网的原文
**extends继承模版:**

每个模板只包含对自己而言独一无二的代码。 无需多余的部分。 如果想进行站点级的设计修改，仅需修改 base.html ，所有其它模板会立即反映出所作修改。

以下是其工作方式。 在加载 current_datetime.html 模板时，模板引擎发现了 {% extends %} 标签， 注意到该模板是一个子模板。 模板引擎立即装载其父模板，即本例中的 base.html 。

此时，模板引擎注意到 base.html 中的三个 {% block %} 标签，并用子模板的内容替换这些 block 。因此，引擎将会使用我们在 { block title %} 中定义的标题，对 {% block content %} 也是如此。 所以，网页标题一块将由{% block title %}替换，同样地，网页的内容一块将由 {% block content %}替换。

注意由于子模板并没有定义 footer 块，模板系统将使用在父模板中定义的值。 父模板 {% block %} 标签中的内容总是被当作一条退路。

继承并不会影响到模板的上下文。 换句话说，任何处在继承树上的模板都可以访问到你传到模板中的每一个模板变量。

你可以根据需要使用任意多的继承次数。 使用继承的一种常见方式是下面的三层法：

1. 创建 base.html 模板，在其中定义站点的主要外观感受。 这些都是不常修改甚至从不修改的部分。

2. 为网站的每个区域创建 base_SECTION.html 模板(例如, base_photos.html 和 base_forum.html )。这些模板对base.html 进行拓展，并包含区域特定的风格与设计。

3. 为每种类型的页面创建独立的模板，例如论坛页面或者图片库。 这些模板拓展相应的区域模板。

这个方法可最大限度地重用代码，并使得向公共区域（如区域级的导航）添加内容成为一件轻松的工作。

以下是使用模板继承的一些诀窍：
- 如果在模板中使用 {% extends %} ，必须保证其为模板中的第一个模板标记。 否则，模板继承将不起作用。

- 一般来说，基础模板中的 {% block %} 标签越多越好。 记住，子模板不必定义父模板中所有的代码块，因此你可以用合理的缺省值对一些代码块进行填充，然后只对子模板所需的代码块进行（重）定义。 俗话说，钩子越多越好。

- 如果发觉自己在多个模板之间拷贝代码，你应该考虑将该代码段放置到父模板的某个 {% block %} 中。

- 如果你需要访问父模板中的块的内容，使用 {{ block.super }}这个标签吧，这一个魔法变量将会表现出父模板中的内容。 如果只想在上级代码块基础上添加内容，而不是全部重载，该变量就显得非常有用了。

- 不允许在同一个模板中定义多个同名的 {% block %} 。 存在这样的限制是因为block 标签的工作方式是双向的。 也就是说，block 标签不仅挖了一个要填的坑，也定义了在父模板中这个坑所填充的内容。如果模板中出现了两个相同名称的 {% block %} 标签，父模板将无从得知要使用哪个块的内容。


```
{% extends "base.html" %}
	#继承的代码
{% block xx %}
	#在base.html中用同样block 包裹的代码,可以在这里被修改
{% endblock %}
	#继承的代码
```

**include调用模版:**
只是简单调用整个HTML文件代码,通常用在不会修改,而又大量使用的html.
{% include "base.html" %}




django的表单form
==
官方文档: [点击](https://docs.djangoproject.com/en/1.11/topics/forms/)

form
======
django默认的form表单可以生成前端的form表单元素,并对数据合法性进行验证,

表单元素属性:

1. required: 是否必须 
2. max_length: 最大长度,
3. min_length: 最少长度,
4. error_messages: 自定义错误信息
5. widget: 前端样式
6. validators: 验证器,可以在这里设置一些方法对数据进行处理


```
#cmdb/urls.py
url(r'^test/$', views.TestForm),

#cmdb/views.py
def TestForm(request):
    form = formtest.TestForm
    return render(request,'cmdb/testform.html',{'TestForm': form})

#cmdb/formtest.py
import re
from django import forms
from django.core.exceptions import ValidationError

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')
#设置一个手机号验证的模块

class TestForm(forms.Form):
    user_type_choice = ((0, u'普通用户'),(1, u'高级用户'),)
	#设置提供选项的变量
    user_type = forms.IntegerField(widget=forms.widgets.Select(choices=user_type_choice,attrs={'class': "form-control"}))
    #定义一个form表单元素select选择器.并将选项和样式传给前端页面

    title = forms.CharField(max_length=20,			
                            min_length=5,
                            error_messages={'required': u'标题不能为空',
                                            'min_length': u'标题最少为5个字符',
                                            'max_length': u'标题最多为20个字符'},
                            widget=forms.TextInput(attrs={'class': "form-control",'placeholder': u'标题5-20个字符'}))
	
    memo = forms.CharField(required=False,
                           max_length=256,
                           widget=forms.widgets.Textarea(attrs={'class': "form-control no-radius", 'placeholder': u'详细描述', 'rows': 3}))

    phone = forms.CharField(validators=[mobile_validate, ],
                            error_messages={'required': u'手机不能为空'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'手机号码'}))

    email = forms.EmailField(required=False,
                             error_messages={'required': u'邮箱不能为空', 'invalid': u'邮箱格式错误'},
                             widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}))
                             
                             
#templates/cmdb/testform.html
<form action="" method="post">{% csrf_token %}
    {% for i in TestForm %}
      <p>{{ i.name }}:{{ i }}</p> <br>
    {% endfor %}
    <hr>
    <input type="submit" value="设置用户信息">
</form>
#前端页面获取form表单
```
>>PS: 缺点是不能直接引用展示数据库中的数据

modelform
======
想对一些数据库的数据进行前端展示就要用到forms下的ModelForm(普通的数据可以直接使用form)

modelform基本语法
```
#cmdb/formtest.py
from django import forms   #forms模块
from cmdb import models	   #应用数据库的
class UserInfo(forms.ModelForm):

    class Meta:            #申明应用哪些表或哪些字段
        model = models.UserInfo
        #申明应用哪些表
        fields = ('username','password','age')
        #或申明应用哪些字段
        # exclude = ()   ModelForm要求fields或exclude必须要申明,如果不使用过滤显示所有字段可以将exclude设为空
        
		widgets = {'username' : forms.TextInput(attrs={'class':'form-control'}),}
		#申明字段在前端展示的样式

#cmdb/urls.py
url(r'^testform/$', views.UserInfo), 	#定义路径

#cmdb/views.py
from cmdb import formtest
def UserInfo(request):
    form = formtest.UserForm()			#实例化表单
    return render(request,'cmdb/formtest.html',{'UserForm':form})  #给前端返回

#templates/cmdb/formtest.html
    <form action="" method="post">{% csrf_token %}
        {{ UserForm }}
        //{{ UserForm.password.name }} 单独取表单中的一个元素名称
        //{{ UserForm.password }}  单独取表单中的一个元素
        
        <input type="submit" value="设置用户信息">
    </form>
```

添加前端验证功能

```
#cmdb/views.py
from cmdb import formtest
from cmdb import models
def UserInfo(request):
    form = formtest.UserForm()
    if request.method == 'POST':  			   #如果是post提交
        form = formtest.UserForm(request.POST) #获取用户输入
        #form有一个cleaned_data 的方法可以清理用户请求中数据,比如html和一些元数据.使
        if form.is_valid():					   #验证数据合法性
            form.save()  					   #将用户的输入保存
    return render(request,'cmdb/formtest.html',{'UserForm':form})

```


django-admin定制
==



启动
======

django的自带的默认数据后台.启用只需要简单的几步.


```
#1. 创建管理员
python manage.py createsuperuser

#2. 项目里的usrls.py设置  
url(r'^admin/', include(admin.site.urls))

#3. 创建数据库app下的cmdb/models.py
from django.db import models
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    def __str__(self):
        return '<%s>'%(self.book_name)
    #python版本:3.+使用__str__返回在web页面需要展示的数据, 2.+使用__unicode__,否则会返回数据的对象名   
    class Meta():
	    verbose_name_plural = '用户列表'
	    #定义UserInfo这个表在web中的展示名

#4. app下的注册数据库cmdb/admin.py
from django.contrib import admin
from cmdb import models
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'age')
    #设置展示的内容
    search_fields = ('username', 'age')
    list_filter = ('username', 'age')
    #search_fields和list_filter设置了就可以使用默认的搜索
admin.site.register(models.UserInfo, UserInfoAdmin)
#注册数据库和admin的web内容
```
![](http://7xread.com1.z0.glb.clouddn.com/35a189da-c412-4144-8398-a92d14526e3a)


定制
======

在admin.py里面定义的类设置

1. list_display: 需要显示的字段
2. search_fields: 可搜索的字段,1,不能搜索manytomany的字段.2,有外键关联的字段要使用"local-fields__otherfields"自己的字段名和关联的字段名中间两个下划线
3. list_fields: 过滤器根据不同字段属性过滤数据
4. list_editable: 让字段可以在web中修改.web中展示的第一个字段不可修改
5. list_per_date: 每页显示的数据条数
6. filter_horizontal: 多对多的字段数据展示.
7. raw_id_fields: 外键数据展示
8. ordering: 按照哪个字段排序
9. short_description: 设置元素在web中的展示名
10. actions: 定义web中action的操作.可定制批量修改数据.


```
#cmdb/models.py
from django.db import models
from django.utils.html import format_html
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    status_choices = (('yes',u"成功"),('no',u"失败"),('unkonw',u"未知"))
    #设置状态信息
    status = models.CharField(choices=status_choices,max_length=32,default='unkonw')
    #添加状态字段
    class Meta():
        verbose_name_plural = '用户列表'
    #设置数据库名在web中展示名
    def colored_status(self):
        if self.status == 'yes':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">成功</span>')
        elif self.status == 'no':
            format_td = format_html('<span style="padding:2px;background-color:red;color:white">失败</span>')
        elif self.status == 'unkonw':
            format_td = format_html('<span style="padding:2px;background-color:yellow;color:black">未知</span>')
        return format_td
    #修改需要高亮字段的展示方式.根据status字段的值,展示一个高亮的html



#cmdb/admin.py
from django.contrib import admin
from cmdb import models

def make_yes(modelAdmin,request,queryset):
    queryset.update(status='yes')
make_yes.short_description = "设置为成功" 

def make_no(modelAdmin,request,queryset):
    queryset.update(status='no')
make_no.short_description = "设置为失败"

def make_unkonw(modelAdmin,request,queryset):
    queryset.update(status='unkonw')
make_unkonw.short_description = "设置为未知"

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'status','colored_status','password', 'age',)
    search_fields = ('username', 'age')
    list_filter = ('username', 'age')
    actions = [make_yes,make_no,make_unkonw] 
    #设置action的函数
    models.UserInfo.colored_status.short_description = '状态'
    #colored_status字段在web中的展示名
admin.site.register(models.UserInfo, UserInfoAdmin)
```

![](http://7xread.com1.z0.glb.clouddn.com/8317662c-1335-4270-92f6-572fee9fd3ea)

>> PS:  一个admin定制化的项目xadmin



Django 配置文件
==

在项目中找到setting.py(直接copy我的一个学习目录.项目建错名了Mystie)

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#定义项目路径,方便项目中文件和包的引用.

DEBUG = True			#开发模式,如果改为Flase需要指定ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmdb',
    'monitor',
]
#在项目中申明APP


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#中间件系统

ROOT_URLCONF = 'Mystie.urls'	#定义项目全局的urls.py入口

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        #这个默认是Django的模版引擎
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        #定义html模版路径,[os.path.join(BASE_DIR, 'templates'),'/home/www/html'],默认会到这几个路径中寻找html文件
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#html模版相关设置

WSGI_APPLICATION = 'Mystie.wsgi.application'
#wsgi插件引擎


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#定义数据库的类型和链接信息


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#密码验证相关


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#时区,语言编码等设置

STATIC_URL = '/static/' 		#定义静态文件引用的路径别名

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static')
)
#定义静态文件引用哪些文件夹,类似templates路径的作用


```

数据库的链接配置修改
======

默认使用的sqlite,mysql数据库的配置.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name', 
        'HOST':'db_host',
        'PORT':'db_port',
        'USER':'db_user',
        'PASSWORD':'db_password'
    }
}
```

