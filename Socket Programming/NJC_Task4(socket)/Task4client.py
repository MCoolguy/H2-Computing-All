import socket 

client_socket = socket.socket()
client_socket.connect(('127.0.0.1',8888))

choices  = ['1','2','3','4']
while True:
    menu  = client_socket.recv(1024).decode()
    print(menu)
    choice = input("Enter choice: ")
    client_socket.sendall(choice.encode())
    print(client_socket.recv(1024).decode()) 
    if choice not in choices:
        break

    
    

