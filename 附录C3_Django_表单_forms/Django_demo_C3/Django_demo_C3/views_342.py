
#附录C3 Django 表单 forms
# 3.4.2 表单 select


from django.shortcuts import render
from .form_341 import UserForm
# from Django_demo_C3.form_341 import BookForm


def getClassList():
    cList = []

    f = open("D:/ProgramData/PyCharm_Community_Edition/"
    "PyCharm-Community-2020/Python网络爬虫程序技术/"
    "附录C3_Django_表单_forms/Django_demo_C3/classList.txt", \
    "rt", encoding= "utf-8")

    # f = open("classList.txt", "rt", encoding= "utf-8")
    rows = f.readlines()
    for row in rows:
        s = row.strip()
        if s != "":
            cList.append( [s, s])
    f.close()

    return cList
    

def show(request):
    cList = getClassList()

    if request.method == "POST":
        form = UserForm(request.POST)      #维持选择的值。
        # sclass = request.POST.get("sclass")   #获得值。
        sclass = request.POST.getlist("sclass")   #获得多个值。
        msg = sclass
        
    else:
        form = UserForm()
        msg = ""
    form.fields["sclass"].choices = cList
    
    return render(request, "show_342.html", locals())




