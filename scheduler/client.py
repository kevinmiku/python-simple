# -*- coding: UTF-8 -*-

import socket
import time
import pickle
import struct


import config

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
        pass

    def send_request(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect(config.Server.HOST_IP, config.Server.HOST_PORT)
            self.client.setblocking(0)
            data = pickle.dumps(request)
            self.client.send(struct.pack("II", len(data)) + data)
        except BaseException as e:
            return -1
        return 1


if __name__ == '__main__':
    c = Client()
    c.start_client()