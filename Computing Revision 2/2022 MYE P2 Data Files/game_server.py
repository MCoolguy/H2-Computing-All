import socket
import tictactoe

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 3456))
listen_socket.listen()

game_socket, addr = listen_socket.accept()
game = tictactoe.TicTacToe()

while True:
    # Display current Tic-Tac-Toe board
    <your code here>

    # Prompt for move from server player
    move = -1
    while move != 0 and not game.is_valid_move(move):
        move = int(input('Server moves (0 to quit): '))
    print()
    if move == 0:
        <your code here>
        print('You quit, opponent wins!')
        print()
        break
		
    game.make_move(0, move)
	#Send b'MOVE' followed by the chosen cell #number and b'\n' to the opponent
    <your code here>

    # Display current Tic-Tac-Toe board
    <your code here>

    # Check if server player won
    if <your code here>:
        print('You win!')
        print()
        break

    # Check if board is full
    if <your code here>:
        print('Stalemate')
        print()
        break

    # Receive move from client player
    received = b''
    while b'\n' not in received:
        <your code here>
    if <your code here>:
        move = int(received[4:])
        print('Client moves: ' + str(move))
        print()
        game.make_move(1, move)
    elif <your code here>:
        print('Opponent quits, you win!')
        print()
        break

game_socket.close()
listen_socket.close()
