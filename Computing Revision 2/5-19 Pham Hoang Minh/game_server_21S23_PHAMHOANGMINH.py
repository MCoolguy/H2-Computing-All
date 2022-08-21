N = 3                       # Size of grid
WIDTH = len(str(N ** 2))    # Width for each cell
PLAYERS = ('O', 'X')        # Player symbols

class TicTacToe:

    def __init__(self):
        self.board = []
        for i in range(N):
            self.board.append([None] * N)

    def render_row(self, row_index):
        start = row_index * N + 1
        row = self.board[row_index].copy()
        for column_index in range(N):
            if row[column_index] is None:
                cell = str(start + column_index)
            else:
                cell = PLAYERS[row[column_index]]
            if len(cell) < WIDTH:
                cell += ' ' * (WIDTH - len(cell))
            row[column_index] = ' ' + cell + ' '
        return '|'.join(row) + '\n'

    def render_board(self):
        rows = []
        for row_index in range(N):
            rows.append(self.render_row(row_index))
        divider = '-' * ((WIDTH + 3) * N - 1) + '\n'
        return divider.join(rows)

    def make_move(self, player_index, cell_index):
        cell_index -= 1
        self.board[cell_index // N][cell_index % N] = player_index

    def is_valid_move(self, cell_index):
        if cell_index < 1 or cell_index > N ** 2:
            return False
        cell_index -= 1
        return self.board[cell_index // N][cell_index % N] is None

    def is_full(self):
        for row_index in range(N):
            for column_index in range(N):
                if self.board[row_index][column_index] is None:
                    return False
        return True

    def get_winner(self):
        # Check diagonals
        if self.board[0][0] is not None:
            found = True
            for i in range(N):
                if self.board[0][0] != self.board[i][i]:
                    found = False
                    break
            if found:
                return self.board[0][0]
        if self.board[0][N - 1] is not None:
            found = True
            for i in range(N):
                if self.board[0][N - 1] != self.board[i][N - i - 1]:
                    found = False
                    break
            if found:
                return self.board[0][N - 1]

        # Check rows and columns
        for i in range(N):
            if self.board[i][0] is not None:
                found = True
                for j in range(N):
                    if self.board[i][0] != self.board[i][j]:
                        found = False
                        break
                if found:
                    return self.board[i][0]
            if self.board[0][i] is not None:
                found = True
                for j in range(N):
                    if self.board[0][i] != self.board[j][i]:
                        found = False
                        break
                if found:
                    return self.board[0][i]

        # No matching lines were found, so no winner
        return None

import socket
import tictactoe


listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 3456))
listen_socket.listen()

game_socket, addr = listen_socket.accept()
game = tictactoe.TicTacToe()

while True:
    # Display current Tic-Tac-Toe board
    print(game.render_board())

    # Prompt for move from server player
    move = -1
    while move != 0 and not game.is_valid_move(move):
        move = int(input('Server moves (0 to quit): '))
    print()
    if move == 0:
        print(game.render_board())
        print('You quit, opponent wins!')
        print()
        break
		
    game.make_move(0, move)
	#Send b'MOVE' followed by the chosen cell #number and b'\n' to the opponent
    game_socket.sendall(b'MOVE' + move.decode() + b'\n') 

    # Display current Tic-Tac-Toe board
    print(game.render_board())

    # Check if server player won
    if game.get_winner()!=None:
        print('You win!')
        print()
        break

    # Check if board is full
    if game.is_full()==True:
        print('Stalemate')
        print()
        break

    # Receive move from client player
    received = b''
    while b'\n' not in received:
        received = game_socket.recv(1024)
        
    if b'Move' in received:
        move = int(received[4:])
        print('Client moves: ' + str(move))
        print()
        game.make_move(1, move)
    elif b'END' in received:
        print('Opponent quits, you win!')
        print()
        break

game_socket.close()
listen_socket.close()
