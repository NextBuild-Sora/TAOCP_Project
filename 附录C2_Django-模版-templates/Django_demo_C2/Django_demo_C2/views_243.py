# 附录C2_Django-模版-templates.
#Django 2.4.3 常用表单元素



from django.shortcuts import render

#select 元素单选
"""
def index(request):
    msg = ""
    course = ""

    if request.method == "POST":
        course = request.POST.getlist("course")
        msg = course

    return render(request,"show_243.html", locals())
"""


# select 多选元素
# textarea 元素
def index(request):
    msg = ""
    courses = []
    if request.method == "POST":
        courses = request.POST.getlist("courses")
        for c in courses:
            msg = msg + c + "  "
    return render(request, "show_243.html", locals())



