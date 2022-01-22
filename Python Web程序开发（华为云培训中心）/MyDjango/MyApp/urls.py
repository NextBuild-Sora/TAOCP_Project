from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.hello),
    url(r'^func$', views.func)

]
