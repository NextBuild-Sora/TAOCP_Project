
# ---- 客户端GET方式发送数据 ---- #
# -第一部分

'''
    ==GET方式发送使得数据附加在URL后面，在URL后面先接一个"?"号，数据采用：
"名称1=值1&名称2=值2&名称3=值3……"的方式，多个数据之间用"&"符号隔开，
例如向服务器传递省份与城市的数据就可以这样写：
urllib.request.urlopen("http://127.0.0.1:5000?province=GD&ci
ty=SZ")

    ==如果参数值包含汉字，那么我们必须使用urllib.parse.quote对参数值进行编码，
    例如：
province= urllib.parse.qoute("广东")
city= urllib.parse.qoute("深圳")
urllib.request.urlopen("http://127.0.0.1:5000?province="+pro
vince+"&city="+city)

'''

import urllib.parse
import urllib.request

url = "http://127.0.0.1:5000"

try:
    proince = urllib.pares.quote("广东")
    city = urllib.pares.quote("深圳")
    data = "proince=" + proince + "&city=" + city
    html = urllib.rquest.urlopen("http://127.0.0.1:5000?" + data )
    html = html.read()
    html = html.decode()
    print (html)
except Exception as err:
    print(err)

