"""Django_demo_C5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.core.exceptions import ViewDoesNotExist
from django.urls import path

from django.conf.urls import url 
# from . import views_51
from . import views_52
from . import views_53
from mobiles import views_54



urlpatterns = [
    # path('admin/', admin.site.urls),


    # 5.1 Session 用户登录
    # url(r'^$', views_51.login),
    # url(r'^home/$', views_51.home),


    #Django 5.2 Cookie用户登录
    # url(r'^$', views_52.login),
    # url(r'^home/$', views_52.home),


    #Django 5.3 超级管理员用户
    # url(r'^$', views_53.show),
    # url(r'^admin/', admin.site.urls)    #管理员系统的网址
    

    #Django 5.4 网站 综合实训
    url(r'^$', views_54.index),
    url(r'^show$', views_54.show),
    url(r'^add$', views_54.addPhone),
    url(r'^edit$', views_54.editPhone),
    url(r'^login$', views_54.login),


]



