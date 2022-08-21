import socket
import tictactoe

client_socket = socket.socket()
client_socket.connect(('127.0.0.1',3456))
game = tictactoe.TicTacToe()

while True:
    if game.get_winner()!=None:
        print('You win!')
        print()
        break

    # Check if board is full
    if game.is_full()==True:
        print('Stalemate')
        print()
        break
    
    received = b''
    while b'\n' not in received:
        received = client_socket.recv(1024)     
    if b'Move' in received:
        move = int(received[4:])
        print('Server moves: ' + str(move))
        print()
        game.make_move(1, move)
    elif b'END' in received:
        print('Opponent quits, you win!')
        print()
        break
    
    # Display current Tic-Tac-Toe board
    print(game.render_board())

    move = -1
    while move != 0 and not game.is_valid_move(move):
        move = int(input('Client moves (0 to quit): '))
    print()
    if move == 0:
        print(game.render_board())
        print('You quit, opponent wins!')
        print()
        break
		
    game.make_move(0, move)
	#Send b'MOVE' followed by the chosen cell #number and b'\n' to the opponent
    client_socket.sendall(b'MOVE' + move.decode() + b'\n') 

client_socket.close()

