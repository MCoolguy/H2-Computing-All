import random
def gen_maze():
    file = open("MAZE.TXT", 'r')
    maze = [] #will be a 2 dimensional list to store the maze
    for line in file:
        line = line.strip()
        row = []
        for char in line:
            row.append(char)
        maze.append(row)
    
    file.close()
    return maze

def random_treasure(maze):

    prize_posn = []
    for row_index in range(1,len(maze)-1):
        for col_index in range(1, len(maze[0])-1):
            if maze[row_index][col_index] == '.':
                prize_posn.append((row_index, col_index))

    index = random.randint(0, len(prize_posn)-1)
    prize = prize_posn[index]
    
    maze[prize[0]][prize[1]] = 'P'
    return prize

def display(maze):
    temp = ''
    for row in maze:
        for col in row:
            temp = temp + col + ' '
        temp += '\n'
    print(temp)
    return


def find_player(maze):
    for row in maze:
        if 'O' in row:
            return (maze.index(row), row.index('O'))

def update_posn(player, move, prev_move):
    if move == 'U':
        player = (player[0]-1, player[1])
    if move == 'D':
        player = (player[0]+1, player[1])
    if move == 'L':
        player = (player[0], player[1]-1)
    if move == 'R':
        player = (player[0], player[1]+1)
    if move == '':
        if prev_move == '':
            pass
        else:
            player = update_posn(player, prev_move, prev_move)
    return player


def validate(move, maze, player, prev_move):
    move_avail = []
    if maze[player[0]][player[1]-1] != 'X': #Left
        move_avail.append((player[0], player[1]-1))
        
    if maze[player[0]][player[1]+1] != 'X': #Right
        move_avail.append((player[0], player[1]+1))
        
    if maze[player[0]-1][player[1]] != 'X': #Up
        move_avail.append((player[0]-1, player[1]))
        
    if maze[player[0]+1][player[1]] != 'X': #Down
        move_avail.append((player[0]+1, player[1]))
        
    posn = update_posn(player, move, prev_move)
    if posn in move_avail:
        return True
    return False

    
def game():
    maze = gen_maze() #generate the maze
    treasure_posn = random_treasure(maze) #put a random treasure on the maze
    player = find_player(maze) #current position of player
    move_lst = ["U", 'D', 'L', 'R', '']
    prev_move = ''
    
    while True:
        display(maze)
        move = input("input action ('U', 'D', 'L', 'R', ''):")
        while (move not in move_lst) or (validate(move, maze, player, prev_move) == False): #validation check
            print("Please enter a valid move")
            move = input("input action ('U', 'D', 'L', 'R', ''):")
        temp_player_posn = update_posn(player, move, prev_move)

        #check if new position hits the prize
        if maze[temp_player_posn[0]][temp_player_posn[1]] == 'P':
            print()
            print("Congratulations, you win!")
            break

        #updating maze and player position
        maze[player[0]][player[1]] = '.'
        maze[temp_player_posn[0]][temp_player_posn[1]] = 'O'
        player = temp_player_posn
        if move != '':
            prev_move = move
        print()

    print("Ending Game")
        
        
        
        
        
    
