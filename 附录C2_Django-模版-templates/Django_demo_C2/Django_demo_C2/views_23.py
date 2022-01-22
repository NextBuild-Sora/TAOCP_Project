# 附录C2_Django-模版-templates.
#Django 2.3 模版 条件参数


from typing import AsyncGenerator
from django.shortcuts import render

# def index(request):
#     age = 14
#     return render(request, "show_23.html", locals())

def index(request):
    st = []
    st.append({"name":"A", "sex":"M"})
    st.append({"name":"B", "sex":"F"})
    return render(request, "show_23.html", locals())

