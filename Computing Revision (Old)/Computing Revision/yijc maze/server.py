import socket
import random

listensocket = socket.socket()
listensocket.bind(('127.0.0.1',12344))
listensocket.listen()
newsocket,address = listensocket.accept()

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

def getinput():
    question = b"Enter U(p), D(own), L(eft), R(ight) or Q(uit) : "
    newsocket.sendall(question)
    choice = (newsocket.recv(1024).decode())
    return choice

    

player = [4, 5] #start pos of player
x, y = 4,5
while [x,y] == [4,5]:   
    x = random.randint(0,9) #prize must not be [4,5] as this is the start pos of player
    y = random.randint(0,10)
prize = [x,y]
grid1 = grid(prize,player)


#newsocket.sendall(grid.encode())
counter = 0
#newsocket.sendall(grid.encode())
while True:
    newsocket.sendall(grid1.encode())
    move = getinput()
    if move == 'Q':
        newsocket.sendall(b"You Quit")
        break
    else:
        next_position = user(player, move)
        counter += 1
        if next_position==prize:
            newsocket.sendall(grid.encode())
            newsocket.sendall(b'You got the Prize in '+str(counter)+' steps!')
            break
        else:
            player = next_position
            grid1 = (prize,player)
            newsocket.sendall(grid1.encode())

#newsocket.close()
# while True:
#     move = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').upper()
#     if move == 'Q':
#         print('You have ended the game.')
#         break
#     else:
#         next_position = user(player, move)
#         counter += 1
#         if next_position==prize:
#             print('You got the Prize in '+str(counter)+' steps!')
#             break
#         else:
#             player = next_position
#             print(grid(prize,player))
