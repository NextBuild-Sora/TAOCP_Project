from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def hello(request):
    return render(request, "PYC01-HTML_JS_Demo.html")

