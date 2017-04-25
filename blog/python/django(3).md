django入门(三) 
=

入门概念:
==
在Django中通过model模块对数据库进行操作.而这些操作又引入了ORM对象关系映射的概念(Object Relational Mapping).

官方文档: [点击链接](https://docs.djangoproject.com/en/1.11/topics/db/models/)

class
======

每个模型(class)相当于单个数据库表，每个属性也是这个表中的一个字段。 属性名就是字段名，它的类型（例如CharField ）相当于数据库的字段类型 （例如 varchar ）:



1. 每个模型都是django.db.models.Model的子类
2. 模型的每个属性表示一个数据库字段。
3. 模型自动会生成数据库访问API(可以通过模型的使用不同方法和属性对数据库进行操作)
4. 要正确的使用model模块,需要在配置文件setting.py中正确的注册INSTALLED_APPS
5. 使用manager.py makemigrations/migrate对数据库新增字段和建表操作(第一篇关于Django入门有提到)

>> PS: 使用mysql时需要先到数据库中建好DB_name, model并不能帮我们直接生成数据库.

```
#model.py
from django.db import models					#引用models
class UserInfo(models.Model):					#申明表名
	username = models.CharField(max_length=50) 	#申明字段,每个类属性称为field
```

field types(字段类型)
======
field对应数据库中每张表的一个字段,不能使用保留字段clean, save, or delete等.每个field类型必须在类中申明对应的类属性.通过这些类属性的作用:

1. 字段包含数据的数据类型(int,varchar,text...).
2. 做html渲染(`<input type="text">, <select>...`)
3. 在自动提交表单中使用Django admin对表单做一些简单的验证.

基本的字段类型:

- AutoField:一个自动递增的id值,在数据没有指定主键时默认生成并作为主键

- CharField: 存储长度较小的字符,必须要指定max_length属性

- TextField: 存储大量的字符文本.

- DateField: 日期date的存储类型

- DateTimeField: 时间datetime类型

- EmailField: email的类型.django会自动帮助检查数据合法性

- IntegerField: int类型

- URLField: url链接

```
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    user_comm = models.TextField()
    reg_date = models.DateTimeField()
    user_email  = models.EmailField()
    user_zone = models.URLField()
```
>> PS: 数据类型基本对应数据中的数据类型概念,只是封装了默认验证和html渲染方法

field options(字段属性)
======

- null: 字段是否可以为空 null = True只影响数据的存储.

```
username = models.CharField(max_length=32,null=True)
```

- blank: 字段是否可以接受空白值,影响前端提交数据是的验证,配合null使用

```
user_comm = models.TextField(blank=True)
```

- choices: 选择器,设置一个选择器在前端展示给用户选择而不是用户自己输入.第一个值是展示出来的选项,第二个值是数据库中实际存储的值
```
 salary_choices_date = (
        ('一档','2000以下'),
        ('二档','4000-8000'),
        ('三档','8000以上'),
    )
    salary_choices = models.CharField(max_length=10,choices=salary_choices_date,default="三档")
```

- db_index: 为字段设置索引

- default: 为字段设置默认值

- editable: 默认为True,设置为false在admin模块中不能修改字段的值,并且 ModelForm中使用该字段也不会进行验证

- error_messages: 可自定义该字段的错误信息

- help_text: 可定义字段的帮助信息

- primary_key: 设置字段为主键,如果不设置会自动生成

- unique: 设置该字段的数据在整个表中是唯一的,不能有重复值.位置值的字段不用创建索引

- verbose_name: 字段别名


Relationship fields(字段关系)
======

一对多的关系应该是：1个对应多个，而多个当中的一个只能对应1个。

>> PS: 一个国家有多个地区, 国家和地区就属于一对多的关系,国家可以有多个地区,这多个地区都是一个国家

多对多应该是：2个以上中的1个对应多个，而多个当中的一个可以对应2个以上的一个以上

>> PS: 老师和学生的关系就是多对多,学生可以有多个老师,老师也可以有多个学生 



- ForeignKey: (外键)一对多关系,
- ManyToManyField: 多对多关系
>> PS: OnetoOneField,这个还没怎么懂.Django特有的一种关系

```
class Author(models.Model):
    auth_name = models.CharField(max_length=32)
    auth_address = models.CharField(max_length=64,null=True,blank=True)
    
class Publisher(models.Model):
    pub_name = models.CharField(max_length=32)
    pub_address = models.CharField(max_length=64,null=True,blank=True)


class Book(models.Model):
    book_name = models.CharField(max_length=32)
    pub = models.ForeignKey(Publisher)
    authors = models.ManyToManyField(Author)

#Publisher可以有多个Book.pub,但是Book.pub不能有多个Publisher,也就是说:出版社可以出版很多书,但是书不能有多个出版社(当让现实中可能会有联合出版,为了理解不考虑那种情况)
#Book.authors可以有多个Author数据,Author也可以有多个Book.authors,书可以有多个作者,一个作者也可以有很多本书.
```


from django.db import models
 
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              
        return self.headline










CSRF
==

官网关于ajax自动发送csrf验证的代码也需要开启{% csrf_token %}

```
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

```












