#*******************************************
#
# 2、创建网站服务器.
#*******************************************


import flask
import json
import time

app = flask.Flask(__name__)

@app.route("/")
def index():    #(1)网站服务器在访问地址"/"时首先提交 phone.html 网页.
    return flask.render_template("phone.html")

@app.route("/marks")
def loadMarks():    #(2)网页中根据 JavaScript 代码会执行 loadPhones 函数.
    time.sleep(1)   #模拟延迟过程;延迟 1 秒后发送数据.
    marks = ["华为", "苹果", "三星"]
    return json.dumps(marks)    #再次访问服务器"/phones"时发送手机的品牌 marks 与颜色 colors数据，数据按 JSON 字符串格式发送.

app.run()

