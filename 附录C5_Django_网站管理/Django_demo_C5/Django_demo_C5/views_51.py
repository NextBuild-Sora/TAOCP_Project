
## 5.1 Session 用户登录


from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect 


def login(request):
    msg = ""
    request.session["logined"] = ""
    if request.method == "POST":
        uname = request.POST.get("uname", "")
        upass = request.POST.get("upass", "")
        if (uname == "xxx" and upass == "123"):
            request.session["loginde"] = "OK"
            # resp = HttpResponseRedirect("/home")
            # resp.set_cookie("logined", "OK")
            # return resp
            return HttpResponseRedirect("home")
        else:
            msg = "wrong name or password"
        # request.session["logined"] = ""
        return render(request, "login.html", {"msg":msg})

def home(request):
    logined = request.session.get("logined", "")
    if logined != "OK":
        return HttpResponseRedirect("/")
    
    # s = "<h3>Home Page</h3><a href='/'>Logout</a>"
    s = "<h3>Home Page</h3><div>It is secret</div><a href='/'>Logout</a>" + logined   #安全页面
    return HttpResponse(s)




