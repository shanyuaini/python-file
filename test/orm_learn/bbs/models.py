from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.


#文章
class Article(models.Model):
    title = models.CharField('标题',max_length=255,)
    brief = models.CharField('简介',null=True,blank=True,max_length=255,)
    category = models.ForeignKey("Category")  #外键关联一个表,引号是通过反射方式找到这个表,因为代码从上往下执行时Category还没生成所以需要反射
    content = models.TextField("文章内容")
    author = models.ForeignKey("UserProfile")
    pub_date = models.DateTimeField('发布时间',null=True,blank=True,) #生成时间
    mod_date = models.DateTimeField('修改时间',auto_now=True,) #auto_now 每次更改都要更新,auto_now_add只是第一次创建生成
    priority = models.IntegerField("优先级",default=10)
    status_choices = ((1,'草稿'),
                      (2,'已发布'))
    status = models.IntegerField(choices=status_choices,default=2)
    title_img = models.ImageField('文章配图',null=True,blank=True,upload_to='statics/images/uploads')

    def clean(self):
        if self.status == 1 and self.pub_date is not None:
            raise ValidationError(('草稿'))
        if self.status == 2 and self.pub_date is None:
            self.pub_date= datetime.date.today()
    #djang的clean方法可以自定义检查方法

    def __str__(self):
        return '%s'%(self.title)

#评论
class Comment(models.Model):
    comment = models.TextField(blank=True,null=True)
    article = models.ForeignKey(Article,help_text='所属文章')
    parent_comment=models.ForeignKey('self',related_name='children',null=True,blank=True)
    #关联父评论
    comment_choices= ((1,'评论'),
                      (2,'点赞'))
    comment_type = models.IntegerField(choices=comment_choices,default=1)
    user = models.ForeignKey("UserProfile")
    comm_date = models.DateTimeField('评论时间',auto_now_add=True,)

    def clean(self):
        if self.comment_type ==1 and len(self.comment) == 0:
            raise ValidationError('评论不能为空')
     #判断评论是否为空

    def __str__(self):
        return '%s' % (self.comment)

#板块
class Category(models.Model):
    name = models.CharField('板块名',max_length=64,unique=True,)
    brief = models.CharField('简介',null=True,blank=True,max_length=255,)
    set_as_top = models.BooleanField(default=False) #是否在首页显示的标签
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField('UserProfile',blank=True)

    def __str__(self):
        return '%s' % (self.name)

#用户
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.TextField('个人介绍',null=True,blank=True,)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True,upload_to='statics/images/uploads')#从filefield会验证是否为图片文件,可以设置图像大小
    def __str__(self):
        return '%s' % (self.name)

