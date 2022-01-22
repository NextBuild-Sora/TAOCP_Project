
#附录C3 Django 表单 forms
# 3.3.1 表单 checkbox


from django.shortcuts import render
from .form_331 import LoginForm
# from Django_demo_C3.form_33 import BookForm


def show(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        courses = request.POST.getlist("courses")   #获得列表形式。
        s = " "
        for c in courses:
            s = s + c + " "

    else:
        form = LoginForm()
    
    return render(request, "show_331.html", locals())




