import random

board = [ "-", "-", "-", 
          "-", "-", "-",
          "-", "-", "-"]   

game_active = True
switch_token = True
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
        print()
        print(f' {self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('-----------')
        print(f' {self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('-----------')
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]}')
        print()
    
    # write spot chose by Player
    def write_board(self, spot, marker):
        self.spot = spot        
        # if check which player's turn (if X) (elif O)
        if marker == 'X':
            self.board[self.spot] = 'X'
        elif marker == 'O':
            self.board[self.spot] = 'O'
        else:
            print('Invalid marker')

    def check_free_spot(self, spot):
        self.spot = spot
        if  self.spot == 'X' or self.spot == 'O':
            return False
        else:
            return True

    # clear grid    
    def restart_board(self):
        for i in range(9):
            self.board[i] = '-'

    def check_row_win(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        if self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True

    def check_col_win(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True

    def check_diag_win(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
    

class DefinePlayers:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

    def __str__(self):
        return (f'Player {self.name}, chose {self.coin}')

    def cointoss(self):
        return self.coin


def coin_toss():
    coin_toss_round = random.randint(0, 1)
    if coin_toss_round == 0:
        return "heads"
    elif coin_toss_round == 1:
        return "tails" 

def checkTie():
    if game_active == True:
        if "-" not in game_start.board:
            print("It's a tie")
            return True

def checkWin():
    if game_start.check_row_win():
        print(f'The winner is {game_start.winner}')
        return True

    elif game_start.check_col_win():
        print(f'The winner is {game_start.winner}')
        return True

    elif game_start.check_diag_win():
        print(f'The winner is {game_start.winner}')
        return True

# start game

print('Player 1 please enter your name: ')
name1 = input()
print('Player 1, do you want heads or tails? ')
coin1 = input()    
print('Player 2 please enter your name: ')
name2 = input()

player1 = DefinePlayers(name1, coin1)
print(player1)
if player1.coin == 'heads':
    coin2 = 'tails'
else:
    coin2 = 'heads'
player2 = DefinePlayers(name2, coin2)
flip = coin_toss()    
print(flip)
# coin toss (random) which player starts
if flip == player1.cointoss():
    print(f'{player1.name} starts the game')
    switch_token = True
else:
    print(f'{player2.name} starts the game')
    switch_token = False

game_start = GameBoard(board)

while (game_active):
    
    if switch_token:        
        game_start.print_board()
        # first player, ask place in grid
        print(f'{player1.name} - provide the spot you want to mark (1-9): ')
        coordX = int(input())-1
        # check if input is valid
        while (coordX < 0 or coordX > 9) and game_start.check_free_spot(coordX):
            print(f'{coordX} is invalid or already taken, choose a number from 1 to 9 : ')
            coordX = int(input())-1
        game_start.write_board(coordX, 'X')
        game_start.print_board() 
        if checkWin():
            game_active = False
        if checkTie():
            game_active = False
        switch_token = False
        
    else:
        game_start.print_board()
        print(f'{player2.name} - provide the spot you want to mark (1-9): ')
        coordY = int(input())-1
        # check if input is valid
        while (coordY < 0 or coordY > 9) and game_start.check_free_spot(coordY) :
            print(f'{coordY} is invalid or already taken, choose a number from 1 to 9 : ')
            coordY = int(input())-1
        game_start.write_board(coordY, 'O')
        game_start.print_board()          
        if checkWin():
            game_active = False
        if checkTie():
            game_active = False
        switch_token = True
        
    if game_active == False:
        print('Do you want to play again? (y/n) \n')
        choice1 = input()
        if choice1 == 'y':
            game_active = True
            game_start.restart_board()
        elif choice1 == 'n':
            game_active = False
