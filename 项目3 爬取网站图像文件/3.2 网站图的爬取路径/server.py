
#服务器

import flask
import os
app = flask.Flask(__name__)

def getFile(fileName):
    data = b""
    if os.path.exists(fileName):
        fobj = open(fileName, "rb")
        data = fobj.read()
        fobj.close()
    return data

@app.route("/")
def index():
    return getFile("books.html")

@app.route("/<section>")
def process(section):
    data = ""
    if section != "":
        data = getFile(section)
    return data

if __name__ == "__main__":
    app.run()


