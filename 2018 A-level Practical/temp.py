import random
file  = open("MAZE.txt",'r')
maze = []
for line in file:
    maze.append(line.strip())
    
randomx = random.randint(0,10)
randomy = random.randint(0,11)
while maze[randomx][randomy]=='X':
    randomx = random.randint(0,10)
    randomy = random.randint(0,11)
    
prizex = randomx
prizey= randomy

templist = list(maze[0])
templist[0][1] = 'p'
maze[0] = ''.join(templist[0][1])

#maze[prizex][prizey] = 'p'
print(type(maze[0][1]))
        