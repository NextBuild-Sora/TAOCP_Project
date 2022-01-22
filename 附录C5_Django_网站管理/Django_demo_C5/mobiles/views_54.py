
#Django 5.4 网站 综合实训


from django.shortcuts import render
from mobiles import models
from mobiles import forms
from django.http import HttpResponseRedirect



def initUser():
    user=models.User(name="admin",password="123")
    user.save()

def index(request):
    request.session["logined"]=""
    initUser()
    phones=models.Product.objects.all()
    return render(request,"index_54.html",locals())

def show(request):
    if request.session.get("logined","")=="":
        return HttpResponseRedirect("/")
    id=request.GET.get("id","")
    if id!="":
        models.Product.objects.filter(id=id).delete()
    phones=models.Product.objects.all()

def addPhone(request):
    if request.session.get("logined","")=="":
        return HttpResponseRedirect("/")
    msg=""
    if request.method=="POST":
        form=forms.ProductForm(request.POST)
        if form.is_valid:
            model=request.POST.get("model","")
            maker = request.POST.get("maker", "")
            year = request.POST.get("year", "")
            price = request.POST.get("price", "")
            qty = request.POST.get("qty", "")
            desp = request.POST.get("desp", "")
            if year=="":
                year="0"
            if price=="":
                price="0"
            if qty=="":
                qty="0"
            product=models.Product(model=model,maker=maker,year=int(year),price=int(price),qty=int(qty),desp=desp)
            product.save()
            msg="增加成功"
        else:
            msg="增加失败"
    else:
        form=forms.ProductForm()
    return render(request,"addPhone_54.html",locals())

def editPhone(request):
    if request.session.get("logined","")=="":
        return HttpResponseRedirect("/")
    msg=""
    if request.method=="POST":
        form=forms.ProductForm(request.POST)
        if form.is_valid:
            model=request.POST.get("model","")
            maker = request.POST.get("maker", "")
            year = request.POST.get("year", "")
            price = request.POST.get("price", "")
            qty = request.POST.get("qty", "")
            desp = request.POST.get("desp", "")
            if year=="":
                year="0"
            if price=="":
                price="0"
            if qty=="":
                qty="0"
            id=request.POST.get("id","")
            models.Product.objects.filter(id=id).update(model=model,maker=maker,year=int(year),price=int(price),qty=int(qty),desp=desp)
            msg="更新成功"
        else:
            msg="更新失败"
    else:
        try:
            id=request.GET.get("id","")
            p=models.Product.objects.get(id=id)
            d={"model":p.model,"maker":p.maker,"year":p.year,"price":p.
            price,"qty":p.qty,"desp":p.desp}
            form = forms.ProductForm(d)
        except:
            form=forms.ProductForm()
        return render(request,"editPhone_54.html",locals())

def login(request):
    request.session["logined"]=""
    msg=""
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        name=request.POST.get("name","")
        password = request.POST.get("password", "")
        user=models.User.objects.filter(name=name,password=password)
        if user:
            request.session["logined"]="OK"
            return HttpResponseRedirect("/show")
        else:
            msg="登录失败"        
    else:
        form=forms.LoginForm()
    return render(request,"login_54.html",locals())




