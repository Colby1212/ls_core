import random 
import os

WINNING_COMBINATIONS = [
    [1,2,3], [4, 5, 6], [7, 8, 9],   # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
    [1, 5, 9], [3, 5, 7],            # diagonals 
]

PLAYER_MARKER = 'X'

COMPUTER_MARKER = 'O'

INITIAL_MARKER = '-'

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def display_board(board):
    os.system('clear')

    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ') 
    print(f'-----+-----+-----') 
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ') 
    print(f'-----+-----+-----') 
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')

def game_status(board): 
    for combination in (WINNING_COMBINATIONS):
        values = [board[i] for i in combination]
        if values[0] == INITIAL_MARKER:
            continue
        if len(set(values)) == 1:
            if values[0] == PLAYER_MARKER:
                return 'Player Wins!!'
            else:
                return 'Computer Wins!!'
        
    if empty_squares(board) == []: 
        return 'Tie Game!'


def is_invalid_choice(choice): 
    try: 
        int(choice) 
    except ValueError: 
        return True 
    return False

def valid_choice(choice, board):
    while True:
        while is_invalid_choice(choice): 
            print(f"Invalid choice! Pick again ({empty_squares(board)}): ") 
            choice = input() 
        if int(choice) not in empty_squares(board): 
            print(f"Invalid choice! Pick again ({empty_squares(board)}): ") 
            choice = input() 
        else: 
            return choice

def player_move(board):
    choice = input(f'Pick a square({empty_squares(board)}): ')
    choice = int(valid_choice(choice, board))
    board[choice] = PLAYER_MARKER

def computer_move(board): 
    computer_choice = random.choice(empty_squares(board)) 
    board[computer_choice] = COMPUTER_MARKER


def play_again(): 
    answer = input("Would you like to play again? (y/n): ") 
    if answer and answer[0].casefold() == 'y': 
        return True 
    else: 
        return

def tic_tac_toe(): 
    while True: 
        board = initialize_board() 
        display_board(board)
        while True:
            player_move(board)  
            if game_status(board): 
                display_board(board)
                print(game_status(board)) 
                break
            computer_move(board) 
            display_board(board) 
            if game_status(board): 
                print(game_status(board)) 
                break 
        if not play_again(): 
            break

tic_tac_toe()