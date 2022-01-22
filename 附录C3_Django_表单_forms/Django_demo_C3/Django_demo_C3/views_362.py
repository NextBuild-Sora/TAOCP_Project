
#附录C3 Django 表单 forms
# 3.6.2 表单 数据验证


from django.shortcuts import render
from .form_361 import LoginForm
# from Django_demo_C3.form_361 import LoginForm
    

def show(request):

    if request.method == "POST":
        form = LoginForm(request.POST)      #维持选择的值。
        
        if form.is_valid():    #如果form是有效的。
            name = request.POST.get("name", "")
            sex = request.POST.get("sex", "")
            age = request.POST.get("age", "")
            msg = "OK"  #用于提示作用。
        else:   
            if "sex" in form.errors:        #性别错误。
                sexError = form.errors["sex"][0]
            if "age" in form.errors:      #年龄错误。
                ageError = form.errors["age"][0]
            msg = "Wrong"
        
    else:
        form = LoginForm()
    return render(request, "show_362.html", locals())




