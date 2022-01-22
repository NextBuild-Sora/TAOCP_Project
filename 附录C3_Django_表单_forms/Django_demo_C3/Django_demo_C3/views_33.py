
#附录C3 Django 表单 forms
# 3.3 表单 checkbox


from django.shortcuts import render
from .form_33 import LoginForm
# from Django_demo_C3.form_33 import BookForm


def show(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        python = request.POST.get("python")
        php = request.POST.get("php")
    else:
        form = LoginForm()
    
    return render(request, "show_33.html", locals())




