
#Django 4.2 模块 操作数据 



from django.shortcuts import render
from person.models import PersonModel
# from .models import PersonModel



def show(request):
    #删除 Name = "B"
    # PersonModel.objects.filter(Name= "B").delete()

    PersonModel.objects.filter(Sex= "男")   #过滤；类似于：select * from ... whers Sex="女"

    PersonModel.objects.filter(Sex= "男").update(Age= 18)   #修改（更新数据）


    # persons = PersonModel.objects.all()   #显示（获取数据）全部

    return render(request, "show_411.html", locals())




