import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"connection from {adress} established")
    clientsocket.send(bytes("welcome to server", "utf-8"))
    clientsocket.close()