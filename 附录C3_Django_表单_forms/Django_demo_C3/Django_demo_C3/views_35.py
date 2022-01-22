
#附录C3 Django 表单 forms
# 3.5 表单 textarea     多行表单


from django.shortcuts import render
from .form_35 import LoginForm
# from Django_demo_C3.form_35 import BookForm

    

def show(request):

    if request.method == "POST":
        form = LoginForm(request.POST)      #维持选择的值。
        note = request.POST.get("note")

        
    else:
        form = LoginForm()
    
    return render(request, "show_35.html", locals())




