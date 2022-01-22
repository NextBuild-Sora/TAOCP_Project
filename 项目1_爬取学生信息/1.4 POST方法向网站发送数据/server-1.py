
#服务器
#-GET，POST 混合


import  flask

app = flask.Flask(__name__)
@app.route("/", methods = ['GET','POST'])
def index():
    try:
        p = flask.request.args.get("province")  #GET方式
        c = flask.request.args.get("city")  #GET方式
        n = flask.request.form.get("note")  #POST
        '''    
        p = flask.request.values.get("province")  #统一方式
        c = flask.request.values.get("city")  #统一方式
        n = flask.request.values.get("note")  #统一
        '''
        print(p)
        print(c)
        print(n)
        return p + "\n" + c + "\n" + n
    except Exception as err:
        print(err)
app.run()


