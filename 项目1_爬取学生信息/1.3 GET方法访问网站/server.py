#服务端

import  flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    p = flask.request.args.get("provice")   #获取客户端传给服务器的参数值
    c = flask.request.args.get("city")
    print(p, c)     #打印服务器收到的
    return p + "," + c  #返回给客户端
app.run()


