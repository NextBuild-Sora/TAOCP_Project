
# 服务器

import urllib
import flask

app = flask.Flask(__name__)
@app.route("/")
def index():
    if not "fileName" in flask.request.values:
        s="图像.jpg"
        return s
    else:
        fileName=flask.request.values.get("fileName")
        f=open(fileName, "rb")
        data=f.read()
        f.close()
        return data
app.run()

