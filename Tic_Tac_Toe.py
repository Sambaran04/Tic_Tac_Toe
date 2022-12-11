from IPython.display import clear_output


def create_board(board):
    clear_output()
    print(board[1]+' |'+board[2]+' |'+board[3])
    print('__|__|_')
    print(board[4]+' |'+board[5]+' |'+board[6])
    print('__|__|_')
    print(board[7]+' |'+board[8]+' |'+board[9])
    
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player-1, choose your sign (X or O): ").upper()
        player_1 = marker
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    print(f'Player-1 is {player_1} and Player-2 is {player_2}')
    return (player_1,player_2)

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, mark):
     
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the middle
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the middle
    (board[3] == mark and board[6] == mark and board[9] == mark) or # down the right side
    (board[1] == mark and board[5] == mark and board[9] == mark) or # diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark))# diagonal

import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position] not in ('X','O')

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def position_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Enter the position (1,2,3,4,5,6,7,8,9): "))
        if position not in range(1,10):
            print("Invalid Input! Please try again...")
    return int(position)

def replay():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input("Do you want to play? (Y or N): ").upper()
        if choice not in ['Y', 'N']:
            print("Invalid Input! Please try again...")
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False
    
print('Welcome to Tic Tac Toe!')

while True:
    board = ['0','1','2','3','4','5','6','7','8','9']
    player_1, player_2 = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            create_board(board)
            position = position_choice(board)
            place_marker(board, player_1, position)
            
            if win_check(board, player_1):
                create_board(board)
                print(f'Congratulations {player_1}(Player-1), You Won')
                game_on = False
            else:
                if full_board_check(board):
                    create_board(board)
                    print("The Match is drawn...")
                    break
                else:
                    turn = 'Player 2'
        else:
            create_board(board)
            position = position_choice(board)
            place_marker(board, player_2, position)
            
            if win_check(board, player_2):
                create_board(board)
                print(f'Congratulations {player_2}(Player-2), You Won')
                game_on = False
            else:
                if full_board_check(board):
                    create_board(board)
                    print("The Match is drawn...")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
