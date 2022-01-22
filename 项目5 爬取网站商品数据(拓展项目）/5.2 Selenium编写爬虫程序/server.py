##################
# 服务器程序
##################


import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("phone.html")

@app.route("/show")
def show():
    return "Server Message"

app.run()


