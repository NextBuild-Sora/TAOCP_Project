
# 1 实现简单的UDP客户端通信程序
# ---客户端---


from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

dest_addr = ('127.0.0.1', 2233)
udp_socket.sendto("你好".encode("utf8"), dest_addr)
udp_socket.sendto("你好".encode("utf8"), dest_addr)
udp_socket.close()

