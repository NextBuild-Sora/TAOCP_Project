
#附录C3 Django 表单 forms
# 3.2.1 表单 radio


from django.shortcuts import render
from .form_321 import LoginForm
# from Django_demo_C3.form_321 import BookForm


def show(request):
    form = LoginForm()
    
    return render(request, "book_321.html", locals())




