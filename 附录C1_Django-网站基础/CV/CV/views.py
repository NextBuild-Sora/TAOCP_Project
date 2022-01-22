
#(5) 编写 demo/views.py

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# def index(request):
    # return render(request, "index.html")

#拓展练习: 把 views.py 改写成下面这样，
# 试问网站能否工作？为什么？
def index(request):
    f = open("templates/index.html", "rt", encoding="utf-8")
    data = f.read()
    f.close()
    return HttpResponse(data)


