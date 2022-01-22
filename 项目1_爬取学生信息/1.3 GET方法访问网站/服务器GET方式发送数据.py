
# ---- 服务器GET方式发送数据 ---- #
# -第二部分

"""
    ==服务器用Flask中的request对象的args来存储GET的参数，用get方
法来获取参数，即用flask.request.args.get(参数)来获取参数的值，
例如：
province=flask.request.args.get("province")
city=flask.request.args.get("city")

就可以获取GET传递的参数province与city的值。

编写服务器程序server.py如下：
"""


import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    try:
        province = flask.request.args.get("province")
        city = flask.request.args.get("city")
        return province + "," + city
    except Exception as err:
        return str(err)

if __name__ == "__main__":
    app.run()


"""
    ==先运行server.py建立web网站，再运行client.py，可以看到client.py的结果是：
广东,深圳

注意web网址是http://127.0.0.1:5000，如果我们直接访问这个网站会有错误，因为
没有提供province与city参数，服务器执行：
province=flask.request.args.get("province")
city = flask.request.args.get("city")

语句时会到args中查找province,city参数的值，结果没有找到而出现错误。为了避免
这种错误可以把这两语句写成如下：
province = flask.request.args.get("province") if "province" in flask.request.args else ""
city = flask.request.args.get("city") if "city" in flask.request.args else ""

这样在"province"、"city"没有出现在flask.request.args中时province、city值就设置
为空字符串。

"""

