# coding=utf-8
from scheduler import config
import socket
class Server:
    def __init__(self):
        """
        init function
        :return:
        """
        self.server = None
        pass
    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        try:
            print((config.Server.servertHostName, config.Server.port2))
            self.server.bind((config.Server.servertHostName, config.Server.port2)) #绑定端口
            print("1")
            self.server.listen(5) #设置最大连接数

            while True:
                clientsocket, addr = self.client.accept()
                print("链接地址：%s" % str(addr))
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    server = Server()
    server.start()
    server.listen()