#****************************************
# 服务器程序                              #
#****************************************

####################################################
#    服务器程序首先提交一个 login.html 的网页，         #
#    用户输入名称与密码后提交，                        #
#    服务器获取用户名称与密码后判断是否正确，             #
#    如果不正确就继续显示登录页面，                     #
#    如果正确就转"/show"页面显示手机记录.              #
####################################################


import flask

app = flask.Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def login():
    user = flask.request.values.get("user") if "user" in flask.request.values else ""
    pwd = flask.request.values.get("pwd") if "pwd" in flask.request.values else ""
    if user == "xxx" and pwd == "123":
        return flask.redirect("/show")  #转"/show"网页。
    else:
        return flask.render_template("login.html")

@app.route("/show", methods= ["GET", "POST"])
def show():
    s = "<table border='1'>"
    s = s+"<tr><td>品牌</td><td>型号</td><td>价格</td></tr>"
    s = s+"<tr><td>小米</td><td>小米11 8+128GB</td><td> ￥ 3999</td></tr>"
    s = s+"<tr><td>华为</td><td>Mate40 8GB+128GB</td><td> ￥ 4999</td></tr>"
    s = s+"<tr><td>苹果</td><td>iPhone12 128GB</td><td> ￥ 6799</td></tr>"
    s= s+ "</table><p>"
    s= s+ "<a href='/'>退出</a>"
    return s

app.run()

