from flask import Flask, request, jsonify, redirect, url_for
from admin import admin


app = Flask(__name__)


class Config(object):
    DEBUG = True

# 蓝图
app.register_blueprint(admin, url_prefix="/admin")

# 配置
app.config.from_object(Config)
# app.config.from_pyfile('config.ini')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 路由传递参数
@app.route('/num/<int:id>')
def num(id):
    print(type(id))
    return 'hello %s' % id

#请求方式
@app.route('/demo', methods=['GET', 'POST'])
def demo():
    return request.method

#返回json
@app.route('/func')
def func():
    json_dict = {
        "flask":1.0,
        "python":"web"
    }
    return jsonify(json_dict)

# 重定向
@app.route('/func2')    #第一种方式
def func2():
    return redirect("https://www.huawei.com")
@app.route('/func3')    #第二种方式
def func3():
    return redirect(url_for("func2"))

# hook函数使用
@app.before_first_request   #第一次请求之前调用
def before_fiest_request():
    print("第一次请求之前调用：before_first_reqiest")
@app.before_request     #每次请求前调用
def before_request():
    print("请求校验：before_request")
@app.after_request      #执行完视图函数之后会调用
def after_request(response):
    print("执行完视图函数：after_request")
    response.headers["Content-Type"] = "application/json"
    return response
@app.teardown_request       #每一次请求之后都会调用
def teardown_request(e):
    print("请求之后：teardown_request")




if __name__ == '__main__':
    app.run()
