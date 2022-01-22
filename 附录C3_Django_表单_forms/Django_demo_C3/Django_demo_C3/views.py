
#附录C3 Django 表单 forms
# 3.1 表单 text password


from django.shortcuts import render
# from Django_demo_C3.form import LoginForm
from .form import LoginForm


def show(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  #维持原来的值
        user = request.POST.get("user")
        password = request.POST.get("password")

    else:
        form = LoginForm()  #这是空值
    return render(request, "show.html", locals())




