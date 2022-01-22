# 附录C2_Django-模版-templates.
#Django 2.3.1 模版 条件参数


# from typing import AsyncGenerator
from django.shortcuts import render


def index(request):
    if request.method == "post":
        python = request.POST.get("python", "")
        mysql = request.POST.get("mysql", "")
        msg = python + " , " + mysql
    else:
        python = ""
        mysql = ""
        msg = "" 
    return render(request, "show_231.html", locals())

