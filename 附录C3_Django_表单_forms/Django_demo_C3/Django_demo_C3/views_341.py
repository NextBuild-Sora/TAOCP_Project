
#附录C3 Django 表单 forms
# 3.4.1 表单 select


from django.shortcuts import render
from .form_341 import UserForm
# from Django_demo_C3.form_341 import BookForm


def show(request):
    if request.method == "POST":
        form = UserForm(request.POST)      #维持选择的值。
        # sclass = request.POST.get("sclass")   #获得值。
        sclass = request.POST.getlist("sclass")   #获得多个值。
        msg = sclass
        
    else:
        form = UserForm()
    
    return render(request, "show_341.html", locals())




