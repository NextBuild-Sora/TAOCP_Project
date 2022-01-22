
# 客户端

import  urllib.request

url = "http://127.0.0.1:5000"
p = "广东省"
c = "深圳市"

p = urllib.parse.quote(p)
c = urllib.parse.quote(c)
#print(p, c)
data = "provice=" + p + "&city=" + c
resp = urllib.request.urlopen(url + "?" + data)     #向服务器发送数据
data = resp.read()  #服务器返回数据
html = data.decode()    #编码转换（解/转码）
print(html)
