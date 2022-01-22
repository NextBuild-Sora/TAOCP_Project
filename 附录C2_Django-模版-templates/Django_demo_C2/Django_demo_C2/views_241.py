# 附录C2_Django-模版-templates.
#Django 2.4.1 常用表单元素


from django.shortcuts import render


def index(request):
    user = ""
    sex = "Male"
    if request.method == "POST":
        user = request.POST.get("sex", "Male")
        msg = sex
    return render(request, "show_241.html", locals())


