
import flask

app = flask.Flask(__name__)     #这条语句是初始化一个Flask对象，参数__name__时程序的名称。

@app.route("/")     #这是一段路由控制语句，每个路由地址用"@app.route(...)"来指明，在访问相对地址是"/"时就执行函数hello()，因此访问地址http://127.0.0.1:5000时看到“你好”。
def hello():
    return "你好, Flask "

@app.route('/hi')
def hi():
    return "Hi, 你好"

if __name__ == "__main__":
    app.run()


