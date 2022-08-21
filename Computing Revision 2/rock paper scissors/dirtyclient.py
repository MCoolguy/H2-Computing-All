#client side
import socket

game_socket = socket.socket()
#ip = input("Select public IP address: ")
#port = int(input("Select port no: "))

game_socket.connect(('127.0.0.1', 12362))
print("CONNECTED\n")

while True:
    in_data = ''
    while '\t' not in in_data:
        in_data += game_socket.recv(1024).decode()
    print(in_data)

    choice = input("Selection: ")

    if choice == '0':
        print("Client has left the game")
        game_socket.sendall(b'0\n')
        break
    else:
        game_socket.sendall(choice.encode() + b'\n')
    
    in_data = ''
    while '\t' not in in_data:
        in_data += game_socket.recv(1024).decode()
    print(in_data)

game_socket.close()
