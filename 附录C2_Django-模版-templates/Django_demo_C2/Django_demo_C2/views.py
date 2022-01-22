# 附录C2_Django-模版-templates.
#Django 2.1 简单模版参数.


from django.shortcuts import render

def index(request):
    name = "Xxx. "
    sex = "Male. "
    age = 20
    return render(request, "show.html", locals())

