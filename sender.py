import socket
unit=('192.168.42.13',8888)
kvu= ('192.168.42.10',8888)
def udp_sender(host='192.168.42.13', port=8888):
    # Создаем UDP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Привязываем сокет к адресу и порту
        sock.bind((host, port))
        sock.sendto(b"unitstart", kvu)
                 

if __name__ == "__main__":
    udp_sender()