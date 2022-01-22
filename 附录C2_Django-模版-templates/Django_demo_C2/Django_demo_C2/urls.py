"""Django_demo_C2 URL Configuration

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


from django import urls
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from . import views
from . import views_22
from . import views_23
from . import views_231
from . import views_232
from . import views_24
from . import views_241
from . import views_242
from . import views_243
from . import views_25
from . import views_25_B



urlpatterns = [
    # path('admin/', admin.site.urls),
    
    #Django 2.1 简单模版参数.
    # url(r'^$', views.index),    
    
    #Django 2.2 列表模版参数
    # url(r'^$', views_22.index),
    
    #2.3 模版 条件参数
    # url(r'^$', views_23.index),
    # url(r'^$', views_231.index),    #
    # url(r'^$', views_232.index),
    
    #Django 2.4 常用表单元素
    # url(r'^$', views_24.index),
    # url(r'^$', views_241.index),
    # url(r'^$', views_242.index),
    # url(r'^$', views_243.index),

    #2.5 模版 综合实训 学生名单
    # url(r'^$', views_25.index),
    url(r'^$', views_25_B.index),
    url(r'^show$', views_25_B.show),

    
    
]
