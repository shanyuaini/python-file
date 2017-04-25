# _*_ coding: utf-8 _*_

from django.forms import ModelForm
from bbs import models
#记得在models里from bbs import article_forms注册一下这个模块

class ArticleModelForm(ModelForm):
    class Meta:
        model = models.Article
        #exclude = ('author','pub_date','priority')
        exclude = ('author','pub_date','priority')
        # 为发帖做一个modelform,关联models中的Article表

    def __init__(self,*args,**kwargs):
        super(ArticleModelForm,self).__init__(*args,**kwargs)
        #继承自己
        #self.fields['title'].widget.attr['class'] = 'form-control'
        #为单个字段加样式
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class' : 'form-control'})

        #为所有字段改样式




