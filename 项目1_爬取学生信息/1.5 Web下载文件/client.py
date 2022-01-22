

# 客户端


import urllib.request

url="http://127.0.0.1:5000"

resp=urllib.request.urlopen(url)
data = resp.read()
fileName=data.decode()
#print (fileName)
resp = urllib.request.urlopen(url + "?fileName=" + urllib.parse.quote(fileName))    #客户端请求打开连接；中文名称进行转码
data=resp.read()    #读取
f=open("download" + fileName, "wb")     #下载
f.write(data)   #写入
f.close()   #关闭
print(fileName , len(data))     #打印文件大小
