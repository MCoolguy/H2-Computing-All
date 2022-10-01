import random
file = open("MINEFIELD.txt","r")

n = int(file.readline())
field = [['.'for i in range(n)]for i in range(n)]
soldierx,soldiery = n//2,n//2
field[soldierx][soldiery] = "S"
totalsteps = []


def spawnmines():
    for line in file:
        x,y = line.strip().split(',')
        field[int(x)][int(y)] = 'M'
        
def display(minefield):        
    for count in range(len(minefield)):
        print("".join(minefield[count]))
        
def lose(x,y):
    if field[x][y] =='M':
        return True
    return False

def live(x,y):
    if field[x][y]!='M':
        return True
    return False

def win(x,y):
    if x>6 or y>6 or x<0 or y<0:
        return True
    return False

def repeat(x,y):
    if field[x][y] =='P':
        return True
    return False


def move(field):
    global soldierx
    global soldiery
    
    moves = ['UP','DOWN','LEFT','RIGHT']
    chance = random.randint(0,3)    
    if chance ==0:
        soldierx -=1
        if repeat(soldierx,soldiery):
            soldierx+=1
        totalsteps.append(' UP')
        if win(soldierx,soldiery):
            print("You win")
            return True
        elif lose(soldierx,soldiery):
            print("You lose")
            return False
        elif live(soldierx,soldiery):
            field[soldierx][soldiery] = 'P'


    if chance ==1:
        soldierx +=1
        if repeat(soldierx,soldiery):
            soldierx-=1
        totalsteps.append(' DOWN')
        if win(soldierx,soldiery):
            print("You win")
            return True
        elif lose(soldierx,soldiery):
            print("You lose")
            return False
        elif live(soldierx,soldiery):
            field[soldierx][soldiery] = 'P'

    if chance ==2:
        soldiery -=1
        if repeat(soldierx,soldiery):
            soldiery+=1
        totalsteps.append(' LEFT')
        if win(soldierx,soldiery):
            print("You win")
            return True
        elif lose(soldierx,soldiery):
            print("You lose")
            return False
        elif live(soldierx,soldiery):
            field[soldierx][soldiery] = 'P'

    if chance ==3:
        soldiery +=1
        if repeat(soldierx,soldiery):
            soldiery-=1
        totalsteps.append(' RIGHT')
        if win(soldierx,soldiery):
            print("You win")
            return True
        elif lose(soldierx,soldiery):
            print("You lose")
            return False
        elif live(soldierx,soldiery):
            field[soldierx][soldiery] = 'P'

        
    



#Main Program
spawnmines()
display(field)
while True:
    if move(field)==True or move(field)==False:
        break
display(field)
print("STEPS: " + "".join(totalsteps))
    


