# 附录C2_Django-模版-templates.
#Django 2.3.2 模版 条件参数


# from typing import AsyncGenerator
from django.shortcuts import render


def index(request):
    cList = ["19-3-1","19-3-2", "20-3-4", "21-3-5"]
    size = len(cList)
    if request.method == "POST":
        # sclass = request.POST.get("sclass", "")   #一个值。
        sclass = request.POST.getlist("sclass")    #getlist获取多个值, sclass是个列表.
    else:
        # sclass = ""   #一个值
        sclass = []     #列表
    msg = sclass
    return render(request, "index.html", locals())


