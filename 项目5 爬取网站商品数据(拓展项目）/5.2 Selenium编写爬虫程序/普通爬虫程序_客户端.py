
# 普通爬虫程序
# 客户端
# 通过 urllib.request 直接访问"http://127.0.0.1:5000"


import urllib.request

resp=urllib.request.urlopen("http://127.0.0.1:5000")
data=resp.read()
data=data.decode()
print(data)

