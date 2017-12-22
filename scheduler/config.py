# -*- coding: UTF-8 -*-

"""
全局配置文件
"""
import socket
import sys
class Client(object):
    pass

class Server(object):
    host = "www.baidu.com"
    port = 80
    port2 = 8081
    try:
        HOST_IP = socket.gethostbyname(host)
        #servertHostName = socket.gethostname()
        servertHostName = '127.0.0.1'
    except socket.error:
        print("failed to get host")

    #HOST_IP = '127.0.0.1'
    #HOST_PORT = 9090
    MAX_WORKER_NUM = 5
    RESP_NUM = 2

