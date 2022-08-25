import random


# def maze(prize,player): #grid(prize,player)
#     string = ""
#     for row in range(11):
#         for i in range(10):
#             if [i,row] == player:
#                 string += 'O'     #player
#             elif [i,row] == prize:
#                 string += 'P'
#             else:
#                 string += '.' #unexplored grid
#         string += '\n' #next line
#     return string
file  = open("MAZE.txt",'r')
maze = []
for line in file:
    maze.append(line.strip())
    
def displaymaze(prizex,prizey,playerx,playery):
    for row in range(11):  #row is y coord # i is x 
        for i in range(10):
            if maze[row][i] == maze[playerx][playery]:
                maze[row][i] = 'O'
    return maze[row]    
    
                
            


def choice(playerx,playery, direction):
    if direction == 'U':
        return (playerx+1,playery)
    elif direction == 'D':
        return (playerx-1,playery)
    elif direction == 'L':
        return (playerx,playery-1)
    elif direction == 'R':
        return (playerx,playery+1)
    else:
        return (playerx,playery)




playerx = 5
playery = 4 
randomx = random.randint(0,11)
randomy = random.randint(0,10)
while maze[randomx][randomy]=='X':
    randomx = random.randint(0,11)
    randomy = random.randint(0,10)
prizex = randomx
prizey= randomy
print(maze[prizex][prizey])

#print(displaymaze(prizex,prizey,playerx,playery))

while True:
    move = input("ENTER MOVE ").upper()
    if move == 'Q':
        print('gglmao.')
        break
    else:
        next_position = choice(playerx,playery, move)
        if next_position== (randomx,randomy):
            print('u got prize')
            break
        else:
            playerx = next_position[0]
            playery= next_position[1]
            print(displaymaze(prizex,prizey,playerx,playery))


            
            
    

