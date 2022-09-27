import socket 

clientsocket = socket.socket()
clientsocket.connect(('127.0.0.1',12344))



while True:
    data = clientsocket.recv(1024)
    if b"Enter" in data:
        choice = input(data.decode())
        clientsocket.sendall(choice.encode())
    
    else:
        print(data.decode())
        if b'Quit' or b'Prize' in data:
            break
        
        

       
#clientsocket.close() 
