
#服务器


import  flask

app = flask.Flask(__name__)
@app.route("/", methods = ['POST'])
def index():
    try:
        p = flask.request.form.get("province")
        c = flask.request.form.get("city")
        n = flask.request.form.get("note")
        print(p)
        print(c)
        print(n)
        return p + "\n" + c + "\n" + n
    except Exception as err:
        print(err)
app.run()














