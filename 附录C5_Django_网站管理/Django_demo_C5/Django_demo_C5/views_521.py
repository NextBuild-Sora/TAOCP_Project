
## Django 5.2 Cookie用户登录


from django.http import HttpResponse, HttpResponseRedirect, response 
from django.shortcuts import render, redirect 


def login(request):
    msg = ""
    if request.method == "POST":
        uname = request.POST.get("uname", "")
        upass = request.POST.get("upass", "")
        if (uname == "xxx" and upass == "123"):
            respone = HttpResponseRedirect("home")
            response.set_cookie("longied", "OK")
            return response
        else:
            msg = "Wrong name or password"
    response =  render(request, "login.html", {"msg":msg})
    response.set_cookie("logined", "")
    return response

def home(request): 
    log = request.COOKIES.get("logined", "")
    if log != "OK":
        response = HttpResponseRedirect("/")
        response.set_cookie("logined", "")
        return response
    
    # s = "<h3>Home Page</h3><a href='/'>Logout</a>"
    s = "<h3>Home Page</h3><div>It is secret</div><a href='/'>Logout</a>" + log   #安全页面
    return HttpResponse(s)




