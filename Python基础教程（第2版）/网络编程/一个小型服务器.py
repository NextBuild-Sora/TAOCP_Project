
# --- 一个小型服务器 ---- #

import socket

s = socket.socket()

host = socket.gethostname()         #获得当前主机名
port = 1024     #端口号
s.bind( (host, port) )      #绑定连接地址

s.listen(5)     #监听；可以接受客户端的连接
while True:
    c, addr = s.accept()    #阻塞；等待接受客户端的连接
    print ("Got connerction from", addr)
    c.send("Thank you for connectiong")     #发送数据
    c.close()       #关闭


