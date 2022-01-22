# 附录C2_Django-模版-templates.
#Django 2.2 列表模版参数.


from django.shortcuts import render

def index(request):
    # names = ["A", "B", "C"]     #简单列表
    
    #复杂的列表
    students = []
    students.append({"name":"A", "sex":"男", "age":20, "courses":["Java", "Python"]})
    students.append({"name":"A", "sex":"男", "age":23})
    students.append({"name":"A", "sex":"女", "age":22})
    students.append({"name":"A", "sex":"女", "age":21})
    return render(request, "show_22.html", locals())

