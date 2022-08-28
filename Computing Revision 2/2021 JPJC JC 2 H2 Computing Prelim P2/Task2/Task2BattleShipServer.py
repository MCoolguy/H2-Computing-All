import random
import socket

def InitialiseGrid():
    grid = [["O" for i in range(4)]for i in range(5)] #AVOID ALIASING
    return grid

def DisplayGrid(arr):
    for row in grid:
        print(" ".join(row))
        
def validateRow(row):
    if not row.isdigit(): #presence and type check
        return False
    if int(row) < 0 or int(row) > 3: #range check
        return False
    return True

def validateCol(col):
    if not col.isdigit(): #presence and type check
        return False
    if int(col) < 0 or int(col) > 4: #range check
        return False
    return True

def CheckResult(row,col):
    if [row,col] == ship:
        return True
    return False
    
def getInput():
    rowguess = b'Enter guess for row: '
    serversocket.sendall(rowguess)
    rowguess = serversocket.recv(1024).decode()
    while validateRow(rowguess)!=True:
        rowguess = b'Enter guess for row: '
        serversocket.sendall(rowguess)
        rowguess = serversocket.recv(1024).decode()  
    colguess = b'Enter guess for col: '
    serversocket.sendall(colguess)
    colguess = serversocket.recv(1024).decode()
    while validateCol(colguess)!=True:
        colguess = b'Enter guess for col: '
        serversocket.sendall(colguess)
        colguess = serversocket.recv(1024).decode()
    return int(rowguess),int(colguess)
    
listensocket = socket.socket()
listensocket.bind(('127.0.0.1',6789))
listensocket.listen()

serversocket,address = listensocket.accept()

ship = [random.randint(0,3),random.randint(0,4)]
grid = InitialiseGrid()
guesscount = 0
won = False

serversocket.sendall(b'Welcome to Battleship!')
while guesscount<3:
    print()
    DisplayGrid(grid)
    row,col = getInput()
    guesscount+=1
    won = CheckResult(row,col)
    if won ==True:
        grid[row][col] = 'S'
        print()
        DisplayGrid(grid)
        serversocket.sendall(b"YOU WON")
        break
    grid[row][col] = "X"
    
if won ==False:
    print()
    DisplayGrid(grid)
    serversocket.sendall(b"GAME OVER")
     
serversocket.close()
listensocket.close()
        
    