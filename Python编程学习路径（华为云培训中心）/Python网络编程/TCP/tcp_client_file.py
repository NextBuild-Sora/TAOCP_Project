
# --- TCP文件服务器实践 ---
# 客户端


from socket import *

def main():

    tcp_client_socket = socket(AF_INET, SOCK_STREAM)    #创建

    #目的信息
    server_ip = input("IP地址：")
    server_port = int(input("端口："))

    #链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    #输入需要下载的文件名
    file_name = input("请输入要下载的文件名：")

    #发送文件下载请求
    tcp_client_socket.send(file_name.encode("utf-8"))

    #接受对方发送过来的数据
    recv_data = tcp_client_socket.recv(1024)

    #如果接受到数据再创建文件，否则不创建
    if recv_data:
        with open("[接受]" + file_name, "wb") as f:
            f.write(recv_data)

    #关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()



