import random
import os

INITIAL_MARKER = '-'

PLAYER_MARKER = 'X'

COMPUTER_MARKER = 'O'

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7],
    ]


def join_or(sequence, delimiter=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {word} {sequence[1]}"

    leading_items = delimiter.join(str(item) for item in sequence[0:-1])
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'


def prompt(message):
    print(f' ==> {message}')

def display_board(board):
    os.system('clear')

    prompt(f"You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}")
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |')
    print('')


def initialize_board():
    return {square: INITIAL_MARKER  for square in range(1,10)}


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square {join_or(valid_choices)}')
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry thats not a valid choice")

    board[int(square)] =  PLAYER_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    if winning_squares(board):
        square = winning_squares(board)
        board[square] = COMPUTER_MARKER
    elif find_defense(board):
        square = random.choice(list(find_defense(board)))
        board[square] = COMPUTER_MARKER
    elif find_offense(board):
        square = random.choice(find_offense(board))
        board[square] = COMPUTER_MARKER

    elif board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER
    else:
        square = random.choice(empty_squares(board))
        board[square] = COMPUTER_MARKER

def winning_squares(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        line_values = board[sq1], board[sq2], board[sq3]
        if ((line_values.count(COMPUTER_MARKER) == 2) and (INITIAL_MARKER in line_values)):
            return line[line_values.index(INITIAL_MARKER)]
    return None

def find_defense(board):
    defensive_moves = []
    for line in WINNING_LINES:
        line_values = [board[sq] for sq in line]
        if (line_values.count(PLAYER_MARKER) == 2) and (INITIAL_MARKER in line_values):
            defensive_moves.append(line[line_values.index(INITIAL_MARKER)])
    return set(defensive_moves)

def find_offense(board):
    offensive_lines = []
    for line in WINNING_LINES:
        line_values = [board[sq] for sq in line]
        if (line_values.count(INITIAL_MARKER) == 2) and (COMPUTER_MARKER in  line_values):
            priority_squares = [sq for sq in line if board[sq] == INITIAL_MARKER]
            offensive_lines.extend(priority_squares)
    return offensive_lines

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == PLAYER_MARKER
                and board[sq2] == PLAYER_MARKER
                and board[sq3] == PLAYER_MARKER):
            return 'Player'
        if (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def start_new_round(text):
    prompt(text)
    answer = input().lower()
    if answer and answer[0] != 'y':
        return False
    return True

def alternate_turn(turn):
    if turn == 'computer':
        turn = 'player'
    else:
        turn = 'computer'
    return turn

def your_turn(turn, board):
    if turn == 'computer':
        computer_chooses_square(board)
    else:
        player_chooses_square(board)

def play_tic_tac_toe():
    while True:
        player_score = 0
        computer_score = 0
       
        while player_score < 4 and computer_score < 4:
            board = initialize_board()
            turn = random.choice(['player', 'computer'])
            
            while True:
                display_board(board)
                your_turn(turn, board)
                turn = alternate_turn(turn)
                if someone_won(board) or board_full(board):
                    break
            display_board(board)

            if someone_won(board):
                prompt(f"{detect_winner(board)} won!")
                if detect_winner(board) == "Player":
                    player_score += 1
                elif detect_winner(board) == 'Computer':
                    computer_score += 1

            else:
                prompt("Its a tie!")

            if player_score == 4 or computer_score == 4:
                if player_score == 4:
                    prompt("You've won the match!")
                else:
                    prompt("The Computer has won the match!")
                break
            prompt(f'Player: {player_score} Computer: {computer_score}')
            if not start_new_round('Are you ready for the next round? (y or n)'):
                break

        if not start_new_round("Would you like to start another match? (y or n)"):
            break

        prompt("Thanks for playing Tic Tac Toe!")
play_tic_tac_toe()
