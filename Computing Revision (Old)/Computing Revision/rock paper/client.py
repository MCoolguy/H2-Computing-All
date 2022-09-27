import socket

chat_socket = socket.socket() 

address = "127.0.0.1" #input('Enter IPv4 address of server: ')
port = 1234 #int(input('Enter port number of server: '))


chat_socket.connect((address,port)) 

while True:
    choice = input('guess:').encode()
    chat_socket.sendall(choice)
    question = input(" Do you want to keep going? Yes or No?")
    question2= question.encode()
    chat_socket.sendall(question2)
    if question == "No":
        break
    else:
        pass
        
chat_socket.close() 
