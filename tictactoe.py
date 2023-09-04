import random

board = [ "1", "2", "3", 
          "4", "5", "6",
          "7", "8", "9"]   

# build grid
''' example grid
X | X | X
O | O | O
X | O | X
'''

class GameBoard:
    def __init__(self, board):
        self.board = board
    
    def __str__(self):
        pass

    # show board
    def print_board(self):
        print(f' {self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('-----------')
        print(f' {self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('-----------')
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]}')
    
    # write spot chose by Player
    def write_board(self, spot):
        self.spot = spot
        # if check which player's turn (if X) (elif O)
        self.board[self.spot] = 'X'
        # self.board[self.spot] = 'O'

    # clear grid    
    def restart_board(self):
        for i in range(9):
            self.board[i] = ' '

# define player X, ask name

# define player O, ask name

# coin toss (random) which player starts

# start game

# first player, ask place in grid to start

# second player, ask place in grid to place

# repeat until winner (3 in a row) or no more moves (read: grid full)

# determine win/loss/draw

# play again?

# TEST GRID INPUT

print('Player X - provide the spot you want to mark: ')
coordX = int(input())
while (coordX < 1 or coordX > 9):
    print(f'{coordX} is invalid, choose a number from 1 to 9 : ')
    coordX = int(input())
#print('Player Y - provide the spot you want to mark: ')
#coordY= input()

game_board1 = GameBoard(board)


game_board1.write_board(coordX-1)
game_board1.print_board()
#game_board1.restart_board()
#game_board1.print_board()