#############################################
#
# 创建网站服务器
# 创建一个服务器用来展示 phone.html 网页
#
##############################################


import flask

app=flask.Flask(__name__, static_folder="images")
@app.route("/")
def show():
    return flask.render_template("phone.html")
app.run()


