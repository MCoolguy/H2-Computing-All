import random 

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

player = [4, 5] #start pos of player
x, y = 4,5
while [x,y] == [4,5]:   
    x = random.randint(0,9) #prize must not be [4,5] as this is the start pos of player
    y = random.randint(0,10)
prize = [x,y]
grid = grid(prize,player)
print(type(grid))