import random

board = [ "1", "2", "3", 
          "4", "5", "6",
          "7", "8", "9"]   

game_active = True
# build grid
''' example grid
X | X | X
----------
O | O | O
----------
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

    def check_row_win(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != " ":
            self.winner = self.board[0]
            return True
        if self.board[3] == self.board[4] == self.board[5] and self.board[3] != " ":
            self.winner = self.board[3]
            return True
        if self.board[6] == self.board[7] == self.board[8] and self.board[6] != " ":
            self.winner = self.board[6]
            return True

    def check_col_win(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != " ":
            self.winner = self.board[0]
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != " ":
            self.winner = self.board[1]
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != " ":
            self.winner = self.board[2]
            return True

    def check_diag_win(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != " ":
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != " ":
            self.winner = self.board[2]
            return True

class DefinePlayers:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

    def __str__(self):
        print(f'Player {self.name}, chose {self.coin}')


def coin_toss():
    coin_toss_round = random()
    if coin_toss_round == 0:
        return "heads"
    elif coin_toss_round == 1:
        return "tails" 

# start game
while (game_active):
    print('Player 1 please enter your name: ')
    name1 = input()
    print('Player 1, do you want heads or tails? ')
    coin1 = input()

    print('Player 2 please enter your name: ')
    name2 = input()

    player1 = DefinePlayers(name1, coin1)
    if player1.coin == 'heads':
        coin2 = 'tails'
    else:
        coin2 = 'heads'
    player2 = DefinePlayers(name2, coin2)

    # coin toss (random) which player starts
    if coin_toss() == player1.coin():
        print(f'{player1.name} starts the game')
        start1 = True
    else:
        print(f'{player2.name} starts the game')
        start1 = False

    if start1:
        # first player, ask place in grid
        print(f'{player1.name} - provide the spot you want to mark: ')
        coordX = int(input())
        # check if input is valid
        while (coordX < 1 or coordX > 9):
            print(f'{coordX} is invalid, choose a number from 1 to 9 : ')
            coordX = int(input())










# repeat until winner (3 in a row) or no more moves (read: grid full)

# determine win/loss/draw

# play again?


#print('Player Y - provide the spot you want to mark: ')
#coordY= input()

# TEST GRID INPUT
game_board1 = GameBoard(board)


game_board1.write_board(coordX-1)
game_board1.print_board()
#game_board1.restart_board()
#game_board1.print_board()