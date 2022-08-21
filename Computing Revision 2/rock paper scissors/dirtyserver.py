#server side rock paper scissors
import socket
import random

def gen_move():
    num = random.randint(1,3)
    return num

def comparison(s,c):
    if s == c:
        return 'd'

    if s == 1 and c == 2 or s == 2 and c == 3 or s == 3 and c == 1:
        return 'c'

    return 's'


    
move = ['NULL', 'r', 'p', 's'] #r: rock, p:paper, s=scissors, 1-based indexing

my_socket = socket.socket()
#ip = input("ip: ")
#port = int(input("port: "))

my_socket.bind(('127.0.0.1', 12362))
my_socket.listen()


game_socket, addr = my_socket.accept()

print("Connect to: " + str(addr))

scores = {'s':0, 'c':0} #keep track of score counter, s: server, c:client



while True:
    game_socket.sendall(b"Please key in your options:\n0:quit\n1:scissors\n2:rock\n3:paper\t\n")

    in_data = ''
    while '\n' not in in_data:
        in_data += game_socket.recv(1024).decode()

    if in_data.strip().isnumeric() != True:
        game_socket.sendall(b"Please enter a number\t\n")

    elif in_data.strip() == '0':
        print("Client has left the game")
        break
    
    else:
        server_choice, client_choice = gen_move(),int(in_data.strip())
        win = comparison(server_choice, client_choice)

        game_socket.sendall(b"Server's choice: " + str(server_choice).encode()+b'\n')
        if win == 's':
            game_socket.sendall(b"Server won\t")
            scores['s'] += 1
        elif win == 'c':
            game_socket.sendall(b"Client won\t")
            scores['c'] += 1
        else:
            game_socket.sendall(b"It was a draw\t")

        game_socket.sendall(b"Scores:\nServer: " + str(scores['s']).encode() + b"\nClient: " + str(scores['c']).encode() + b'\t\n\n')
            

game_socket.close()
