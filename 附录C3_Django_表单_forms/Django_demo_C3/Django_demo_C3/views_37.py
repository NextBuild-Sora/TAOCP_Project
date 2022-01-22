
#附录C3 Django 表单 forms
# 3.7 表单 综合实训




import sqlite3
from django.shortcuts import render
from .form_37 import RegisterForm
# from Django_demo_C3.form_37 import RegisterForm



class UserDB:
    def initialize(self):
        try:
            self.cursor.execute("drop table users")
        except:
            pass
        self.cursor.execute("create table users (user varchar(16) primary key,pwd varchar(16),sex varchar(16),age int,tel varchar(16),email varchar(64))")
    
    def open(self):
        self.con= sqlite3.connect("users.db")
        self.cursor= self.con.cursor()
        #self.initialize()
    
    def close(self):
        self.con.commit()
        self.con.close()

    def insert(self,user,pwd,sex,age,tel,email):
        flag=True
        try:
            sql="insert into users (user,pwd,sex,age,tel,email) values(?,?,?,?,?,?)"
            self.cursor.execute(sql,[user,pwd,sex,age,tel,email])
        except Exception as err:
            print("插入错误：", err)
            flag=False
        return flag


def show(request):
    msg = ""

    if request.method == "POST":
        form = RegisterForm(request.POST)      #维持选择的值。
        if (form.is_valid):    #如果form是有效的。
            user = request.POST.get("user")
            sex = request.POST.get("sex")
            age = request.POST.get("age", "0")
            age = int(age)
            pwd = request.POST.get("pwd")
            tel = request.POST.get("tel")
            email = request.POST.get("email")
            DB = UserDB()
            DB.open()
            if (DB.insert(user, pwd, sex, age, tel, email)):
                msg = "注册成功"
            else:
                msg = "注册失败"
            DB.close()
        
    else:
        form = RegisterForm()
    return render(request, "show_37.html", locals())




