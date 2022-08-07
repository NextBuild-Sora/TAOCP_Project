
# 2 UDP聊天程序实践
# --全双工通信小程序1--


from socket import *
import time
import tkinter
import threading


class Chat1(object):
    """
    初始化IP地址和端口
    """
    def __init__(self, ip="127.0.0.1", prot=2021):
        self.s = socket(AF_INET, SOCK_DGRAM)    #创建udp socket
        self.s.bind((ip, prot))   #绑定IP和端口

        self.recving()
        self.UI_init()  #初始化窗口

    def UI_init(self):
        """
        程序窗体
        :return:
        """
        self.root = tkinter.Tk()    #UI的主窗体

        self.Chat = tkinter.Text(width=100, height=30, bg='white')
        self.Chat.grid(row=1, column=0, columnspan=3)

        self.ip_input = tkinter.Entry()
        self.ip_input.grid(column=0, row=2)
        self.port_input = tkinter.Entry()
        self.port_input.grid(column=1, row=2)

        self.text = tkinter.Text(width=100, height=10)
        self.text.grid(column=0, row=3, columnspan=3)
        self.send = tkinter.Button(text="send", command= lambda :[self.send_msg(), ])
        self.send.grid(column=0, row=4)

        self.root.mainloop()

    def show_chat(self, msg):
        """
        显示聊天记录
        :param msg:
        :return:
        """
        self.temp = "\n" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + msg
        self.Chat.insert("end", self.temp)

    def send_msg(self):
        """
        发送聊天信息
        :return:
        """
        msg = self.text.get('0.0', 'end')   #获取text组件中的内容
        ip = self.ip_input.get()    #获取Entry中的文本信息
        port = self.port_input.get()

        try:
            #基于多线程实现全双工通信，一个线程用于接受信息，一个用于发送信息
            t_send = threading.Thread(target=self.s.sendto, args=(msg.encode("utf-8"), (ip, int(port))))
            # t_send.setDaemon(True)

            t_send.start()
        except Exception as e:
            msg = "发送失败: %s"%e
            # print("发送失败：%s"%e)
        #发送失败时，聊天记录为失败原因
        self.show_chat(msg)

    def recv_msg(self):
        """接受数据并显示"""
        while True:
            #1.接受数据
            recv_msg = self.s.recvfrom(1024)
            #2.解码
            recv_ip = recv_msg[1][0]+":"+str(recv_msg[1][1])
            recv_msg = recv_msg[0].decode("utf-8")
            #拼接完整联天信息
            msg = recv_ip+"\n"+recv_msg

            self.show_chat(msg)

    def recving(self):
           """
           启动线程用于接受信息
           :param self:
           :return:
           """
           t_recv = threading.Thread(target=self.recv_msg)
           t_recv.setDaemon(True)
           t_recv.start()

if __name__ == "__main__":
    q = Chat1()

