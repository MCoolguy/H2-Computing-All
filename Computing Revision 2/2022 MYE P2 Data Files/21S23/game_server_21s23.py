import socket
import Task3
#SERVER CODE -uses the symbol 'O' to represent its moves
#passively listens for incoming connection requests 
listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 5678))
listen_socket.listen()

game_socket, addr = listen_socket.accept()

game = Task3.TicTacToe() #instantiaite TicTacToe object

while True:
    # Display current Tic-Tac-Toe board
    print(game.render_board())
    # Prompt for move from server player
    move = -1 # status to indicate server is waiting ie. cant move
    while move != 0 and not game.is_valid_move(move):
        move = int(input('Server moves (0 to quit): '))
    print()
    if move == 0: #Although player sends 0 to quit, the actual data sebt us "END\n". 
        game_socket.sendall(b'END\n')
        print('You quit, Server quits, Client wins!')
        print()
        break
    game.make_move(0, move) #server uses symbol  'O' in PLAYERS
    #Send b'MOVE' followed by the chosen cell #number and b'\n' to the opponent
    game_socket.sendall(b'MOVE' + str(move).encode() + b'\n')
    # Display current Tic-Tac-Toe board
    print(game.render_board())
    # Check if server player won
    if game.get_winner() != None:
        print('You win!')
        print()
        break
    # Check if board is full
    if game.is_full():
        print('Stalemate')
        print()
        break
    # Receive move from client player
    received = b''
    while b'\n' not in received:
        receiving = game_socket.recv(1024)
        received = received + receiving
    received.encode()
    print(received)
    if 'MOVE' in received:
    #if received.startswith(b'MOVE'):
        move = int(received[4:])
        print('Client moves: ' + move)
        print()
        game.make_move(1, move)
    elif 'END' in received:
    #elif received.startswith(b'END'):
        print('Client has quitted, server wins!')
        print()
        break

game_socket.close()
listen_socket.close()
