import requests
import socket

class Server:
    c,a=None
    def __init__(self):
        self.activeSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.activeSocket.bind(('0.0.0.0',55628))
        self.activeSocket.listen(1)
        c,a = self.activeSocket.accept()

    def main(self):
        while(True):
            d=self.activeSocket.recv(1024)
            if d:
                print(d)