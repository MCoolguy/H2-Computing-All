import socket

chat_socket = socket.socket() #a socket for chatting (data transmission)

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

chat_socket.connect((address,port)) #initiate a connection to the given adress tuple
while True:
    print('WAITING FOR SERVER...')
    message = b''
    while b'\n' not in message: #while endline is not in message, keep receiving data from the chat socket for data transmission
        message += chat_socket.recv(1024)
    print('SERVER WROTE: ' + message.decode()) #decode the message received and display it
    message = input('INPUT CLIENT: ').encode() #encode message to be sent
    chat_socket.sendall(message + b'\n')
    if message.upper() == 'quit'.upper(): #code for server terminating the chat
        chat_socket.sendall("CLIENT HAS QUIT THE CHATTING APPLICATION.".encode() + b'\n')
        break

chat_socket.close() #quit the data transmission socket
