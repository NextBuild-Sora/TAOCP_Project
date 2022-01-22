
#附录C3 Django 表单 forms
# 3.7.1 表单 综合实训



from os import error
import sqlite3
from django.shortcuts import render
from .form_371 import UserForm
# from Django_demo_C3.form_371 import RegisterForm


def verify(user, pwd, con_pwd, email, tel):
    errors = []
    if user == "":
        errors.append("用户不能空")
    if pwd == "" or con_pwd == "" or pwd != con_pwd:
        errors.append("密码不能空；两个密码必须一致")
    if email != "":
        p = email.find("@")
        if p == -1 or p == 0 or p ==len(email)-1:
            errors.append("Email格式不正确")    
    if tel != "":
        count = 0
        for t in tel:
            if t>="0" and t<="9":
                count = count + 1
        if count != 11 or len(tel) != 11:
            errors.append("手机号码必须是11位长数字")
    return errors

# 数据库 ( 注册账号 )
def registerUser(user, pwd, email, tel):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    sql = "create table users (user varchar(8) primary key, pwd varchar(8), email varchar(64), tel varchar(11))"
    try:
        cursor.execute(sql)
    except:
        pass
    sql = "insert into users (user, pwd, email, tel) values (?,?,?,?)"
    msg = "注册成功"
    try:
        cursor.execute(sql, [user, pwd, email, tel])
    except:
        msg = "注册失败"
    con.commit()
    con.close()
    return msg 

# 登录用户
def loginUser(user, pwd):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    sql = "select * from users where user=? and pwd=?"
    cursor.execute(sql, [user, pwd])
    row = cursor.fetchone()
    if row:
        msg = "登陆成功"
    else:
        msg = "登陆失败"
    # con.commit()
    con.close()
    return msg 



#注册 Register.
def show(request):
    msg = ""
    if request.method == "POST":
        form = UserForm(request.POST)      #维持选择的值。
        user = request.POST.get("user", "").strip()
        pwd = request.POST.get("pwd", "").strip()
        con_pwd = request.POST.get("con_pwd", "").strip()
        tel = request.POST.get("tel", "").strip()
        email = request.POST.get("email", "").strip()
        errors = verify(user, pwd, con_pwd, email, tel)
        if not errors:
            #验证通过
            msg = registerUser(user, pwd, email, tel)

    else:
        form = UserForm()
        errors = []
    return render(request, "show_371.html", locals())


#登录
def login(request):
    msg = ""
    if request.method == "POST":
        form = UserForm(request.POST)      #维持选择的值。
        user = request.POST.get("user", "").strip()
        pwd = request.POST.get("pwd", "").strip()
        msg = loginUser(user, pwd)
    else:
        form = UserForm()
        # errors = []

    return render(request, "login_371.html", locals())



