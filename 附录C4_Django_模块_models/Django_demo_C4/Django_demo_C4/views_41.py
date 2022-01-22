
#Django 4.1 模块 显示数据


from django.shortcuts import render
from person.models import PersonModel
# from .models import PersonModel



def show(request):
    # PersonModel.objects.create(Name="A", Sex="男", Age= 20)    #出错：int属性错误。
    # PersonModel.objects.create(Name="B", Sex="女", Age= 21)    #出错：int属性错误。

    PersonModel.objects.create(Name= "A", Sex= "男", Age= '20')
    PersonModel.objects.create(Name= "B", Sex= "女", Age= '21')

    return render(request, "show_41.html", locals())




