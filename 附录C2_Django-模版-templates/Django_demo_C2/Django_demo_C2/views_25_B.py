# 附录C2_Django-模版-templates.
#2.5 模版 综合实训 学生名单


from django.shortcuts import render

def readClassList():
    clist = []
    f = open('students.txt', "rt", encoding="utf-8")
    rows = f.readlines()
    for row in rows:
        s = row.split("\t")
        if len(s) == 3:
            if s[2] not in clist:
                clist.append(s[2])
    f.close()
    return clist

def readStudentList(cName):
    slist = []
    f = open('students.txt', "rt", encoding="utf-8")
    rows = f.readlines()
    for row in rows:
        s = row.split("\t")
        if len(s) == 3:
            if s[2].strip() == cName.strip():
                slist.append({"no":s[0], "name":s[1], "cname":s[2]})
    f.close()
    return slist


def index(request):
    clist = readClassList()
    return render(request, "show_25_Classes.html", locals())

def show(request):
    cName = request.GET.get("cName", "")
    if cName:
        slist = readStudentList(cName)
    else:
        slist = []
    return render(request, "show_25_Students.html", locals())


