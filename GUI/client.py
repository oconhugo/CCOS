import socket
import pickle

#Class in charge of creating the client side of socket communication
#Establish the communication with the server (cooker)
class client(object):
    def __init__(self, master, **kwargs):
        print("3")

    def client_socket(self,z):
        s = socket.socket()
        port = 3125
        s.connect(('localhost', port))
        s.sendall(pickle.dumps(z))
        s.close()