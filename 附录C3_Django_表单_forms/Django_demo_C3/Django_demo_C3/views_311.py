
#附录C3 Django 表单 forms
# 3.1.1 表单 text password


from django.shortcuts import render
from .forms_311 import BookForm
# from Django_demo_C3.forms import BookForm


def show(request):
    form = BookForm()
    
    return render(request, "book.html", locals())




