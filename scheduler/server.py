# coding=utf-8
from scheduler import config
import socket
import socketserver

class Server:
    def __init__(self):
        """
        init function
        :return:
        """
        self.server = None

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print((config.Server.servertHostName, config.Server.port2))
        self.server.bind((config.Server.servertHostName, config.Server.port2)) #绑定端口
        print(1)
        self.server.listen(5)

    def listen(self):
        while True:
            conn, addr = self.server.accept()
            while True:
                accept_data = str(conn.recv(1024), encoding="utf8")
                print("".join(["接收内容：", accept_data, "     客户端口：", str(addr[1])]))
                if accept_data == "byebye":  # 如果接收到“byebye”则跳出循环结束和第一个客户端的通讯，开始与下一个客户端进行通讯
                    break
                send_data = input("输入发送内p容：")
                conn.sendall(bytes(send_data, encoding="utf8"))
            conn.close()  # 跳出循环时结束通讯


if __name__ == '__main__':
    server = Server()
    server.start()
    server.listen()
