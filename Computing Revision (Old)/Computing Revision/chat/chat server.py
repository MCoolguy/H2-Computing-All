import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1',6789))
listen_socket.listen()#makes the socket 'listen_socket' listen for connection request

#.accept() returns (opens) a new socket for chatting (or data transmission)
#as well as the address of client (IPv4 address, port number)
chat_socket, address = listen_socket.accept() 
while True: #iterative server so that the server is always open and waiting for connection requests
    message = input('INPUT SERVER: ').encode() #encodes the message server inputs
    if message.upper() == 'quit'.upper(): #code for server terminating the chat
        chat_socket.sendall("SERVER HAS QUIT THE CHATTING APPLICATION.".encode()+ b'\n')
        break
    chat_socket.sendall(message + b'\n') #appends '\n' to act as an ending character so that the client can verify that every packet has been sent (client checks if '\n' inside message)
    print('WAITING FOR CLIENT...')
    message = b''
    while b'\n' not in message:
        message += chat_socket.recv(1024)
    print('CLIENT WROTE: ' + message.decode())#decodes data received from client
    
    
chat_socket.close() #quit the data transmission socket
#listen_socket.close() #quit the listening socket if I want to close the server
