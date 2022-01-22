
#附录C3 Django 表单 forms
# 3.6 表单 数据验证


from django.shortcuts import render
from .form_36 import LoginForm
# from Django_demo_C3.form_36 import LoginForm
    

def show(request):

    if request.method == "POST":
        form = LoginForm(request.POST)      #维持选择的值。
        if form.is_valid:    #如果form是有效的。
            name = request.POST.get("name", "")
            sex = request.POST.get("sex", "")
            age = request.POST.get("age", "")
        else:   
            errors = form.errors    #给出表单的错误。     
    else:
        form = LoginForm()
    
    return render(request, "show_36.html", locals())




