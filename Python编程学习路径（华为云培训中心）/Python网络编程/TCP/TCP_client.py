
#  ---实现TCP客户端程序---


from socket import *


tcp_client_socket = socket(AF_INET, SOCK_STREAM)    #创建

#目的信息
server_ip = input("请输入服务器IP：")
server_port = int(input("请输入服务器port（端口）："))

tcp_client_socket.connect((server_ip, server_port))     #链接服务器

#提示用户输入数据
send_data = input("请输入要发送的数据：")
tcp_client_socket.send(send_data.encode('gbk'))

#接受对方发过来的数据
recvData = tcp_client_socket.recv(1024)
print('接受到的数据：', recvData.decode('gbk'))

tcp_client_socket.close()       #关闭套接字



