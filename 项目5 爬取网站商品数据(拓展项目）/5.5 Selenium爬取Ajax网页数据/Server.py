#**********************************************
# 5.5 Selenium 爬取 Ajax 网页数据
# 2、创建服务器程序
#**********************************************


import flask
import json

app=flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("phone.html")

@app.route("/phones")
def getPhones():
    mark = flask.request.values.get("mark")
    phones = []
    if mark == "华为":
        phones.append({"model":"华为 Mate40", "mark":"华为", "price":4999})
        phones.append({"model":"华为 P40", "mark":"华为", "price":4488})
    elif mark == "苹果":
        phones.append({"model":"iPhone SE", "mark":"苹果", "price":3299})
        phones.append({"model":"iPhone 12", "mark":"苹果", "price":5499})
    elif mark == "三星":
        phones.append({"model":"三星 Galaxy S21", "price":5999})
    s = json.dumps({"phones": phones})
    return s

if __name__ == "__main__":
    app.run()


