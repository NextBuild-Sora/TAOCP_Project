# 附录C2_Django-模版-templates.
#Django 2.4.2 常用表单元素



from django.shortcuts import render

#checkbox 单选元素
"""
def index(request):
    python = ""
    php = ""
    msg = ""
    if request.method == "POST":
        python = request.POST.get("python", "")
        php = request.POST.get("php", "")
        msg = python + ", " + php
    return render(request, "show_242.html", locals())
"""

#checkbox 多选元素
def index(request):
    msg = ""
    courses = []
    if request.method == "POST":
        courses = request.POST.getlist("courses")
        for c in courses:
            msg = msg + c + "  "
    return render(request, "show_242.html", locals())

