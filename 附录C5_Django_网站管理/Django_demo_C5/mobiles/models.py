from django.db import models

# Create your models here.


#Django 5.4 网站 综合实训


class Product(models.Model):
    model = models.CharField(max_length= 128, blank= False, verbose_name= "型号")
    maker = models.CharField(max_length= 128, blank= False, verbose_name= "制造商" )
    year = models.PositiveIntegerField(blank= False)
    price = models.PositiveIntegerField(default= 0, verbose_name= "价格")
    qty = models.PositiveIntegerField(default= 1, verbose_name= "数量")
    desp = models.PositiveIntegerField(default= 128, verbose_name= "简介")

class User(models.Model):
    name = models.CharField(max_length= 128, primary_key= True)
    password = models.CharField(max_length= 128, primary_key= False)
    
