import socket
import random

def InitialiseGrid():
    grid = [["o" for i in range(4)]for i in range(5)]
    return grid

def DisplayGrid(arr):
    string =""
    for row in grid:
       string += " ".join(row)+'\n'
    newsocket.sendall(string.encode()) 
def ValidateRow(row):
    if row<=3 and row>=0:
        return True
    return False

def ValidateCol(col):
    if col<=4 and row>=0:
        return True
    return False

def getInput():
    rowguess = b"Enter your guess for row: "
    newsocket.sendall(rowguess)
    rguess = newsocket.recv(1024).decode()
    colguess = b"Enter is your guess for col: "
    newsocket.sendall(colguess)
    cguess = newsocket.recv(1024).decode()
    return int(rguess),int(cguess)

def CheckResult(row,col):
    if [row,col] == ship:
        return True
    return False
    



listensocket = socket.socket()
listensocket.bind(('127.0.0.1',12345))
listensocket.listen()
newsocket,address = listensocket.accept()

guesscount=0
won = False
grid = InitialiseGrid()
ship = [random.randint(0,3),random.randint(0,4)]

newsocket.sendall(b'Welcome to battleship')

                  
while guesscount<3:
    #print("guesses: " + str(guesscount))
    DisplayGrid(grid)
    row, col = getInput()
    won = CheckResult(row,col)
    #print("guess is " + row + ',' + col)
    guesscount +=1
    if won==True:
        grid[row][col] == 'S'
        DisplayGrid(grid)
        newsocket.sendall("YOU WON")
        break
    grid[row][col]=='X'

if won==False:
    DisplayGrid(grid)
    newsocke.sendall("GAME OVER")
        
    
    
