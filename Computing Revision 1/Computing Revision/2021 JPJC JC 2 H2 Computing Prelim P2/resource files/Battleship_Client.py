#Client socket
#============

import socket

client_socket = socket.socket()

#address = input('Enter IPv4 address of server: ')
#port = int(input('Enter port number of server: '))

address = '127.0.0.1'
port = 12345

client_socket.connect((address, port))

while True:
    data = client_socket.recv(1024) #receive data from server
    if b"Enter" in data: #instruction received
        choice = input(data.decode()) #get player to input number
        client_socket.sendall(choice.encode()) #send number to server
        
    else:
        print(data.decode()) #non-instruction received
        if b"GAME OVER" in data \
        or b"YOU WON" in data:
            break

client_socket.close()

