# _*_ coding: utf-8 _*_

from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.signin),
]