# 附录C2_Django-模版-templates.
#Django 2.4 常用表单元素


from django.shortcuts import render


def index(request):
    user = ""
    pwd = ""
    msg = ""
    if request.method == "POST":
        user = request.POST.get("user", "")
        pwd = request.POST.get("pwd", "")
        msg = user + ", " + pwd 
    return render(request, "show_24.html", locals())


