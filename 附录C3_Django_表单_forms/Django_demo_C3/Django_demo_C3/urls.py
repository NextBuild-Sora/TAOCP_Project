"""Django_demo_C3 URL Configuration

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
from django.urls import path


from django.conf.urls import url
# from Django_demo_C3 import views_311

# from . import views
# from . import views_311
# # from . import views_32
# from . import views_321
# # from . import views_33
# from . import views_331
# from . import views_34
# from . import views_341
from . import views_342
from . import views_35
from . import views_36
from . import views_361
from . import views_362
from . import views_37
from . import views_371






urlpatterns = [
    # path('admin/', admin.site.urls),


    #3.1 表单 text password
    # url(r'^$', views.show),
    # url(r'^$', views_311.show),

    #3.2 表单 radio
    # url(r"^$", views_32.show),
    # url(r'^$', views_321.show),

    #3.3 表单 checkbox
    # url(r'^$', views_33.show),
    # url(r'^$', views_331.show),

    #3.4 表单 select
    # url(r'^$', views_34.show),
    # url(r'^$', views_341.show),
    # url(r'^$', views_342.show),
    # url(r'^$', views_35.show),

    #3.6 表单 数据验证
    # url(r'^$', views_36.show),
    # url(r'^$', views_361.show),
    # url(r'^$', views_362.show),

    #3.7 表单 综合实训
    # url(r'^$', views_37.show),
    url(r'^$', views_371.login),
    url(r'^register$', views_371.show),
    # url(r'^$', views_371.show),

    
    

    

]


