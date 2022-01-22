
# ---- 学生管理服务器程序 ---- #

"""
    学生的记录包括学号No、姓名Name、性别Sex与年龄Age，服务
器的作用是建立与维护一个Sqllite的学生数据库students.db中的

    学生记录表students：
create table students (No varchar(16) primary key,Name
varchar(16), Sex varchar(8), Age int)

    服务器建立一个Web网站，同时提供查询学生记录、增加学生记
录、删除学生记录等接口服务.

"""


import flask
import sqlite3
import json

app = flask.Flask(__name__)

class StudentDB:
    def openDB(self):
        self.con = sqlite3.connect("students.db")
        self.cursor = self.con.cursor()

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def initTable(self):    #初始化表格
        res = {}
        try:
            self.cursor.execute( "create table students(NO varchar(16) primary key, Name varchar(16), Sex varchar(8), Age int)" )
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = str(err)
        return  res

    def insertRow(self, No, Name, Sex, Age):    #插入信息
        res = {}
        try:
            self.cursor.execute("insert into students (No,Name,Sex,Age) values(?, ?, ?, ?)", (No,Name,Sex,Age))
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = str(err)
        return res

    def deleteRow(self, No):    #删除一条学生记录
        res ={}
        try:
            self.cursor.execute("delete from students where No=?", (No,))
            res["msg"] = "OK"
        except Exception as err:
            res["msg"] = 'OK'
        return res

    def selectRows(self):   #获取所有的学生
        res = {}
        try:
            data = []
            self.cursor.execute("select * from students order by No")
            rows = self.cursor.fetchall()
            for row in rows:
                d = {}
                d['NO']=row[0]
                d['Name']=row[1]
                d['Sex']=row[2]
                d['Age']=row[3]
                data.append(d)
            res['msg']='OK'
            res['data']=data
        except Exception as err:
            res['msg']= str(err)
        return res

    @app.route('/', methods=['GET','POST'])
    def process( ):
        opt = flask.request.values.get('opt') if 'opt' in flask.request.values else ""
        res={}
        db = StudentDB()
        db.openDB()
        if opt == 'init':
            res = db.initTable()
        elif opt == 'insert':
            No = flask.request.values.get('No') if 'No' in flask.request.values else ""
            Name = flask.request.values.get('Name') if 'Name' in flask.request.values else ""
            Sex = flask.request.values.get('Sex') if 'Sex' in flask.request.values else ""
            Age = flask.request.values.get('Age') if 'Age' in flask.request.values else ""
            res = db.insertRow(No, Name, Sex, Age)
        elif opt == 'delete':
            No = flask.request.values.get("No") if "No" in flask.request.values else ""
            res = db.deleteRow(No)
        else:
            res = db.selectRows()
        db.closeDB()
        return json.dumps(res)

if __name__ == "__main__":
    app.run()


