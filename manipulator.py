import socket
import time

class Manipulator():
    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def toPoint(self,x, y, z, a=0, g=0):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        self.UDPClientSocket.sendto(str.encode(f"g:{x}:{y}:{a}:{z}:{g}#"), self.serverAddressPort)
        time.sleep(5)