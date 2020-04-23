import socket

class client(object):
    def __init__(self, master, **kwargs):
        print("3")

    def client_socket(self):
        s = socket.socket()
        port = 3125
        s.connect(('localhost', port))
        z = 'LAS PODEROSISIMAS AGUILAS DEL AMERICA'
        s.sendall(z.encode())
        s.close()