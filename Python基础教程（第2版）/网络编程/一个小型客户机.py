
# ---- 一个小型客户机 ---- #


import socket

s = socket.socket()

host = socket.gethostname()     #获得主机名
port = 1024     #端口号

s.connect( (host, port) )   #连接一个地址
print ( s.recv(1024) )  #打印接受最大（1024）字节数的数据

