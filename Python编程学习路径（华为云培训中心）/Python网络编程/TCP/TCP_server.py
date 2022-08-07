
# ---实现TCP服务器端程序---


from socket import * 

tcp_server_socket = socket(AF_INET, SOCK_STREAM)    #创建socket

address = ('', 7788)    #本地信息

tcp_server_socket.bind(address) #绑定
tcp_server_socket.listen(128)   #被动；接受别人的链接

client_socket, clientAddr = tcp_server_socket.accept()  #客户端链接服务器

recv_data = client_socket.recv(1024)    #接受对方发送的过来的数据
print('接受到的数据位：', recv_data.decode('gbk'))

client_socket.send("Thank you （谢谢你）!".encode('gbk'))     #发送一些数据到客户端

client_socket.close()       #关闭客户端服务的套接字


