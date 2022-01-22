
#客户端


import  urllib.request

url = "http://127.0.0.1:5000"
p = "广东"
c = '深圳'
n = "深圳依山傍海，气候宜人，实在是适合。。。。"

p = urllib.parse.quote(p)
c = urllib.parse.quote(c)
n = urllib.parse.quote(n)
pc = "province=" + p + "&city=" + c + "&note=" + n

resp = urllib.request.urlopen(url, data=pc.encode())
data = resp.read()
html = data.decode()
print(html)

