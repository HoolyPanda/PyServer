import requests
import socket

class Client:
    def __init__(self):
        self.activeSocket= socket.socket()
        self.activeSocket.connect(('176.59.49.181',1000))
        while(True):
            self.activeSocket.send(str(input()))