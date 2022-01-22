
#附录C3 Django 表单 forms
# 3.2 表单 radio


from django.shortcuts import render
# from Django_demo_C3.form_32 import LoginForm
from .form_32 import LoginForm


def show(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  #维持原来的值
        user = request.POST.get("user")
        sex = request.POST.get("sex")

    else:
        form = LoginForm()  #这是空值
    return render(request, "show_32.html", locals())




