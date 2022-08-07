
# --- TCP文件服务器实践 ---
# 服务器端


from socket import *
import sys


def get_file_content(file_name):
    """ 获取文件的内容 """
    try:
        with open(file_name, "rb") as f:
            content = f.read()
        return content
    except:
        print("下载异常：%s" % file_name)


def main():
    if len(sys.argv) != 2:
        port = 2333
    else:
        port = int(sys.argv[1]) 

    tcp_server_socket = socket(AF_INET, SOCK_STREAM)    #创建socket
    address = ('', port)        #本地信息

    tcp_server_socket.bind(address)     #绑定本地信息
    tcp_server_socket.listen(128)       #将主动套接字变为被动套接字

    while True:
        
         #等待客户端的链接，即为这个客户端发送文件
        client_socket, clientAddr = tcp_server_socket.accept()   

         #接受对方发送过来的数据
        recv_data = client_socket.recv(1024)       
        file_name = recv_data.decode("utf-8")
        print("对方请求下载的文件名为：%s" % file_name)
        file_content = get_file_content(file_name)

        #发送文件的数据给客户端
        if file_content:
            client_socket.send(file_content)
            client_socket.close()   #关闭这个套接字

    tcp_server_socket.close()   #关闭监听套接字

if __name__ == '__main__':
    main()


