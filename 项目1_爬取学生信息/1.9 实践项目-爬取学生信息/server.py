
# 服务器程序
"""
    设计一个 Web服务器server.py，它读取students.txt文件中
的学生数据，以表格的形式呈现在网页上.
"""

from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def shouw():
    if os.path.exists("students.txt"):
        st = "<h3>学生信息表</h3>"
        st = st + "<table border='1' width='300'>"
        fobj = open("students.txt", "rt", encoding="utf-8")
        while True:
            #读取一行，去除行尾部"\n"换行符号
            s = fobj.readline().strip("\n")
            #如果读到文件尾部就退出
            if s == "":
                break
            #按逗号拆分开
            s = s.split(",")
            st = st + "<tr>"
            #把各个数据组织在<td>...</td>的单元中
            for i in range(len(s)):
                st = st + "<td>" + s[i] + "</td>"
            #完成一行
            st = st + "</tr>"
        fobj.close()
        st = st + "</table>"
        return st

if __name__ == "__main__":
    app.run()


