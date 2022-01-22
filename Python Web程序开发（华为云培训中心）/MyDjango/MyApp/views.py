# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse("Hello, World")
    return render(request, "MyApp//hello.html", context={"hi":"Hello"})

def func(request):
    L = ["flask", "django", "web.py"]
    return render(request, "MyApp//hello.html", context={"L":L})
