import socket

chat_socket = socket.socket() #a socket for chatting (data transmission)

address = "127.0.0.1" #input('Enter IPv4 address of server: ')
port = 6789 #int(input('Enter port number of server: '))

count = 0

chat_socket.connect((address,port)) #initiate a connection to the given adress tuple
correctnum = chat_socket.recv(1024)
tempnum = correctnum.decode()
while True:
    guess1 = input('guess:')
    guess2= guess1.encode() #encode message to be sent
    chat_socket.sendall(guess2)
    count += 1
    if count ==5 or int(tempnum)==int(guess1):
        break
    

chat_socket.close() #quit the data transmission socket