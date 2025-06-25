import socket
import time

class Manipulator():
    def __init__(self, ip:str, port:int, type:str) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.type=type
        self.serverAddressPort = (ip, port)


    def toPoint(self,x, y, z, a=0, g=0):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        if self.type=="g":
            self.UDPClientSocket.sendto(str.encode(f"{self.type}:{x}:{y}:{a}:{z}:{g}#"), self.serverAddressPort)
        if self.type=="p":
            self.UDPClientSocket.sendto(str.encode(f"{self.type}:{x}:{y}:{z}:{a}:{g}#"), self.serverAddressPort)
        time.sleep(5)