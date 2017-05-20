# _*_ coding: utf-8 _*_
from django.conf.urls import url
from webchat import views

urlpatterns = [
    url(r'^$', views.chat,name='chat'),
    url(r'^send_msg/$', views.send_msg,name='send_msg'),
]