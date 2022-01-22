
# Django 4.3 模块 管理数据



from django.shortcuts import render

from person.models import PersonModel
# from .models import PersonModel

from Django_demo_C4.forms_421 import PersonForm
# from .forms_421 import PersonForm




def show(request):
    msg = ""

    if request.method == "POST":
        form = PersonForm(request.POST)
        Name = request.POST.get("Name", "")
        Sex = request.POST.get("Sex")
        Age = request.POST.get("Age", "0")
        
        try:
            Age = int(Age)
            PersonModel.objects.create(Name= Name, Sex= Sex, Age= Age)  #增加数据
            msg = "增加成功"
        except Exception as err:
            msg = str(err)
    else:
        form = PersonForm()
    
    # persons = PersonModel.objects.all()   #显示（获取数据）全部
    persons = PersonModel.objects.all().order_by("Name")   #按姓名排序。

    return render(request, "show_43.html", locals())




