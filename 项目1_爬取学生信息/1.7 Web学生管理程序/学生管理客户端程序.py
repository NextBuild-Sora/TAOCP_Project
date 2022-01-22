

# ---- 学生管理客户端程序 ---- #


import urllib.request
import json

class Student:
    def __init__(self, No, Name, Sex, Age):
        self.No = No
        self.Name = Name
        self.Sex = Sex
        self.Age = Age

    def show(self):
        print("%-16s %-16s %-8s %-4d" % (self.No, self.Name, self.Sex, self.Age))

students = []
url = "http://127.0.0.1:5000"

def listStudents():
    global  students
    print( "%-16s %-16s %-8s %-4d" % ('No', 'Name', 'Sex', 'Age') )
    for s in students:
        s.show()

def insertStudent(s):
    global students
    i = 0
    while (i < len(students) and s.No > students[i].No):
        i = i + 1
    if (i < len(students) and s.No == students[i].No):
        print(s.No + '已经存在')
        return False
    students.insert(i, s)
    return True

def deleteRow():
    global students
    No = input("No= ")
    if (No != ""):
        for i in range(len(students)):
            if (students[i].No == No):
                st = ""
                try:
                    st = "No= " + urllib.request.quote(No)
                    st = st.encode()
                    content = urllib.request.urlopen(url + "?opt=delete" , st)
                    st = content.readline()
                    st = json.loads(st.decode())
                    st = st['msg']
                except Exception as exp:
                    st = str(exp)

                if (st == 'OK'):
                    del students[i]
                    print("删除成功")
                else:
                    print(st)
                break

def insertRow():
    No = input("No= ")
    Name = input("Name= ")
    while True:
        Sex = input("Sex= ")
        if (Sex == '男' or Sex == '女'):
            break
        else:
            print("性别无效；只能输入：男或女！")
    Age = input("Age= ")
    if (Age == ""):
        Age = 0
    else:
        Age = int(Age)
    if No != "" and Name !="":
        s = Student(No, Name, Sex, Age)
        for x in students:
            if (x.No == No):
                print(No + " 已经存在")
                return
        st = ""
        try:
            st = "No="+urllib.request.quote(No) + "&Name="+urllib.request.quote(Name) + "&Sex="+urllib.request.quote(Sex) + "&Age="+str(Age)
            st = st.encode()
            content = urllib.request.urlopen(url + "?opt=insert", st)
            st = content.read()
            st = json.loads(st.decode())
            st = st["msg"]
        except Exception as exp:
            st = str(exp)

        if (st == "OK"):
            insertStudent(s)
            print("增加成功")
        else:
            print(st)
    else:
        print("学号、姓名不能为空")

def initialize():
    st = ""
    try:
        content = urllib.request.urlopen(url + "?opt=init")
        st = content.read()
        st = json.loads(st.decode)
        st = st['msg']
    except Exception as exp:
        st = str(exp)

    if (st == "OK"):
        print("初始成功")
    else:
        print(st)
    return st

def readStudents():
    global students
    try:
        students.clear()
        content = urllib.request.urlopen(url)
        data = b""
        while True:
            buf = content.read(1024)
            if (len(buf) > 0):
                data = data + buf
            else:
                break
        data = data.decode()
        data = json.loads(data)
        if data['msg'] == 'OK':
            data = data["data"]
            for d in data:
                # 每个人都是一本字典
                s = Student(d["No"], d["Name"], d["Sex"], d["Age"])
                students.append(s)
    except Exception as exp:
        print(exp)

try:
    readStudents()

    while True:
        print("")
        print("***学生名单***")
        print("0. 初始化学生表")
        print("1. 查看学生列表")
        print("2. 增加学生记录")
        print("3. 删除学生记录")
        print("4. 退出这个程序")
        s = input("请选择(0,1,2,3,4): ")
        if (s == "0"):
            initialize()
        elif (s == "1"):
            listStudents()
        elif (s == "2"):
            insertRow()
        elif (s == "3"):
            deleteRow()
        elif (s == "4"):
            break
except Exception as exp:
    print("错误信息：", exp)


