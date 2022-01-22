from django.contrib import admin
from person_53.models import PersonModel

# Register your models here.

#Django 5.3 超级管理员用户
admin.site.register(PersonModel)

