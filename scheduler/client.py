# -*- coding: UTF-8 -*-

import socket
import pickle
from scheduler import config

class Client(object):
    """
    client
    """
    def __init__(self):
        """
        init function
        :return:
        """
        self.client = None
        pass

    def start_client(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((config.Server.servertHostName, config.Server.port2))
        pass

    def send_request(self, request):
        try:
            print((config.Server.HOST_IP, config.Server.port))
            self.client.connect((config.Server.HOST_IP, config.Server.port))
            #self.client.setblocking(0) #将套接字设置为非阻塞模式
            data = pickle.dumps(request)
            #self.client.send(struct.pack("II", len(data)) + data)
            self.client.sendall(request)
            reply = self.client.recv(4096)
            print(reply)
        except BaseException:
            return -1
        return 1

    def send_requestC(self):
        while True:
            send_data = input("输入发送内容:")
            self.client.sendall(bytes(send_data, encoding="utf8"))
            if send_data == "byebye":
                break
            accept_data = str(self.client.recv(1024), encoding="utf8")
            print("".join(("接收内容：", accept_data)))
        self.client.close()

if __name__ == '__main__':
    c = Client()
    #request = {'type':'Email', 'content': '我就是条邮件', 'send_time': '2017-12-07 16:44'}
    # message = "GET / HTTP/1.1\r\n\r\n"
    #remote_ip = socket.gethostbyname(host)

    c.start_client()
    c.send_requestC()


