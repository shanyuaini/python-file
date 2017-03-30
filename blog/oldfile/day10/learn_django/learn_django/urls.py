#_*_coding:utf-8_*_

"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^host/', views.host),
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^article/(\d{4})/([0-9]{2})/(\d+)/$', views.article, {'name':'sylar'}),

#调取文章时使用年去匹配第一个(\d+{4})这样是是将这里当作一个参数year传给artcle函数,第二个为月份参数,第三个为文章id参数
#article/(?P<year>\d{4}
#这样写的意思是,将参数传入views.article函数时,函数对应的参数名也必须是year
#{'name':'sylar'}是article函数的默认参数.用来做域名转发时做cookie或session转发

]
