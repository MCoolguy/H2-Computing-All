from random import randint
import socket


def user(position, direction):
    if direction == 'U':
        return [position[0], position[1]-1]
    elif direction == 'D':
        return [position[0], position[1]+1]
    elif direction == 'L':
        return [position[0]-1, position[1]]
    elif direction == 'R':
        return [position[0]+1, position[1]]
    else:
        return position

def grid(prize,player): #grid(prize,player)
    string = ''
    for row in range(11):
        for i in range(10):
            if [i,row] == player:
                string += 'O'     #player
            elif [i,row] == prize:
                string += 'P'
            else:
                string += '.' #unexplored grid
        string += '\n' #next line
    return string    


def main():

    player = [4, 5] #start pos of player

    x, y = 4,5
    while [x,y] == [4,5]:   
        x = randint(0,9) #prize must not be [4,5] as this is the start pos of player
        y = randint(0,10)
    
    prize = [x,y]

    print(grid(prize,player))

    counter = 0

    while True:
        move = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').upper()

        if move == 'Q':
            print('You have ended the game.')
            break
        else:
            next_position = user(player, move)
            counter += 1
            if next_position==prize:
                print('You got the Prize in '+str(counter)+' steps!')
                break
            else:
                player = next_position
                print(grid(prize,player))

#main()

serversocket = socket.socket()
serversocket.bind(('127.0.0.1',12345))
serversocket.listen()
clientsocket,addr = serversocket.accept()

player = [4, 5]
x, y = 4,5
while [x,y] == [4,5]:   
    x = randint(0,9) #prize must not be [4,5] as this is the start pos of player
    y = randint(0,10)
prize = [x,y]
counter =0
while True:
    clientsocket.sendall(str(grid(prize,player)).encode())
    move = clientsocket.recv(1024).decode()
    
    if str(b'\n'.decode()) in move:
        next_position = user(player, move)
        counter += 1
        if next_position==prize:
            clientsocket.sendall(("you got the prize in "+str(counter)).encode())
            break
        else:
            player = next_position
            clientsocket.sendall(str(grid(prize,player)).encode())

           
    #print(move)


#serversocket.close()
#clientsocket.close()


