import socket

clientsocket = socket.socket()
clientsocket.connect(('127.0.0.1',12345))

while True:
    data = clientsocket.recv(1024).decode()
    print(data)

    move = input("U for up, D for down, L for left, R for right")

    if move =="Q":
        print('gg')
        clientsocket.sendall(move.encode())
        break
    else:
        clientsocket.sendall(move.encode()+b'\n')

