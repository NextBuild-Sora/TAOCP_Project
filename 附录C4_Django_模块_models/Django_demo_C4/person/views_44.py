
# Django 4.4 模块 综合实训




from django.shortcuts import render

from person.models import PersonModel
# from .models import PersonModel

from person.forms_44 import PersonInsertForm, PersonUpdateForm
# from .forms_44 import PersonInsertForm, PersonUpdateForm


def show(request):
    Name = request.GET.get("Name", "")
    if Name:
        try:
            PersonModel.objects.filter(pName= Name).delete()
        except:
            pass
    persons = PersonModel.objects.all()
    return render( request, "show_44.html", locals() )

def insert(request):
    if request.method == "POST":
        form = PersonInsertForm(request.POST)
        Name = request.POST.get("Name", "")
        Sex = request.POST.get("Sex")
        Age = request.POST.get("Age")
        if Age == "":
            Age = 0
        else:
            Age = int(Age)
        Tel = request.POST.get("Tel")
        try:
            PersonModel.objects.create(pName= Name, pSex= Sex, pAge= Age, pTel= Tel)
            msg = "增加成功"
        except:
            msg = "增加失败"
    else:
        form = PersonInsertForm()
    return render(request, "insert_44.html", locals())

def update(request):
    if request.method == "POST":
        form = PersonInsertForm(request.POST)
        if form.is_valid():
            Name = request.POST.get("Name")
            Sex = request.POST.get("Sex")
            Age = request.POST.get("Age")
            if Age == "":
                Age = 0
            else:
                Age = int(Age)
            Tel = request.POST.get("Tel")
            try:
                PersonModel.objects.filter(pName= Name).update( pSex= Sex, pAge= Age, pTel= Tel)
                msg = "更新成功"
            except:
                msg = "更新失败"
    else:
        Name = request.GET.get("Name", "")
        if Name:
            person = PersonModel.objects.get(pName = Name)
            data = {"Name":person.pName, "Sex":person.pSex, "Age":person.pAge, "Tel":person.pTel}
            form = PersonUpdateForm(data)
        else:
            form = PersonUpdateForm()
    return render(request, "update_44.html", locals())



