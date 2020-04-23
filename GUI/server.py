import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
s.bind(('0.0.0.0', port))
print ('Socket binded to port 3125')
s.listen(3)
print ('socket is listening')

while True:
    c, addr = s.accept()
    print('Got connection from ', addr)
    print(pickle.loads(c.recv(1024)))
    c.close()