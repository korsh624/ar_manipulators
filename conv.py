import socket
import time

class ConveyerLine():
    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def setSpeed(self,s):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        self.UDPClientSocket.sendto(str.encode(f"s:{s}#"), self.serverAddressPort)

class ConveyerMuver():
    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def setPosition(self,point):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        self.UDPClientSocket.sendto(str.encode(f"s:1:{point}#"), self.serverAddressPort)