#_*_coding:utf-8_*_
__author__ = 'sylar'


import views

url_list = [
    (r'^/$', views.index),
    (r'^/login/$', views.login),
]