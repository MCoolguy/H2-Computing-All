import sqlite3
import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1',8888))
listen_socket.listen()

server_socket,address = listen_socket.accept() 

conn = sqlite3.connect('tide.db')

while True:
    
    menu = b'''Options: \n
              1. Highest high tide with one corresponding date and time it happened\n
              2. Lowest low tide with one corresponding date and time it happened\n
              3. Largest tidal range\n
              4. Smallest tidal range'''
              
    server_socket.sendall(menu)
    choice = server_socket.recv(1024).decode()
    
    if choice == '1':
        command = '''SELECT MAX(Tide.Height),Tide.Time,Tide.Date From Tide WHERE Tide.isHigh=1 '''
        value = conn.execute(command).fetchone()
        height,time,date = value[0],value[1],value[2]
        message = "Height is " + str(height)+ ", Time is "+str(time)+ ", Date is "+str(date)
        server_socket.sendall(message.encode())
    
    elif choice =='2':
        command = '''SELECT MIN(Tide.Height),Tide.Time,Tide.Date From Tide WHERE Tide.isHigh=1 '''
        value = conn.execute(command).fetchone()
        height,time,date = value[0],value[1],value[2]
        message = "Height is " + str(height)+ ", Time is "+str(time)+ ", Date is "+str(date)
        server_socket.sendall(message.encode())
        
    elif choice =='3':
        command_high = '''Select Height from Tide WHERE isHigh=1'''
        command_low = '''Select Height from Tide WHERE isHigh=0'''

        high = conn.execute(command_high).fetchall() 
        low = conn.execute(command_low).fetchall()

        largest_range = 0.0
        for index in range(len(high)):
            absrange = abs(high[index][0]-low[index][0])
            if absrange>largest_range:
                largest_range = absrange
                
        largest_range = round(largest_range,1)  
        
        message = "The largest range was " + str(largest_range)     
        server_socket.sendall(message.encode())
        
    elif choice =='4':
        command_high = '''Select Height from Tide WHERE isHigh=1'''
        command_low = '''Select Height from Tide WHERE isHigh=0'''

        high = conn.execute(command_high).fetchall() 
        low = conn.execute(command_low).fetchall()

        smallest_range = 999.9
        for index in range(len(high)):
            absrange = round(abs(high[index][0]-low[index][0]),1)
            if absrange<smallest_range:
                smallest_range = absrange
                
        smallest_range = round(smallest_range,1)
        message = "The smallest range was " + str(smallest_range)     
        server_socket.sendall(message.encode())
    
    else:
        server_socket.sendall(b'Closing server')
        break
        

        
    
    
        
server_socket.close()
        

        
