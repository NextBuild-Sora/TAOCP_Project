
#######################################################################
# Create your models here.

"""
#Django 4.1 模块 显示数据


from django.db import models


#这条语句（类）类似于 create 创建一张表格。
class PersonModel(models.Model):
    Name = models.CharField(max_length= 8, primary_key= True)
    Sex = models.CharField(max_length= 2)
    Age = models.ImageField()
"""
#######################################################################



#***********************************************************************************#
# Create your models here.

#Django 4.4 模块 综合实训


from django.db import models


#这条语句（类）类似于 create 创建一张表格。
class PersonModel(models.Model):
    pName = models.CharField(max_length= 128, primary_key= True, null= False)
    pSex = models.CharField(max_length= 8, null= False)
    pAge = models.ImageField()
    pTel = models.CharField(max_length= 128, null= True)

    
#***********************************************************************************#


