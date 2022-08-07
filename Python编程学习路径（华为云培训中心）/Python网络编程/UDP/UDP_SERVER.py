
# 1 实现简单的UDP客户端通信程序
# ---测试脚本---


from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)

udp_socket.bind(("127.0.0.1", 2233))

recv_data, addr = udp_socket.recvfrom(1024)
print("收到来自%s:%s发来的信息 -- %s"%(addr[0],addr[1], recv_data))

recv_data, addr = udp_socket.recvfrom(1024)
print("收到来自%s:%s发来的信息 -- %s"%(addr[0],addr[1], recv_data.decode()))

udp_socket.close()

