
#Django 4.1.2 模块 显示数据 



from django.shortcuts import render
from person.models import PersonModel
# from .models import PersonModel



def show(request):
    
    # persons = PersonModel.objects.all(Name= "A", Sex= "男", Age= '20')
    persons = PersonModel.objects.all()

    return render(request, "show_411.html", locals())




