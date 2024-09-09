import socket

class Lamp():

    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def setColor(self,r=0,g=0,b=0,y=0):
        msgFromClient=f"l:{r}:{b}:{g}:{y}#"
        print(msgFromClient)
        bytesToSend = str.encode(msgFromClient)
        bufferSize = 1024
        self.UDPClientSocket.sendto(bytesToSend, self.serverAddressPort)
