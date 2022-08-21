import socket
import random

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1',6789))
listen_socket.listen()#makes the socket 'listen_socket' listen for connection request

#.accept() returns (opens) a new socket for chatting (or data transmission)
#as well as the address of client (IPv4 address, port number)
chat_socket, address = listen_socket.accept()
randomnumber = random.randint(0,100) 
print(randomnumber)
count = 0 
correctnumber = str(randomnumber).encode()
chat_socket.sendall(correctnumber)

while True: #iterative server so that the server is always open and waiting for connection requests
    print('waiting for guess...')
    #print(randomnumber)
    message = chat_socket.recv(1024)
    guess = message.decode()#decodes data received from client
    count +=1
    print(guess,randomnumber)
    if int(guess) == randomnumber:
        print("correct")
        break
    elif count ==5:
        print("game over")
        break
    else:
        print("try again")


chat_socket.close() #quit the data transmission socket
#listen_socket.close() #quit the listening socket if I want to close the server