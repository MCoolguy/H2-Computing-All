import socket
import random

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1',1234))
listen_socket.listen()

chat_socket, address = listen_socket.accept()
options = ['rock','paper','scissors']
serverscore = 0
clientscore = 0
while True:
    choice = chat_socket.recv(1024).decode()
    serverchoice = options[random.randint(0,2)]
    print("server chose " + serverchoice)
    if choice == serverchoice:
        print("tie")
        decision = chat_socket.recv(1024).decode()
        if decision == "Yes":
            pass
        else:
            break
    elif choice=='paper' and serverchoice=="rock" or choice=='rock' and serverchoice=="scissors" or choice=='scissors' and serverchoice=="paper":
        print(" you win ")
        clientscore +=1
        decision = chat_socket.recv(1024).decode()
        if decision == "Yes":
            pass
        else:
            break
    else:
        print("you lose")
        serverscore += 1 
        decision = chat_socket.recv(1024).decode()
        if decision == "Yes":
            pass
        else:
            break
print("server score: " + str(serverscore))
print("client score: " + str(clientscore))

listen_socket.close() 
