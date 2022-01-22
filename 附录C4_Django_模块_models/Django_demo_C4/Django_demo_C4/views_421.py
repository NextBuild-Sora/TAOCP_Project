
#Django 4.2.1 模块 操作数据 



from django.shortcuts import render

from person.models import PersonModel
# from .models import PersonModel

from Django_demo_C4.forms_421 import PersonForm
# from .forms_421 import PersonForm




def show(request):
    form = PersonForm()
    persons = PersonModel.objects.all()   #显示（获取数据）全部

    return render(request, "show_421.html", locals())




