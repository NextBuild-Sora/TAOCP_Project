
"""Django_demo_C4 URL Configuration

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


import django
from django.contrib import admin

from django.urls import path

from django.conf.urls import url
# from . import views_41
# from . import views_412
# from . import views_42
# from . import views_421
# from . import views_43
# from . import views_431

from person import views_44      #Django 4.4 模块 综合实训


urlpatterns = [
    # path('admin/', admin.site.urls),

    #Django 4.1 模块 显示数据
    # url(r"^$", views_41.show),
    # url(r"^$", views_412.show),

    #Django 4.2 模块 操作数据
    # url(r'^$', views_42.show),
    # url(r'^$', views_421.show),


    #Django 4.3 模块 管理数据
    # url(r'^$', views_43.show),
    # url(r'^$', views_431.show),
    
    
    # Django 4.4 模块 综合实训
    url(r'^$', views_44.show),
    url(r'^insert$', views_44.insert),
    url(r'^update$', views_44.update)


]
